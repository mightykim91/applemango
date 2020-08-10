
from urllib.request import urlopen,Request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver # webdriver 가져오기
import time
import os
import time

# plusUrl = input("검색어를 입력하세요 : ")
####################################################################################
# 폴더의 유무 filter
####################################################################################
def bing_filter(ko_search,en_search):
    k_categories = []
    e_categories = []
    folder_path = './cnn_sample/'

    for i in range(len(en_search)):
        k_name = ko_search[i]
        e_name = en_search[i]
        image_dir = folder_path + e_name + '/'
        # print(image_dir)
        if os.path.exists(image_dir): # 크롤링 이미지가 존재하면 => True
            continue
        else:
            k_categories.append(k_name)
            e_categories.append(e_name)
    return k_categories, e_categories

####################################################################################
# bing.com에서 이미지 크롤링
####################################################################################
def bing_crawling(k_categories, e_categories):
    start = time.time()  # 시작 시간 저장
    for i in range(len(k_categories)):
        ko_name = k_categories[i]
        en_name = e_categories[i]

        baseUrl = "https://www.bing.com/images/search?q="
        baseUrl2 = "&form=HDRSC2&first=1&scenario=ImageBasicHover"

        url = baseUrl + quote_plus(ko_name) + baseUrl2
        driver = webdriver.Chrome(
                executable_path = "C:/Users/multicampus/chromedriver_win32/chromedriver.exe"
            )
        driver.get(url)
        time.sleep(1)

        SCROLL_PAUSE_TIME = 1.0
        url_path = []
        cnt = 0 
        ####################################################################################
        # 1. 이미지 url 수집
        ####################################################################################
        while cnt < 50: # cnt 10당 => 약 120~150개사이의 데이터를 축적
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
    # 2. 사람 filter
    ####################################################################################

        import cv2
        import numpy as np
        from os import listdir
        from os.path import isfile, join
        from skimage import io  # url 이미지 읽는 라이브러리
        # 테스트 이미지 불러오기
        # root_path='./cnn_sample/'
        path = './data/haarcascades'
        personfiles = ['haarcascade_eye.xml', 'haarcascade_eye_tree_eyeglasses.xml', 'haarcascade_frontalcatface.xml', 'haarcascade_frontalcatface_extended.xml', 'haarcascade_frontalface_alt.xml', 'haarcascade_frontalface_alt2.xml', 'haarcascade_frontalface_alt_tree.xml', 'haarcascade_frontalface_default.xml', 'haarcascade_fullbody.xml', 'haarcascade_lefteye_2splits.xml', 'haarcascade_lowerbody.xml', 'haarcascade_profileface.xml', 'haarcascade_righteye_2splits.xml', 'haarcascade_russian_plate_number.xml', 'haarcascade_upperbody.xml']
        
        # L = len(url_path)
        for url in url_path:
            image = io.imread(url)  # skimage.io 를 이용한 url 이미지 불러오기
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            for p in personfiles:
                person_cascade = cv2.CascadeClassifier('./data/haarcascades/' + p)
                person = person_cascade.detectMultiScale(image_gray, 1.3, 5)
                if len(person) != 0:
                    url_path.remove(url)
                    print("사람입니다.")
                    break

    ####################################################################################
    # 3. 파일 저장
    ####################################################################################

        # cnn_sample에 폴더 만들기 (폴더는 영어이름으로만 지정)
        try:
            if not os.path.exists("./cnn_sample/"+en_name):
                os.makedirs("./cnn_sample/"+en_name)
        except OSError:
            print('Error:Creating Directory' + en_name)

        # print(url_path)
        # 크롤링한 url 이미지를 jpg로 저장함
        n = 1
        for url in url_path:
            with urlopen(url) as f:
                with open('./cnn_sample/'+en_name+"/"+en_name+str(n)+'.jpg','wb') as h:
                    img = f.read()
                    h.write(img)
                n += 1

    print("총 걸린 시간 :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
    
####################################################################################
# 유사도 필터링 filter
####################################################################################
    # import tensorflow as tf
    # import tensorflow_hub as hub
    # import wget
    # import time
    # from IPython.display import Image, display
    # # import shutil

    # CHANNELS = 3 # number of image channels (RGB)
    # def build_graph(hub_module_url, target_image_path):
    #   # Step 1) Prepare pre-trained model for extracting image features.
    #   module = hub.Module(hub_module_url)
    #   height, width = hub.get_expected_image_size(module)

    #   # Copied a method of https://github.com/GoogleCloudPlatform/cloudml-samples/blob/bf0680726/flowers/trainer/model.py#L181
    #   # and fixed for all type images (not only jpeg)
    #   def decode_and_resize(image_str_tensor):
    #     """Decodes jpeg string, resizes it and returns a uint8 tensor."""
    #     image = tf.image.decode_image(image_str_tensor, channels=CHANNELS)
    #     # Note resize expects a batch_size, but tf_map supresses that index,
    #     # thus we have to expand then squeeze.  Resize returns float32 in the
    #     # range [0, uint8_max]
    #     image = tf.expand_dims(image, 0)
    #     # image = tf.image.resize(
    #     #     image, [height, width], method=ResizeMethod, align_corners=False)
    #     image = tf.image.resize(
    #                 image, [height, width], method=tf.image.ResizeMethod.BILINEAR)

    #     image = tf.squeeze(image, squeeze_dims=[0])
    #     image = tf.cast(image, dtype=tf.uint8)
    #     return image

    #   def to_img_feature(images):
    #     """Extract the feature of image vectors"""
    #     outputs = module(dict(images=images), signature="image_feature_vector", as_dict=True)
    #     return outputs['default']

    #   # Step 2) Extract image features of the target image.
    #   target_image_bytes = tf.io.gfile.GFile(target_image_path, 'rb').read()
    #   target_image = tf.constant(target_image_bytes, dtype=tf.string)
    #   target_image = decode_and_resize(target_image)
    #   target_image = tf.image.convert_image_dtype(target_image, dtype=tf.float32)
    #   target_image = tf.expand_dims(target_image, 0)
    #   target_image = to_img_feature(target_image)

    #   # Step 3) Extract image features of input images.
    #   input_byte = tf.placeholder(tf.string, shape=[None])
    #   input_image = tf.map_fn(decode_and_resize, input_byte, back_prop=False, dtype=tf.uint8)
    #   input_image = tf.image.convert_image_dtype(input_image, dtype=tf.float32)
    #   input_image = to_img_feature(input_image)

    #   # Step 4) Compare cosine_similarities of the target image and the input images.
    #   dot = tf.tensordot(target_image, tf.transpose(input_image), 1)
    #   similarity = dot / (tf.norm(target_image, axis=1) * tf.norm(input_image, axis=1))
    #   similarity = tf.reshape(similarity, [-1])

    #   return input_byte, similarity


    # # 2. target이미지 및 비교 이미지 다운로드 
 
    # target_img_path = target_image_url

    # target_img_path = './cnn_sample/' + plusUrl + "/" + 'target_img.jpg'

    # input_img_paths = []
    # # urllib.error.URLError : url에서 다운받을때 해당 에러가능성있음
    # # wget -q {target_image_url} -O {target_img_path}

    # wget.download(target_image_url,target_img_path)

    # # url 주소로 이미지 따올때,
    # for i, url in enumerate(images):
    #     if len(url) > 0:
    #         input_path = './cnn_sample/' + plusUrl + "/" + "input_img%d.jpg" % i
    #         try:
    #             wget.download(url,input_path)
    #             input_img_paths.append(input_path)
    #         except:
    #             print("url error")

    # tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
    # # tf.logging.set_verbosity(tf.compat.v1.logging.ERROR)

    # # Load bytes of image files
    # # image_bytes = [tf.gfile.GFile(name, 'rb').read() for name in [[target_img_path] + input_img_paths]]
    # image_bytes = [tf.io.gfile.GFile(name, 'rb').read() for name in ([target_img_path] + input_img_paths)]

    # hub_module_url = "https://tfhub.dev/google/imagenet/mobilenet_v2_100_96/feature_vector/1" #@param {type:"string"}

    # with tf.Graph().as_default():
    #   input_byte, similarity_op = build_graph(hub_module_url, target_img_path)
    #   print("<==input_byte, similarity_op ==>" , input_byte, similarity_op)

    #   with tf.Session() as sess:
    #     sess.run(tf.global_variables_initializer())
    #     t0 = time.time() # for time check
        
    #     # Inference similarities
    #     similarities = sess.run(similarity_op, feed_dict={input_byte: image_bytes})
    #     print("%d images inference time: %.2f s" % (len(similarities), time.time() - t0))

    # # Display results
    # print("# Target image")
    # display(Image(target_img_path))
    # print("- similarity: %.2f" % similarities[0])

    # print("# Input images")
    # cnt1 = cnt2 = 0
    # cnt1_lst = []
    # cnt2_lst = []
    # for similarity, input_img_path in zip(similarities[1:], input_img_paths):
    #   display(Image(input_img_path))
    #   print(input_img_path,"의 유사도는 ","- similarity: %.2f" % similarity)
    #   if similarity >= 0.3:
    #     cnt1 +=1
    #     cnt1_lst.append(input_img_path)
    #     # shutil.move(input_img_path,'./upper/'+input_img_path)
    #   else:
    #     cnt2 +=1
    #     cnt2_lst.append(input_img_path)
        
    #     # shutil.move(input_img_path,'./under/'+input_img_path)
    # print(cnt1_lst)
    # print("=====================================")
    # print(cnt2_lst)