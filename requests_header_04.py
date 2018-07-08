import requests


def load_header():
    # 1.url
    url = 'https://p.ssl.qhimg.com/t01d1f1a2ae31e3c3e4.png'
    # header
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    # 3.发起请求
    response = requests.get(url,headers=headers)
    # 4.数据
    data = response.request.headers

    print(data)

if __name__ == '__main__':
    load_header()