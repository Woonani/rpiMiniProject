from requests_toolbelt import MultipartEncoder
import requests
import json
import os
from dotenv import load_dotenv

def game_data(key, winlose):

    load_dotenv()

    url = (os.getenv("api"))+"/profile"
    
    payload = MultipartEncoder(
        fields={'key': key,
                'img0' : ('pic0.jpg', open('data/pic0.jpg', 'rb'), 'text/plain'),
                'img1' : ('pic1.jpg', open('data/pic1.jpg', 'rb'), 'text/plain'),
                'img2' : ('pic1.jpg', open('data/pic1.jpg', 'rb'), 'text/plain'),
                'img3' : ('pic2.jpg', open('data/pic2.jpg', 'rb'), 'text/plain'),
                'winlose' : winlose
                }
    )

    requests.post(url, data = payload, headers = {'Content-Type': payload.content_type})
    
# game_data("1234", "1")


#     files = [ 
#         ('img', open('data/pic0.jpg', 'rb')),
#         ('img', open('data/pic1.jpg', 'rb')),
#         # ('img', open('data/pic0.jpg', 'rb')),
#     ]

#     headers = {
#     'accept': 'application/json',
#     'Content-Type': 'multipart/form-data',
# }


    # requests.post(url, data = files, headers = headers)

    # requests.post(url, files = files)

    # image = MultipartEncoder(fields=files)
    # headers = {"Content-Type": image.content_type}
    # res = requests.post(url, headers=headers, data=image)
    # return res.status_code, res.json()
    


    # response = requests.post(url, headers= headers, payload=payload)
    # print("response:", response)


# URL
# 127.0.0.1은 localhost로 대체 가능 
# url = "http://192.168.0.63:8080/profile/test"

# headers
# headers = {
    # "Content-Type": "application/json"
# }

# data
# temp = {
    # "color": "black",
    # "size": 200
# }
# 딕셔너리를 JSON으로 변환 
# data = json.dumps(temp)


# response = requests.post(url, headers=headers, data=data)

# print("response: ", response)
# print("response.text: ", response.text)