from urllib import request


def load_data():
    url = 'http://www.baidu.com'
    response = request.urlopen(url)
    # 读取数据
    print(response.read())

if __name__ == '__main__':
    load_data()