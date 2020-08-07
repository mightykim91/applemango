from urllib.request import urlopen,Request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver # webdriver 가져오기
import time
import os

# plusUrl = input("검색어를 입력하세요 : ")
search = list(input().split())
print(search)
for plusUrl in search:
    print(plusUrl)
    baseUrl = "https://www.bing.com/images/search?q="
    baseUrl2 = "&form=HDRSC2&first=1&scenario=ImageBasicHover"

    try:
        if not os.path.exists("./cnn_sample/"+plusUrl):
            os.makedirs("./cnn_sample/"+plusUrl)
    except OSError:
        print('Error:Creating Directory' + plusUrl)


    url = baseUrl + quote_plus(plusUrl) + baseUrl2
    driver = webdriver.Chrome(
            executable_path = "C:/Users/multicampus/chromedriver_win32/chromedriver.exe"
        )
    driver.get(url)
    time.sleep(1)

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


    # n = 1
    # for url in images:
    #     with urlopen(url) as f:
    #         with open('./cnn_sample/'+plusUrl+"/"+plusUrl+str(n)+'.jpg','wb') as h: #
    #             img = f.read()
    #             h.write(img)
    #         n += 1



    # import tensorflow as tf
    # import tensorflow_hub as hub
    import wget
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

    # # , method=ResizeMethod.BILINEAR, align_corners=False

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


    # 2. target이미지 및 비교 이미지 다운로드 
    # target_image_url = "https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F9907F84D5C558B9429"

    # target_img_path = target_image_url

    # target_img_path = './cnn_sample/' + plusUrl + "/" + 'target_img.jpg'

    input_img_paths = []
    # urllib.error.URLError : url에서 다운받을때 해당 에러가능성있음
    # wget -q {target_image_url} -O {target_img_path}

    # wget.download(target_image_url,target_img_path)

    # url 주소로 이미지 따올때,
    for i, url in enumerate(images):
        if len(url) > 0:
            input_path = './cnn_sample/' + plusUrl + "/" + "input_img%d.jpg" % i
            try:
                wget.download(url,input_path)
                input_img_paths.append(input_path)
            except:
                print("url error")

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