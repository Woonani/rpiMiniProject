import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def game_data(key, photoURL1, photoURL2, photoURL3, photoURL4, winlose):

    url = (os.getenv("api"))+"/profile"
    
    headers = {
        "Content-Type": "application/json"
    }

    temp = {
        "key" : key,
        "photoURL1" : photoURL1,
        "photoURL2" : photoURL2,
        "photoURL3" : photoURL3,
        "photoURL4" : photoURL4,
        "winlose" : winlose,
    }
    data = json.dumps(temp)

    response = requests.post(url, headers=headers, data=data)
    print("response:", response)

game_data("1234", "no-image.jpg", "no-image.jpg", "no-image.jpg", "no-image.jpg", False)

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