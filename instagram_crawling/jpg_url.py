import base64
import requests
url = "https://img.hankyung.com/photo/202001/01.21343681.1.jpg"
urlpath = base64.b64encode(requests.get(url).content)
print(urlpath)