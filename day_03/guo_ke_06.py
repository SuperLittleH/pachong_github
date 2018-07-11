import re
import requests


class GuoKeLoadData(object):
    def __init__(self):
        self.url = 'https://www.guokr.com/ask/highlight/?page=1'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
        self.pattern = re.compile('<h2><a target="_blank" href="(.*)">(.*)</a></h2>')
        self.proxies = {'Https':'122.142.232.96:8080'}

    def send_data(self):
        # 发送请求
        data = requests.get(self.url, headers=self.headers, proxies=self.proxies).content.decode()
        return data


    def sava_data(self,data):
        #保存数据
        with open('06_guoke.html','w')as f:
            f.write(data)
            print('写入成功')


    def analysis_data(self,data):
        # 解析数据
        result_data = self.pattern.findall(data)
        print(result_data)
        return result_data


    def run(self):
        # 1.发送请求
        data = self.send_data()
        # 2写入数据
        self.sava_data(data)
        # 3.解析数据
        self.analysis_data(data)

if __name__ == '__main__':
    GuoKeLoadData().run()

