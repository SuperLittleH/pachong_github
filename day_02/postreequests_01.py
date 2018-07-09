import requests


def fanyi_baidu():
    # 1.url
    url = 'http://fanyi.baidu.com/basetrans'
    # 2.请求头
    headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Mobile Safari/537.36'}
    # 3.参数 因为是有请求体 所有时post data
    data = {
        'query':'人民币',
        'from':'zh',
        'to':'en'
    }
    # 4.发起请求
    data = requests.post(url,headers=headers,data=data).content.decode()
    print(data)

if __name__ == '__main__':
    fanyi_baidu()