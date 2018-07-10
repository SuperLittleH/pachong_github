from urllib import request


def load_data():
    # 1.url
    url = 'https://www.baidu.com/'
    # 2.请求头
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",}
    # 3.请求体因为urllib自身urlopen无法携带请求头借助Request
    request_user = request.Request(url,headers=headers)
    request_user.add_header('Connection','456')
    # 4.发起请求
    response = request.urlopen(request_user)
    # 获取请求头
    request_user_header =  request_user.get_header('Connection')
    print(request_user_header)

if __name__ == '__main__':
    load_data()