import tensorflow as tf
import tensorflow_hub as hub
import wget
import time
from IPython.display import Image, display
import shutil

CHANNELS = 3 # number of image channels (RGB)
def build_graph(hub_module_url, target_image_path):
  # Step 1) Prepare pre-trained model for extracting image features.
  module = hub.Module(hub_module_url)
  height, width = hub.get_expected_image_size(module)

  # Copied a method of https://github.com/GoogleCloudPlatform/cloudml-samples/blob/bf0680726/flowers/trainer/model.py#L181
  # and fixed for all type images (not only jpeg)
  def decode_and_resize(image_str_tensor):
    """Decodes jpeg string, resizes it and returns a uint8 tensor."""
    image = tf.image.decode_image(image_str_tensor, channels=CHANNELS)
    # Note resize expects a batch_size, but tf_map supresses that index,
    # thus we have to expand then squeeze.  Resize returns float32 in the
    # range [0, uint8_max]
    image = tf.expand_dims(image, 0)
    image = tf.image.resize(
    image, [height, width], align_corners=False)
    image = tf.squeeze(image, squeeze_dims=[0])
    image = tf.cast(image, dtype=tf.uint8)
    return image

  def to_img_feature(images):
    """Extract the feature of image vectors"""
    outputs = module(dict(images=images), signature="image_feature_vector", as_dict=True)
    return outputs['default']

  # Step 2) Extract image features of the target image.
  target_image_bytes = tf.io.gfile.GFile(target_image_path, 'rb').read()
  target_image = tf.constant(target_image_bytes, dtype=tf.string)
  target_image = decode_and_resize(target_image)
  target_image = tf.image.convert_image_dtype(target_image, dtype=tf.float32)
  target_image = tf.expand_dims(target_image, 0)
  target_image = to_img_feature(target_image)

  # Step 3) Extract image features of input images.
  input_byte = tf.placeholder(tf.string, shape=[None])
  input_image = tf.map_fn(decode_and_resize, input_byte, back_prop=False, dtype=tf.uint8)
  input_image = tf.image.convert_image_dtype(input_image, dtype=tf.float32)
  input_image = to_img_feature(input_image)

  # Step 4) Compare cosine_similarities of the target image and the input images.
  dot = tf.tensordot(target_image, tf.transpose(input_image), 1)
  similarity = dot / (tf.norm(target_image, axis=1) * tf.norm(input_image, axis=1))
  similarity = tf.reshape(similarity, [-1])

  return input_byte, similarity

