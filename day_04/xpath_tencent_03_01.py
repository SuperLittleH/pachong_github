import requests
import random


class Tencent_data(object):
    def __init__(self):
        self.base_url = 'https://hr.tencent.com/position.php'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
        proxies = [{'Https':'139.208.194.21:8118'},{'Https':'49.79.156.83:8000'},{'Htpps':'60.255.186.169:8888'},{'Htpps':'115.46.73.162:8123'},{'Https':'60.176.239.194:6666'}]
        self.proxies = random.choice(proxies)

    # 1.发送请求
    def send_request(self,params):
        try:
            data = requests.get(self.base_url,headers=self.headers,proxies=self.proxies,params=params).content.decode()
            print(data)
            return data
        except Exception as e:
            print(e)

    # 2.解析数据


    # 3.保存数据
    def sava_data(self,data):
        with open('03_tencent.html','w')as f:
            f.write(data)
            print('保存成功')

    # 执行
    def run(self):
        # 1.拼接参数
        params = {
            'keywords':'python',
            'tid':'0',
            'lid':'2156',
            'start':'0'
        }


        # 1.发送请求
        data = self.send_request(params=params)

        # 2.保存数据
        self.sava_data(data)



if __name__ == '__main__':
    Tencent_data().run()