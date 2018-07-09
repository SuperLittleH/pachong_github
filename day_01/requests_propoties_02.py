import  requests


def load_360_data():
    # 1.url
    url = 'https://www.so.com/'
    # 2.发起请求
    response = requests.get(url)
    # 3.输出数据str
    data = response.text
    # 4.输出bytes
    data = response.content.decode()
    # 5.状态码
    code = response.status_code
    # 6.请求头
    request_headers = response.request.headers
    # 7.相应头
    response_headers = response.headers
    # 8.cookie请求
    request_cookie = response.request._cookies
    # 9.cookie响应
    response_cookie = response.cookies

    print(response_cookie)

if __name__ == '__main__':
    load_360_data()