from urllib.request import urlopen,Request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver # webdriver 가져오기
import time
import os
import time
from similarity_measure import Similarity_Measurement

ko_search = list(input("한글 음식명:").split())
en_search = list(input("영어 음식명:").split())
stan_search = list(input("target image url:").split())
print(stan_search)
####################################################################################
# 폴더의 유무 filter
####################################################################################
k_categories = []
e_categories = []
url_categories = []
folder_path = './cnn_sample/'
for i in range(len(en_search)):
    k_name = ko_search[i]
    e_name = en_search[i]
    url_name = stan_search[i]
    image_dir = folder_path + e_name + '/'
    # print(image_dir)
    if os.path.exists(image_dir): # 크롤링 이미지가 존재하면 => True
        continue
    else:
        k_categories.append(k_name)
        e_categories.append(e_name)
        url_categories.append(url_name)

####################################################################################
# bing.com에서 이미지 크롤링
####################################################################################
start = time.time()  # 시작 시간 저장
for i in range(len(k_categories)):
    ko_name = k_categories[i]
    en_name = e_categories[i]
    url_name = url_categories[i]

    baseUrl = "https://www.bing.com/images/search?q="
    baseUrl2 = "&form=HDRSC2&first=1&scenario=ImageBasicHover"
    # 웹페이지를 안보이게해줌
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')

    url = baseUrl + quote_plus(ko_name) + baseUrl2
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
    while cnt < 30: # cnt 10당 => 약 500개 사이의 이미지 데이터 추출
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

####################################################################################
# 2. 유사도 비교후 저장
####################################################################################
    # cnn_sample에 폴더 만들기 (폴더는 영어이름으로만 지정)
    try:
        if not os.path.exists("./cnn_sample/"+en_name):
            os.makedirs("./cnn_sample/"+en_name)
    except OSError:
        print('Error:Creating Directory' + en_name)
    Similarity_Measurement(url_path, en_name, url_name)


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
    