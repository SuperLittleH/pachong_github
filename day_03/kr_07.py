import json
import re
import requests
import jsonpath


class Kr36(object):
    def __init__(self):
        self.url = 'http://36kr.com/'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
        self.proxies = {'Https':'122.142.232.96:8080'}
        self.pattern = re.compile('<script>var props=(.*),locationnal=')

    # 发送请求
    def send_data(self):
        data = requests.get(self.url, headers=self.headers, proxies=self.proxies).content.decode()
        return data

    # 2.解析数据
    def analysis_data(self,data):
        result_data = self.pattern.findall(data)
        return result_data


    # 3.保存数据
    def sava_data(self,result_data):
        with open('07_06kr.json','w')as f:
            f.write(result_data[0])
            print('数据写入完成')
            print(result_data[0])
            # json.loads(result_data[0])
            # print(jsonpath.jsonpath(result_data[0],'$.hotLinks|hotLinks'))


    # 执行函数
    def run(self):
        # 1.发送请求
        data = self.send_data()
        # 2.解析数据
        result_data = self.analysis_data(data)
        # 3.保存数据
        self.sava_data(result_data)

if __name__ == '__main__':
    Kr36().run()