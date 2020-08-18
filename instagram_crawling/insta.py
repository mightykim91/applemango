# -*- coding: utf-8 -*- 
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
from server_select import SELECT
from cnn_predict import Predict
from person import person_filter
from menu import find_name
# from text_filter import Text_Filtering_url

warnings.filterwarnings(action='ignore') # 경고 메세지 제거
start = time.time()
#식당에 대한 정보를 입력
baseUrl = "https://www.instagram.com/explore/tags/"
plusUrl = input('식당명을 입력하세요 : ')
en_name = input('식당의 영어명을 입력하세요 : ')
irid = int(input('식당의 rid값을 입력하세요: '))
ko_search = list(input("음식명:").split())
en_search = find_name(ko_search)
# ko_search = ['알밥','비빔밥','비빔면','보쌈','불고기','닭갈비', '닭볶음탕', '된장찌개', '돈까스', '두부김치', '갈비', '갈비찜', '갈치구이', '김밥', '김치볶음밥', '김치전', '김치찌개', '곱창', '계란후라이', '계란찜', '계란말이', '호박전', '후라이드치킨', '훈제오리', '잔치국수', '장어구이', '제육볶음', '짜장면', '짬뽕', '쫄면', '쭈구미볶음', '조개구이', '족발', '조기구이', '주먹밥', '칼국수', '콩국수', '콩나물국밥', '라면','막국수', '만두', '미역국', '물회', '물냉면','오징어튀김' ,'파스타','피자', '생선구이', '새우볶음밥', '새우튀김', '삼겹살', '삼계탕' ,'산낙지', '설렁탕','수제비','순대', '순대국밥', '탕수육', '떡볶이','떡국', '우동', '양념치킨','유뷰초밥', '육회'] 
# en_search = ['albab', 'bibimbab', 'bibimnaengmyeon', 'bossam', 'bulgogi', 'dalg-galbi', 'dalgbokk-eumtang', 'doenjangjjigae', 'donkkaseu', 'dubugimchi', 'galbi', 'galbijjim', 'galchigu-i', 'gimbab', 'gimchibokk-eumbab', 'gimchijeon', 'gimchijjigae', 'gobchang', 'gyelanhulai', 'gyelanjjim', 'gyelanmal-i', 'hobagjeon', 'hulaideuchikin', 'hunje-oli', 'janchigugsu', 'jang-eogu-i', 'jeyugbokk-eum', 'jjajangmyeon', 'jjamppong', 'jjolmyeon', 'jjukkumibokk-eum', 'jogaegu-i', 'jogbal', 'jogigu-i', 'jumeogbab', 'kalgugsu', 'kong-gugsu', 'kongnamulgug', 'lamyeon', 'maggugsu', 'mandu', 'miyeoggug', 'mulhoe', 'mulnaengmyeon', 'ojing-eotwigim', 'paseuta', 'pija', 'saengseonjeon', 'saeubokk-eumbab', 'saeutwigim', 'samgyeobsal', 'samgyetang', 'sannagji', 'seolleongtang', 'sujebi', 'sundae', 'sundaegugbab', 'tangsuyug', 'tteogbokk-i', 'tteoggug', 'udong', 'yangnyeomchikin', 'yubuchobab', 'yughoe']
# en_search = list(input('식당의 음식을 영어(폴더명)로 입력하세요: ').split())
print(len(ko_search), len(en_search))
#########################################################################
# 1. 인스타 그램 url 생성 
#########################################################################

# 웹페이지를 안보이게해줌
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')

url = baseUrl + quote_plus(plusUrl)
# [2] chromedriver 띄운다.
driver = webdriver.Chrome(
    executable_path= "C:/Users/multicampus/chromedriver_win32/chromedriver.exe",
    chrome_options=options)
driver.get(url)
time.sleep(2)

# [3] 로그인 하기
# 로그인 버튼 클릭
try:
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
except:
    print("인스타 로그인 에러 발생!!!")
    
# [4] 스크롤을 하면서 데이터 축적 cnt = 1당 약 12~ 15개의 게시글데이터를 축적
SCROLL_PAUSE_TIME = 1.0
modal_page = []
cnt = 0 
while cnt < 5:
    cnt += 1
    print(cnt,"번 크롤링을 진행중입니다.")
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
    modal_page = list(set(modal_page))
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
    # data = OrderedDict()
    
    # [2] 해당 모달창에 이동하여 계정, 좋아요, 이미지 url을 추출
    req = Request("https://www.instagram.com"+modal_page[i], headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'lxml', from_encoding='utf-8  ')
    info = soup.find('meta', attrs={'property':"og:description"})
    total = info['content']

    # 계정을 추출하여 db와  비교
    account = total[total.find("@")+1 : total.find(")")]
    account = account[:20]
    print("======================")
    print(account)
    if account == '':
        account = "Null"
    num = account.find(':')
    num2 = account.find(' ')
    if num2 != -1:
        account=account.replace(account[num2:],"")
    if num >= 0:
        account=account.replace(account[num:],"") 
    account = account.replace('posted on','')
    account = account.replace('shared a post on','')
    account = account.replace('on Instagram','')
    # account = account.replace(' ','')
    print(account,"을 추출했습니다.")
#########################################################################
# 3. DB와 인스타 계정비교
#########################################################################

    # DB에 계정이 없으면 continue
    if SELECT(account):
        print(account,"님은 애플망고 회원이 아닙니다.")
        continue
    print("애플망고 회원임을 확인했습니다.")
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
    if len(src_list) == 0:
        continue
    res_url_menu = Predict(src_list, ko_search) 
    print("음식 분류 완료!!!!!!!!!!!!!!!!!")
    
    # [3] 해당 url에서 사람 이미지 필터링
    if len(res_url_menu) ==0:
        continue
    res = person_filter(res_url_menu)
    print("사람 필터링 완료!!!!!!!!!!!!!!!!!")
    # print("res ==>", res)

    # [3] 기타 계정 정보 추출
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
        print("##########################################################################")
        print("food_info ==>", food_info)
        data = {
            "irid" : "",
            "rname" : "",
            "rbranch" : "", # 지점명은 일단 비워두자
            "instaid" : "",
            "iurl" : "",
            "likes" : "",
            "idate" : ""}

        img_url = food_info[0]
        data["irid"] = irid
        data["rname"] = en_name 
        data["instaid"] = account
        data["iurl"] = img_url
        # data["ifood"] = food
        data["likes"] = int(likes)
        data["idate"] = my_date.isoformat()
        file_data.append(data)
print("총 걸린 시간은 : ",time.time()-start)
# json 파일로 저장
with open('jsonfile/' + en_name + '.json', 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
driver.close()