# def inter(url_path,en_name):
#   print(en_name)
url_path = ['./cnn_sample/donkkaseu/target_img.jpg', './cnn_sample/donkkaseu/input_img0.jpg', './cnn_sample/donkkaseu/input_img1.jpg', './cnn_sample/donkkaseu/input_img2.jpg', './cnn_sample/donkkaseu/input_img3.jpg', './cnn_sample/donkkaseu/input_img4.jpg', './cnn_sample/donkkaseu/input_img5.jpg', './cnn_sample/donkkaseu/input_img6.jpg', './cnn_sample/donkkaseu/input_img7.jpg', './cnn_sample/donkkaseu/input_img8.jpg', './cnn_sample/donkkaseu/input_img9.jpg', './cnn_sample/donkkaseu/input_img10.jpg', './cnn_sample/donkkaseu/input_img11.jpg', './cnn_sample/donkkaseu/input_img12.jpg', './cnn_sample/donkkaseu/input_img13.jpg', './cnn_sample/donkkaseu/input_img14.jpg', './cnn_sample/donkkaseu/input_img15.jpg', './cnn_sample/donkkaseu/input_img16.jpg', './cnn_sample/donkkaseu/input_img17.jpg', './cnn_sample/donkkaseu/input_img18.jpg', './cnn_sample/donkkaseu/input_img19.jpg', './cnn_sample/donkkaseu/input_img20.jpg', './cnn_sample/donkkaseu/input_img21.jpg', './cnn_sample/donkkaseu/input_img22.jpg', './cnn_sample/donkkaseu/input_img23.jpg', './cnn_sample/donkkaseu/input_img24.jpg', './cnn_sample/donkkaseu/input_img25.jpg', './cnn_sample/donkkaseu/input_img26.jpg', './cnn_sample/donkkaseu/input_img27.jpg', './cnn_sample/donkkaseu/input_img28.jpg', './cnn_sample/donkkaseu/input_img29.jpg', './cnn_sample/donkkaseu/input_img30.jpg', './cnn_sample/donkkaseu/input_img31.jpg', './cnn_sample/donkkaseu/input_img32.jpg', './cnn_sample/donkkaseu/input_img33.jpg', './cnn_sample/donkkaseu/input_img34.jpg', './cnn_sample/donkkaseu/input_img35.jpg', './cnn_sample/donkkaseu/input_img36.jpg', './cnn_sample/donkkaseu/input_img37.jpg', './cnn_sample/donkkaseu/input_img38.jpg', './cnn_sample/donkkaseu/input_img39.jpg', './cnn_sample/donkkaseu/input_img40.jpg', './cnn_sample/donkkaseu/input_img41.jpg', './cnn_sample/donkkaseu/input_img42.jpg', './cnn_sample/donkkaseu/input_img43.jpg', './cnn_sample/donkkaseu/input_img44.jpg', './cnn_sample/donkkaseu/input_img45.jpg', './cnn_sample/donkkaseu/input_img46.jpg', './cnn_sample/donkkaseu/input_img47.jpg', './cnn_sample/donkkaseu/input_img48.jpg', './cnn_sample/donkkaseu/input_img49.jpg', './cnn_sample/donkkaseu/input_img50.jpg', './cnn_sample/donkkaseu/input_img51.jpg', './cnn_sample/donkkaseu/input_img52.jpg', './cnn_sample/donkkaseu/input_img53.jpg', './cnn_sample/donkkaseu/input_img54.jpg', './cnn_sample/donkkaseu/input_img55.jpg', './cnn_sample/donkkaseu/input_img56.jpg', './cnn_sample/donkkaseu/input_img57.jpg', './cnn_sample/donkkaseu/input_img58.jpg', './cnn_sample/donkkaseu/input_img59.jpg', './cnn_sample/donkkaseu/input_img60.jpg', './cnn_sample/donkkaseu/input_img61.jpg', './cnn_sample/donkkaseu/input_img62.jpg', './cnn_sample/donkkaseu/input_img63.jpg', './cnn_sample/donkkaseu/input_img64.jpg', './cnn_sample/donkkaseu/input_img65.jpg', './cnn_sample/donkkaseu/input_img66.jpg', './cnn_sample/donkkaseu/input_img67.jpg', './cnn_sample/donkkaseu/input_img68.jpg', './cnn_sample/donkkaseu/input_img69.jpg', './cnn_sample/donkkaseu/input_img70.jpg', './cnn_sample/donkkaseu/input_img71.jpg', './cnn_sample/donkkaseu/input_img72.jpg', './cnn_sample/donkkaseu/input_img73.jpg', './cnn_sample/donkkaseu/input_img74.jpg', './cnn_sample/donkkaseu/input_img75.jpg', './cnn_sample/donkkaseu/input_img76.jpg', './cnn_sample/donkkaseu/input_img77.jpg', './cnn_sample/donkkaseu/input_img78.jpg', './cnn_sample/donkkaseu/input_img79.jpg', './cnn_sample/donkkaseu/input_img80.jpg', './cnn_sample/donkkaseu/input_img81.jpg', './cnn_sample/donkkaseu/input_img82.jpg', './cnn_sample/donkkaseu/input_img83.jpg', './cnn_sample/donkkaseu/input_img84.jpg', './cnn_sample/donkkaseu/input_img85.jpg', './cnn_sample/donkkaseu/input_img86.jpg', './cnn_sample/donkkaseu/input_img87.jpg', './cnn_sample/donkkaseu/input_img88.jpg', './cnn_sample/donkkaseu/input_img89.jpg', './cnn_sample/donkkaseu/input_img90.jpg', './cnn_sample/donkkaseu/input_img91.jpg', './cnn_sample/donkkaseu/input_img92.jpg', './cnn_sample/donkkaseu/input_img93.jpg', './cnn_sample/donkkaseu/input_img94.jpg', './cnn_sample/donkkaseu/input_img95.jpg', './cnn_sample/donkkaseu/input_img96.jpg', './cnn_sample/donkkaseu/input_img97.jpg', './cnn_sample/donkkaseu/input_img98.jpg', './cnn_sample/donkkaseu/input_img99.jpg', './cnn_sample/donkkaseu/input_img100.jpg', './cnn_sample/donkkaseu/input_img101.jpg', './cnn_sample/donkkaseu/input_img102.jpg', './cnn_sample/donkkaseu/input_img103.jpg', './cnn_sample/donkkaseu/input_img104.jpg', './cnn_sample/donkkaseu/input_img105.jpg', './cnn_sample/donkkaseu/input_img106.jpg', './cnn_sample/donkkaseu/input_img107.jpg', './cnn_sample/donkkaseu/input_img108.jpg', './cnn_sample/donkkaseu/input_img109.jpg', './cnn_sample/donkkaseu/input_img110.jpg', './cnn_sample/donkkaseu/input_img111.jpg', './cnn_sample/donkkaseu/input_img112.jpg', './cnn_sample/donkkaseu/input_img113.jpg', './cnn_sample/donkkaseu/input_img114.jpg', './cnn_sample/donkkaseu/input_img115.jpg', './cnn_sample/donkkaseu/input_img116.jpg', './cnn_sample/donkkaseu/input_img117.jpg', './cnn_sample/donkkaseu/input_img118.jpg', './cnn_sample/donkkaseu/input_img119.jpg', './cnn_sample/donkkaseu/input_img120.jpg', './cnn_sample/donkkaseu/input_img121.jpg', './cnn_sample/donkkaseu/input_img122.jpg', './cnn_sample/donkkaseu/input_img123.jpg', './cnn_sample/donkkaseu/input_img124.jpg', './cnn_sample/donkkaseu/input_img125.jpg', './cnn_sample/donkkaseu/input_img126.jpg', './cnn_sample/donkkaseu/input_img127.jpg', './cnn_sample/donkkaseu/input_img128.jpg', './cnn_sample/donkkaseu/input_img129.jpg', './cnn_sample/donkkaseu/input_img130.jpg', './cnn_sample/donkkaseu/input_img131.jpg', './cnn_sample/donkkaseu/input_img132.jpg', './cnn_sample/donkkaseu/input_img133.jpg', './cnn_sample/donkkaseu/input_img134.jpg', './cnn_sample/donkkaseu/input_img135.jpg', './cnn_sample/donkkaseu/input_img136.jpg', './cnn_sample/donkkaseu/input_img137.jpg', './cnn_sample/donkkaseu/input_img138.jpg', './cnn_sample/donkkaseu/input_img139.jpg', './cnn_sample/donkkaseu/input_img140.jpg', './cnn_sample/donkkaseu/input_img141.jpg', './cnn_sample/donkkaseu/input_img142.jpg', './cnn_sample/donkkaseu/input_img143.jpg', './cnn_sample/donkkaseu/input_img144.jpg', './cnn_sample/donkkaseu/input_img145.jpg', './cnn_sample/donkkaseu/input_img146.jpg', './cnn_sample/donkkaseu/input_img147.jpg', './cnn_sample/donkkaseu/input_img148.jpg', './cnn_sample/donkkaseu/input_img149.jpg', './cnn_sample/donkkaseu/input_img150.jpg', './cnn_sample/donkkaseu/input_img151.jpg', './cnn_sample/donkkaseu/input_img152.jpg', './cnn_sample/donkkaseu/input_img153.jpg', './cnn_sample/donkkaseu/input_img154.jpg', './cnn_sample/donkkaseu/input_img155.jpg', './cnn_sample/donkkaseu/input_img156.jpg', './cnn_sample/donkkaseu/input_img157.jpg', './cnn_sample/donkkaseu/input_img158.jpg', './cnn_sample/donkkaseu/input_img159.jpg', './cnn_sample/donkkaseu/input_img160.jpg', './cnn_sample/donkkaseu/input_img161.jpg', './cnn_sample/donkkaseu/input_img162.jpg', './cnn_sample/donkkaseu/input_img163.jpg', './cnn_sample/donkkaseu/input_img164.jpg']
  # 2. target이미지 및 비교 이미지 다운로드 

