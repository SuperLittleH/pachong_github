import requests

def load_360_data():
    # 1.url
    url = 'https://www.so.com/'
    # 2.发起请求
    response = requests.get(url)
    # 3.请求的数据
    print(response.text)

if __name__ == '__main__':
    load_360_data()