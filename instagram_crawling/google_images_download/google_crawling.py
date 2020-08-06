from google_images_download import google_images_download
# pip install git+https://github.com/Joeclinton1/google-images-download.git 설치 진행
import time
import os
response = google_images_download.googleimagesdownload()

def imageCrawling(keyword):
    arguments = {
        "keywords" : keyword,
        "limit" : 130,
        "print_url":True,
        }
    # print(arguments)
    paths = response.download(arguments)

search = input("검색어:")
imageCrawling(search)