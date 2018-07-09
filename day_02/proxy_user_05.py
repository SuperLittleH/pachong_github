import requests

def load_data():
    # 1.url
    url = 'http://www.baidu.com'
    # 2.请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    }
    # 3.参数代理模式
    proxy = {
        'Https':'139.129.99.9:3128'
    }
    # 4.发起请求
    data = requests.get(url, headers=headers, proxies=proxy,timeout=3).content.decode()
    print(data)

if __name__ == '__main__':
    load_data()