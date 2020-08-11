from urllib.request import urlopen,Request # 인터넷 url를 열어주는 패키지
from urllib.parse import quote_plus # 한글을 유니코드 형식으로 변환해줌
from bs4 import BeautifulSoup # BeautifulSoup: 웹 크롤링이나 스크래핑할떄 쓰이는 python 라이브러리
from selenium import webdriver # webdriver 가져오기
import time # 크롤링 중 시간 대기를 위한 패키지
import warnings # 경고메시지 제거 패키지
from tqdm import tqdm
from selenium.webdriver.common.keys import Keys 
import pandas as pd
import json
from collections import OrderedDict
from datetime import datetime
import requests
# custom functions
from insta_modal import modal_images
from server import SELECT
from cnn_predict import Predict
from person import person_filter

warnings.filterwarnings(action='ignore') # 경고 메세지 제거

#식당에 대한 정보를 입력
baseUrl = "https://www.instagram.com/explore/tags/"
plusUrl = input('식당명을 입력하세요 : ')
en_name = input('식당의 영어명을 입력하세요 : ')
irid = int(input('식당의 rid값을 입력하세요: '))
ko_search = list(input().split())
en_search = list(input().split())

#########################################################################
# 1. 인스타 그램 url 생성 
#########################################################################

url = baseUrl + quote_plus(plusUrl)
# [2] chromedriver 띄운다.
driver = webdriver.Chrome(
    executable_path= "C:/Users/multicampus/chromedriver_win32/chromedriver.exe"
)

driver.get(url)
time.sleep(2)

# [3] 로그인 하기
# 로그인 버튼 클릭
login_section = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button'
driver.find_element_by_xpath(login_section).click()
time.sleep(2)

# 계정, 비밀번호 압력
elem_login = driver.find_element_by_name("username")
elem_login.clear()
elem_login.send_keys('silver_jae@naver.com')
time.sleep(1)
elem_login = driver.find_element_by_name('password')
elem_login.clear()
elem_login.send_keys('ssafy%qks')
time.sleep(0.5)

# 로그인 버튼 클릭
# xpath = """//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button"""
xpath = """//*[@id="loginForm"]/div/div[3]/button/div"""
driver.find_element_by_xpath(xpath).click()
time.sleep(3)

# 건너뛰기 클릭
passbutton="""//*[@id="react-root"]/section/main/div/div/div/div/button"""
driver.find_element_by_xpath(passbutton).click()
time.sleep(3)

# [4] 스크롤을 하면서 데이터 축적 cnt = 1당 약 12~ 15개의 게시글데이터를 축적
SCROLL_PAUSE_TIME = 1.0
modal_page = []
cnt = 0 
while cnt < 1:
    cnt += 1
    pageString = driver.page_source
    bsObj = BeautifulSoup(pageString, 'lxml')
    # [5] 크롤링하 데이터의 모달 페이지를 추출해내어 modal_page에 push
    try:
    # bsObj는 웹에서 모든 데이터를 크롤링한 결과데이터
        for line in bsObj.find_all(name='div', attrs={"class":"Nnq7C weEfm"}): # "class":"Nnq7C weEfm"는 이미지를 가리키는 클래스
            # 인스타는 1row 마다 3 column이 있음 => 1개의 line마다 3개의 개시글 데이터가존재
            for i in range(3):
                title = line.select('a')[i]
                real = title.attrs['href']   
                modal_page.append(real)
    except IndexError as ider:
        print("IndexError")

    last_height = driver.execute_script('return document.body.scrollHeight')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        else:
            last_height = new_height
            continue
    time.sleep(0.3)


#########################################################################
# 2. 크롤링한 데이터에서 계정 modal_page 
#########################################################################
modal_page = list(set(modal_page)) # 모든 게시글 모달창 주소 리스트
num_of_data = len(modal_page)
file_data = []
print('총 {0}개의 데이터를 수집합니다.'.format(num_of_data))
for i in tqdm(range(num_of_data)):
    # [1] data의 구조를 미리 정의 
    data = OrderedDict()
    data = {
        "irid" : "",
        "rname" : "",
        "rbranch" : "", # 지점명은 일단 비워두자
        "instaid" : "",
        "iurl" : "",
        "ifood": "",
        "likes" : "",
        "idate" : "",
    }

    # [2] 해당 모달창에 이동하여 계정, 좋아요, 이미지 url을 추출
    req = Request("https://www.instagram.com"+modal_page[i], headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'lxml', from_encoding='utf-8  ')
    info = soup.find('meta', attrs={'property':"og:description"})
    total = info['content']

    # 계정을 추출하여 db와  비교
    account = total[total.find("@")+1 : total.find(")")]
    account = account[:20]
    if account == '':
        account = "Null"
    account = account.replace('posted on','')
    account = account.replace('shared a post on','')
    account = account.replace('on Instagram','')
    account = account.replace(' ','')
    print(account)
#########################################################################
# 3. DB와 인스타 계정비교
#########################################################################

    # DB에 계정이 없으면 continue
    # if not SELECT(account):
    #     continue


#########################################################################
# 4. 이미지를 추출하여 유사도 측정
#########################################################################
    # [1] 해당 모달의 이미지 모두 긁어옴
    # 이미지 저장

    src_list = []
    url = "https://www.instagram.com"+modal_page[i]
    src_list = modal_images(url)
    print("src_list ==>", src_list)
    
    # [2] 사전에 학습된 cnn 모델로 음식 이미지 판단하고 url을 넘김
    # res_url : 음식이 담긴 url
    # res_menu : 음식의 종류
    res_url_menu = Predict(src_list, en_search) 
    print("음식 분류 완료!!!!!!!!!!!!!!!!!")

    # [3] 해당 url에서 사람 이미지 필터링
    res = person_filter(res_url_menu)
    print("사람 필터링 완료!!!!!!!!!!!!!!!!!")
    print("res ==>", res)

    # [4] 기타 계정 정보 추출
    # 좋아요
    likes = 0
    if total.find("Likes") != -1:
        likes = total[0:total.find("Likes")-1 ]
        likes = likes.replace(',','')
    if 'k' in str(likes):
        likes = likes.replace('k','')
        likes = float(likes)*1000

    # 현재시간
    my_date = datetime.now()

    # # 댓글수
    # comments = 0
    # if total.find("Comments") != -1:
    #     comments = total[total.find(",")+2: total.find("Comments")]

    for food_info in res:
        food_info[0] = img_url
        food_info[1] = food
        data["irid"] = irid
        data["rname"] = en_name 
        data["instaid"] = account
        data["iurl"] = img_url
        data["ifood"] = food
        data["likes"] = int(likes)
        data["idate"] = my_date.isoformat()
        file_data.append(data)
        print(data)
# json 파일로 저장
with open(en_name + '.json', 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
driver.close()