target_image_url = url_path[0]
input_image_urls = url_path[1:]

# target_img_path = './cnn_sample/' + en_name + '/' + 'target_img.jpg'
# # urllib.error.URLError : url에서 다운받을때 해당 에러가능성있음
# wget.download(target_image_url,target_img_path)
# input_img_paths = []
# for i, url in enumerate(input_image_urls):
#   if len(url) > 0:
#     input_path = './cnn_sample/' + en_name + '/' + "input_img%d.jpg" % i
#     print(input_path)
#     try:
#       wget.download(url,input_path)
#       input_img_paths.append(input_path)
#     except:
#       print("url error")

###########################
target_img_path = url_path[0]
input_img_paths = url_path[1:]
############################
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
# tf.logging.set_verbosity(tf.compat.v1.logging.ERROR)
print([target_img_path] + input_img_paths)
  # Load bytes of image files
image_bytes = [tf.io.gfile.GFile(name, 'rb').read() for name in ([target_img_path] + input_img_paths)]
hub_module_url = "https://tfhub.dev/google/imagenet/mobilenet_v2_100_96/feature_vector/1"

with tf.Graph().as_default():
  input_byte, similarity_op = build_graph(hub_module_url, target_img_path)
  print("<==input_byte, similarity_op ==>" , input_byte, similarity_op)

  with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    t0 = time.time() # for time check
    
    # Inference similarities
    similarities = sess.run(similarity_op, feed_dict={input_byte: image_bytes})
    print("%d images inference time: %.2f s" % (len(similarities), time.time() - t0))

  # Display results
  print("# Target image")
  display(Image(target_img_path))
  print("- similarity: %.2f" % similarities[0])

  print("# Input images")
  cnt1 = cnt2 = 0
  cnt1_lst = []
  cnt2_lst = []
  for similarity, input_img_path in zip(similarities[1:], input_img_paths):
    display(Image(input_img_path))
    print(input_img_path,"의 유사도는 ","- similarity: %.2f" % similarity)
    if similarity >= 0.3:
      cnt1 +=1
      cnt1_lst.append(input_img_path)
      # shutil.move(input_img_path,'./upper/'+input_img_path)
    else:
      cnt2 +=1
      cnt2_lst.append(input_img_path)
      # shutil.move(input_img_path,'./under/'+input_img_path)
  print(cnt1, cnt2)




