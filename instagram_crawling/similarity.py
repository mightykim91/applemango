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
    image = tf.image.resize_bilinear(
    image, [height, width], align_corners=False)
    image = tf.squeeze(image, squeeze_dims=[0])
    image = tf.cast(image, dtype=tf.uint8)
    return image

  def to_img_feature(images):
    """Extract the feature of image vectors"""
    outputs = module(dict(images=images), signature="image_feature_vector", as_dict=True)
    return outputs['default']

  # Step 2) Extract image features of the target image.
  target_image_bytes = tf.gfile.GFile(target_image_path, 'rb').read()
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


from os import listdir
from os.path import isfile, join
# 테스트 이미지 불러오기
mypath='./cnn_sample/'
path = './data/haarcascades'

onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f))]


en_search  = ["jjamppong"]

if name in en_search:
  
# 2. target이미지 및 비교 이미지 다운로드 
target_image_url = "https://lh3.googleusercontent.com/proxy/m_CBVQEolvfQpaJ-lKHJTPXTtVwWcbOJAu9KbfhquQam94o_GX64bk2f6z5ys13vfN2ZyT3Uo3NvAPg"
# input_image_urls = src_list[1:]
target_img_paths = './image/' + 'target_img.jpg'

input_image_urls = ['https://th.bing.com/th/id/OIP.U2l_4nf9gWtnXu3JRehOSAAAAA?w=150&h=125&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.9-k6ZI-_ICpRSgxD9XFNAgHaEK?w=311&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.tYB9aByZIfgGJ5VIynT3mAHaE7?w=248&h=184&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.Gc24VZo4XIF6nrbmB4zwSwHaE8?w=284&h=190&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.nxLFt12cOROQNQSfYCxcNgHaFm?w=248&h=188&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.ZVB3s66-S3eiU5Q_97AULwHaJ4?w=131&h=180&c=7&o=5&dpr=1.25&pid=1.7',
'https://th.bing.com/th/id/OIP.apBG0fCRuUKhpEgfCopRMwHaFj?w=230&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.Nb8gJ3QWGcXCjIPSrAbX3AHaEK?w=283&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.3L7_FpOS_Xa4gVLduCDwxAHaFe?w=255&h=187&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.BFfr6yfbYILPjhZTJ0tukwHaEK?w=318&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.nHxq4CYJx2sFzeEoM99A5gHaFj?w=234&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.GtLVgBUd47l79YGV6meJkgHaE2?w=289&h=190&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.KHZ1ijSImXdjRyle87bAkQHaE9?w=242&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.grqA1FO5nNHJXkJVOSkBbwHaHa?w=190&h=190&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.LO_phkPdZb7LzMaOfpR9DQHaE8?w=273&h=182&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.kU2P0qZp98IWiB6SCViD5wHaIX?w=168&h=189&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.ScurCc8OwG38a3x2afR_jgHaEK?w=307&h=180&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.UC3fTKd5_b_Plmb8AtrxRwHaFj?w=232&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.2HuRpMC08XvLWqUwqhQM_wHaE5?w=277&h=183&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.iDdFyCrzZd3Z7NzRWH8igQHaE7?w=267&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.ya1RIGiy2Df7Gdtm1IRWpgHaEK?w=267&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.qGjewxHxqtjADqNNF6BJ3gHaJ3?w=129&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.v7ACNrGNroXNygfzEP6hWQHaFW?w=254&h=183&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.KHZ1ijSImXdjRyle87bAkQHaE9?w=274&h=183&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.XbX8p-Owkd2FdfLEofGDlwHaEw?w=283&h=182&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.Vv_pSi6QliwIjljuJJziRQHaJQ?w=123&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.vYfK5QULW6aKMRd2bKGtPgHaFk?w=229&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.19X2acawDBn6e_csT90u0gHaE8?w=277&h=185&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.uTwp__8i1mbo4-n0DGKJCAHaE8?w=226&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.19X2acawDBn6e_csT90u0gHaE8?w=256&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.D0ZUZ-LpLzfyk-yOTUsESQHaFr?w=234&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.uYU1MHcZkQZ2us1kRQQ9cwHaFw?w=239&h=185&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.6MJ73wahXrXVptr-Rss_mgHaE8?w=260&h=180&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.p-zquANvIm9x8sOX8R7o6AHaFI?w=246&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.NXi_HhKZN9fuvCm8gN8qhAHaHa?w=183&h=184&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.lHkdTlCttYZ-rPn1p4ZgvwHaHa?w=203&h=187&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.A6_-NKsuQyeD3lSJYMu_EgHaEK?w=309&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.cA8OV5OWUo2RneOqpRaHkwHaGQ?w=207&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.R5uW6htypZvM_gLsxI8eKQHaHJ?w=178&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.u-JJwkNXtsuyHlPisma-OwHaJQ?w=142&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.sm0hVfPvE6qfQit1ygAYtwHaFj?w=250&h=188&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.O82JeQ65jB7osllHf41VXQHaJ4?w=119&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.ya1RIGiy2Df7Gdtm1IRWpgHaEK?w=272&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.rquOoPYEjDOBM9UO3l9laQHaHa?w=183&h=183&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.n6a7gsU6zLqQkZO9yOUgjwHaF8?w=201&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.EDqG0P8yyNIdr9va-EP2SAHaEK?w=302&h=185&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.lpOSn-utp2dc2q3lqUYmUgHaE8?w=225&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.SIT_qy-m1mpHJpmW2Usc1QHaE9?w=268&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.3bggAj7zkDYUprGbC8EhVwHaFO?w=218&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.NzlxpgoKygVk0XsOTaxSVwHaEu?w=270&h=184&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.oKlP2Z7xCwR6OIvaqTageAHaHa?w=188&h=189&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.kUFBbO8E3yxC6RA8r7jbzAHaE7?w=228&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.mPRYmiVdaRPnK8eyHeWpVQHaEK?w=305&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.Et-o8oEXuExK6YA0_FEp-AHaHa?w=190&h=187&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.k2tZctPX3xAEu4F6jHfxKQHaEK?w=268&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.-gH-N4YpcUyjbjckGVQmpgHaFj?w=238&h=180&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.RWfUET09P-hrhAuvN2qRAgHaEK?w=310&h=180&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.EDqG0P8yyNIdr9va-EP2SAHaEK?w=319&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.Uhy0rtIZhJPMdr0AiTlNDAHaE7?w=268&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.H3auk0HNvah92UgQPUdP9QHaEK?w=317&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.yjJMzBq8vXkEA7LeEfAXLQHaE8?w=281&h=188&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.TPDNC-ScAhOK_BVtJb4-ywHaE7?w=228&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.-8lfMEblIaxYWGLVcdN1CQHaFj?w=229&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.bVmYDGuf5SV1iOATygcv1AHaEK?w=276&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.2xKMkHznjaLDaMh9-78E1gHaEK?w=303&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.xjqWJSvv4RgU63VUE5BXiAHaHa?w=171&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.uYU1MHcZkQZ2us1kRQQ9cwHaFw?w=221&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.RghmeXaFuWuRQ3_s-bh2AwHaE8?w=278&h=185&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.TqT_CdU-Ehl_7efmjgN7mAHaFj?w=238&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.ycABL781xYy3LuwJSXkO1wHaE7?w=258&h=184&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.Gc24VZo4XIF6nrbmB4zwSwHaE8?w=282&h=188&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.ld5LE789HqCA0GXtOD2uFgHaE7?w=275&h=184&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.aswtE6EHqBmQhpPyidWIWAHaEK?w=313&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.QUgIVOUusddRamLT0bqpGwHaEK?w=312&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.k4aPxPnf5cnnTuF1Uk5PiQHaE8?w=275&h=184&c=7&o=5&dpr=1.25&pid=1.7',
'https://th.bing.com/th/id/OIP.M9MXF2MmDpkrH-FBsjPBkQHaFj?w=232&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.HckJgsegtEDHmA7Pmnk0bgHaE7?w=276&h=183&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.D6jdJ__BVDg-yMifsbKjKQHaFj?w=239&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.eozxhhGk7d5UN8faLA0UrgHaEK?w=294&h=184&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.Fn9cl679okfKy3kj-mZjFAHaFj?w=220&h=184&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.H5r_cVlg0OT1zA_Hoe6i6gHaHa?w=181&h=182&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.8JPkW1Cd0K1Sv4k4s9tA9gHaFj?w=229&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.iDdFyCrzZd3Z7NzRWH8igQHaE7?w=231&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.0OasucLd40kl3gL1AZmHcwHaFj?w=204&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.KGhDVS-ruYG4SEsa7C0NaAHaE8?w=267&h=180&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.tYB9aByZIfgGJ5VIynT3mAHaE7?w=227&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.mPRYmiVdaRPnK8eyHeWpVQHaEK?w=324&h=182&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.wPUtUpNW2RHO8G5Z2pV38QHaE7?w=276&h=184&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.dK3Ooqc7ihqA0xxE3twiIQAAAA?w=298&h=190&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.sI7FAv-f8K1HKMcadqZ9hwHaJK?w=139&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.Nb8gJ3QWGcXCjIPSrAbX3AHaEK?w=276&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.4oHoaGrLQH14AXSpY2PxqgHaHa?w=165&h=184&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.s2TSPcXan1LT4Z1Hw4XATAHaE8?w=274&h=183&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.5-L6_9SBaoPW8xK_GmjPHwHaEK?w=303&h=180&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.SHasSNfhLlpciRuW4uB37QHaE0?w=280&h=183&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.nHxq4CYJx2sFzeEoM99A5gHaFj?w=204&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.jJIPZ74R3-Al2dauve1UuAHaE8?w=278&h=185&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.ScurCc8OwG38a3x2afR_jgHaEK?w=333&h=187&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.hdNowcgLprDF8aoTQUkPbQHaFj?w=227&h=180&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.g28lA_aXQ-zq7aNu6FZvcQHaFj?w=244&h=183&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.A7e4-BpIc_Bb0H5MUBwDsQHaEK?w=306&h=180&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.YBhCLL_vGzohJTGeLtSjrQHaG_?w=169&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.s2TSPcXan1LT4Z1Hw4XATAHaE8?w=280&h=187&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.4y9bwm9sKgPXUQj4W99ABAHaE8?w=260&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.p-zquANvIm9x8sOX8R7o6AHaFI?w=267&h=185&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.sba9vyinNLhBp31bE1UZaQAAAA?w=122&h=184&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.M9MXF2MmDpkrH-FBsjPBkQHaFj?w=204&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.36zcW3AEa8wByYy7HWb2GgHaE9?w=255&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.63zo_ZRnHIZ9eZO_-dg5dwHaEL?w=324&h=183&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.wqlnvkdMegIJGrLZHs50iQHaFH?w=259&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.JPQ15Wc24pGK-gQS1CuUIAHaE5?w=257&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.CfJF72JicqTd3MLr3ssd3wHaLI?w=125&h=189&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.XyXlC-SsxvMspLpg6SoehwHaID?w=149&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.Ev8Q6BLRim9x-h5PoLWnmgHaFj?w=265&h=187&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.7D3qTVLKHd0SlnOXKnbixgHaE5?w=228&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.wqlnvkdMegIJGrLZHs50iQHaFH?w=254&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.8xFMJIqC1zsi22XOdKccUwHaFj?w=202&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.8xFMJIqC1zsi22XOdKccUwHaFj?w=230&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.3xepd-PgB7ub_i9eLNE5XgHaHE?w=182&h=180&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.36zcW3AEa8wByYy7HWb2GgHaE9?w=241&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.SIT_qy-m1mpHJpmW2Usc1QHaE9?w=261&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.wO646o8ehujPIDht-npOMAHaLJ?w=115&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.kVEMHKk_a5uU1E_oytn1FgHaFG?w=266&h=183&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.ZVB3s66-S3eiU5Q_97AULwHaJ4?w=134&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.vGWkF0YfRF8ARCQVPgFdhAHaE7?w=285&h=189&c=7&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.rqOrHKHlcrEXrf4OKvVvCwHaFj?w=226&h=185&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.ZzrrToi9pxI9w7sDDqxo5gHaFj?w=229&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.BLTleP2BeE21n13voSLyUwHaEK?w=318&h=180&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.sI7FAv-f8K1HKMcadqZ9hwHaJK?w=122&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.QUgIVOUusddRamLT0bqpGwHaEK?w=273&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.63zo_ZRnHIZ9eZO_-dg5dwHaEL?w=275&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.rjxAIFbZfxnZBE5jLenBqgHaGF?w=244&h=187&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.NzlxpgoKygVk0XsOTaxSVwHaEu?w=287&h=183&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.EvDebt-cgA0_7bC9QfvBWgAAAA?w=177&h=159&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.3L7_FpOS_Xa4gVLduCDwxAHaFe?w=229&h=180&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.SqQaEjlSRSpMOuZ1i-Mf1gHaEK?w=311&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.iOk3vpkEY7iHEgwymSsXHwHaEK?w=333&h=187&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.2kslJhFhgeG_7ueHuV5QMgHaE9?w=238&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.3bggAj7zkDYUprGbC8EhVwHaFO?w=244&h=180&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.kPoAOzmmZcVhONM4I9sLCAHaFj?w=237&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.dfSolydCWmTzgqwy-wWEUAHaFj?w=234&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.6MJ73wahXrXVptr-Rss_mgHaE8?w=257&h=184&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.p98tRLkgFAsEl67QEg2grgHaE7?w=234&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.EtKyKKAbBbb0ebfE6HfCrQHaFj?w=240&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.AQV_7fc4wpC7NgTDsYP7dgHaE8?w=257&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.EtKyKKAbBbb0ebfE6HfCrQHaFj?w=238&h=180&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.-25EgkEnuGTa-AmbUETx8wHaEL?w=302&h=180&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.OjP-8sHVtnVYoRbjv_-bPgAAAA?w=139&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.1scoDfAYG_JCwgprCxsdvgHaFj?w=238&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.1IXulYbW3_tH7q1a0-RxCQHaF0?w=191&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.vhIJwouw-XIFEay0QNL1pgHaFj?w=244&h=183&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.cA8OV5OWUo2RneOqpRaHkwHaGQ?w=204&h=180&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.TPDNC-ScAhOK_BVtJb4-ywHaE7?w=255&h=185&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.zJeOAjHbu_V-g1H2n9uMwQHaD7?w=335&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.BFfr6yfbYILPjhZTJ0tukwHaEK?w=328&h=184&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.OjP-8sHVtnVYoRbjv_-bPgAAAA?w=141&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.uTwp__8i1mbo4-n0DGKJCAHaE8?w=260&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.kUFBbO8E3yxC6RA8r7jbzAHaE7?w=240&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.dfSolydCWmTzgqwy-wWEUAHaFj?w=216&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.Ctd1yhnWXaJ3lM0S2pvSLwHaHa?w=179&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.IioSAhZT22X65ycJebR-5AHaJh?w=137&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.6LiYMeXrnbwmIhZOaKm00AHaE7?w=228&h=180&c=7&o=5&dpr=1.25&pid=1.7', 'https://th.bing.com/th/id/OIP.OrUnk8WXzJ651Yxg3s_yugHaEK?w=309&h=180&c=7&o=5&pid=1.7', 'https://th.bing.com/th/id/OIP.D6jdJ__BVDg-yMifsbKjKQHaFj?w=234&h=180&c=7&o=5&dpr=1.25&pid=1.7']

# urllib.error.URLError : url에서 다운받을때 해당 에러가능성있음
# wget -q {target_image_url} -O {target_img_path}

wget.download(target_image_url,target_img_paths)

for i, url in enumerate(input_image_urls):
  if len(url) > 0:
    input_path = './image/' + "input_img%d.jpg" % i
    try:
      wget.download(url,input_path)
      input_img_paths.append(input_path)
    except:
      print("url error")

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
# tf.logging.set_verbosity(tf.compat.v1.logging.ERROR)

for target_img_path in target_img_paths:
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




