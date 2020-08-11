from urllib.request import urlopen,Request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver # webdriver 가져오기
import time


baseUrl = "https://www.bing.com/images/search?q="
baseUrl2 = "&form=HDRSC2&first=1&scenario=ImageBasicHover"
plusUrl = input("검색어를 입력하세요 : ")

url = baseUrl + quote_plus(plusUrl) + baseUrl2

driver = webdriver.Chrome(
        executable_path = "C:/Users/multicampus/chromedriver_win32/chromedriver.exe"
    )

driver.get(url)
time.sleep(1)

# for i in range(10):
    # driver.execute_script('window.scrollBy(0,10000)')


SCROLL_PAUSE_TIME = 1.0
images = []
cnt = 0 
    # cnt 10당 => 약 120~150개사이의 데이터를 축적
while cnt < 5:
    cnt += 1
    pageString = driver.page_source
    bsObj = BeautifulSoup(pageString, 'lxml')
    try:
        for line in bsObj.find_all(name='div', attrs={"class":"img_cont hoff"}):
            page = line.find(name="img")["src"]
            if page.find("data:image/jpeg") == -1:
                images.append(page)
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
    images = list(set(images))
driver.close()    

for row in images:
    print(row)