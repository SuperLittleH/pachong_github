import requests


def load_data():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    }
    url = 'http://www.baidu.com'
    response = requests.get(url,headers=headers)
    data = response.content.decode()
    request_cookie = response.request._cookies
    cookie_dict = requests.utils.dict_from_cookiejar(request_cookie)
    print(cookie_dict)

if __name__ == '__main__':
    load_data()
