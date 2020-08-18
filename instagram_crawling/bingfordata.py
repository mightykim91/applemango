from urllib.request import urlopen,Request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver # webdriver 가져오기
import time
import os
from similarity_measure import Similarity_Measurement

ko_search = list(input("한글 음식명:").split())
en_search = list(input("영어 음식명:").split())
stan_search = list(input("target image url:").split())
# print(stan_search)
####################################################################################
# 폴더의 유무 filter
####################################################################################
k_categories = []
e_categories = []
url_categories = []
start = time.time()
folder_path = './cnn_sample/'
for i in range(len(en_search)):
    k_name = ko_search[i]
    e_name = en_search[i]
    url_name = stan_search[i]
    image_dir = folder_path + e_name + '/'
    # print(image_dir)
    if os.path.exists(image_dir): # 크롤링 이미지가 존재하면 => True
        print(k_name + "의 이미지데이터는 이미 존재합니다.")
        continue
    else:
        k_categories.append(k_name)
        e_categories.append(e_name)
        url_categories.append(url_name)

####################################################################################
# bing.com에서 이미지 크롤링
####################################################################################

for i in range(len(k_categories)):
    ko_name = k_categories[i]
    en_name = e_categories[i]
    url_name = url_categories[i]
    start2 = time.time()  # 시작 시간 저장
    print(ko_name + "의 데이터 수집 시작")

    # bing
    baseUrl = "https://www.bing.com/images/search?q="
    baseUrl2 = "&form=HDRSC2&first=1&scenario=ImageBasicHover"
    # google
    # baseUrl = "https://www.google.co.kr/search?q="
    # baseUrl2 = "&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjK4aCV1ZnrAhXUMN4KHYBPBJQQ_AUoAXoECBAQAw&cshid=1597372755447732&biw=1536&bih=722"
    # 웹페이지를 안보이게해줌
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')

    url = baseUrl + quote_plus(ko_name) + baseUrl2
    print(url)
    driver = webdriver.Chrome(
            executable_path = "C:/Users/multicampus/chromedriver_win32/chromedriver.exe",
            chrome_options=options)
    
    driver.get(url)
    time.sleep(1)

    SCROLL_PAUSE_TIME = 1.0
    url_path = []
    cnt = 0 
    ####################################################################################
    # 1. 이미지 url 수집
    ####################################################################################
    while cnt < 50: # cnt 10당 => 약 500개 사이의 이미지 데이터 추출
        print(cnt)
        cnt += 1
        pageString = driver.page_source
        bsObj = BeautifulSoup(pageString, 'lxml')
        try:
            for line in bsObj.find_all(name='div', attrs={"class":"img_cont hoff"}):
                page = line.find(name="img")["src"]
                if page.find("data:image/jpeg") == -1:
                    url_path.append(page)
        
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
        url_path = list(set(url_path))
    driver.close()
    url_path = list(set(url_path))
    print("추출된 url 개수는 : ",len(url_path))
####################################################################################
# 2. 유사도 비교후 저장
####################################################################################
    # [1] cnn_sample에 폴더 만들기 (폴더는 영어이름으로만 지정)
    try:
        if not os.path.exists("./cnn_sample/"+en_name):
            os.makedirs("./cnn_sample/"+en_name)
    except OSError:
        print('Error:Creating Directory' + en_name)
    
    # [2] 유사도 비교
    Similarity_Measurement(url_path, en_name, url_name)

    # [3] text 필터링
    # Text_Filtering_jpg(en_name)

    print(ko_name , "의 걸린 시간 : " , time.time() - start2)

    # # print(url_path)
    # # 크롤링한 url 이미지를 jpg로 저장함
    # n = 1
    # for url in url_path:
    #     with urlopen(url) as f:
    #         with open('./cnn_sample/'+en_name+"/"+en_name+str(n)+'.jpg','wb') as h:
    #             img = f.read()
    #             h.write(img)
    #         n += 1

print("총 걸린 시간 :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
    