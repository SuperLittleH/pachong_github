import requests


def load_360_image():
    # 1.url
    url = 'https://p.ssl.qhimg.com/t01d1f1a2ae31e3c3e4.png'
    # 请求头
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    # 2.发起请求
    response = requests.get(url,headers=headers)
    # 获取数据
    data = response.content

    # 写入文件
    with open('01_imge.png','wb')as f:
        f.write(data)
        print('图片保存完成!')

if __name__ == '__main__':
    load_360_image()