import socket
import requests, json


def get_tuling(info):
    post_json = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": info
            },
        },
        "userInfo": {
            "apiKey": "a3294b99d9484579941b6e3165a43787",
            "userId": "chunlei"
        }
    }
    dat = json.dumps(post_json) #访问接口需要提供一个标准的json
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    response = requests.post(url, data=dat).json()
    return response['results'][0]['values']['text']

if __name__ == "__main__":
    while True:

        user_input = input('我>>>')

        response = get_tuling(user_input)
        print(response)

