import requests


def load_data():
    # 1.url
    url = 'http://www.12306.cn/mormhweb/'
    # 2.请求头
    headers = headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",}
    # 3.发起请求
    data = requests.get(url, headers=headers, verify=False).content.decode()
    print(data)

if __name__ == '__main__':
    load_data()