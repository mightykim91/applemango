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
warnings.filterwarnings(action='ignore') # 경고 메세지 제거

def modal_images(url):
    driver = webdriver.Chrome(
        executable_path= "C:/Users/multicampus/chromedriver_win32/chromedriver.exe"
    )
    # 해당 url을 driver로 할당
    driver.get(url)
    time.sleep(1)

    img_list = []
    # [3] 첫번째 (>) 버튼
    # pageString = driver.page_source
    # bsObj = BeautifulSoup(pageString, 'lxml')
    # line = bsObj.find_all(name='div', attrs={"class":"KL4Bh"})
    # title = line.select('img')
    # real = title.attrs['src']
    # modal_page.append(real)

    # first_button = '//*[@id="react-root"]/section/main/div/div/article/div[2]/div/div[1]/div[2]/div/button'
    first_button = '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[1]/div[2]/div/button'
    second_button='//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[1]/div[2]/div/button[2]'
    # second_button = '//*[@id="react-root"]/section/main/div/div/article/div[2]/div/div[1]/div[2]/div/button[2]'
    
    for cnt in range(1,10):
        # 첫번째 사진은 무조건 plus
        pageString = driver.page_source
        soup = BeautifulSoup(pageString, 'lxml')
        img = soup.select("img[srcset]")
        img_list += img
        img_list = list(set(img_list))

        if cnt == 1:
            try:
                driver.find_element_by_xpath(first_button).click()
            except:
                print('모든사진을 로드했습니다.')
                break
        else:
            try:
                driver.find_element_by_xpath(second_button).click()
            except:
                print('모든사진을 로드했습니다.')
                break
        time.sleep(0.5)

    # print(img_list)
    src_list = []
    for pic in img_list:
        if pic['class'] != ['FFVAD']:
            continue
        srcset = pic.attrs['srcset']
        srcset_list = srcset.split(",")
        item = srcset_list[len(srcset_list)-1]
        img_url = item[:item.find(" ")]
        src_list.append(img_url)      
    # 중복제거를 위해 집합으로 변경 후 리스트로 다시 변환
    src_list = list(set(src_list))

    return src_list

# url = "https://www.instagram.com/p/CCK6V4hnlY2/" # 여러장의 사진
# modal_images(url)