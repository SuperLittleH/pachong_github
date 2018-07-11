import requests
import re

class NeihanBaSpider(object):
    def __init__(self):
        self.url = 'https://www.neihan8.com/article/list_5_'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
        self.proxies = {'Https':'122.142.232.96:8080'}

        # 第一次解析
        self.first_pattern = re.compile('<div class="f18 mb20">(.*?)</div>',re.S)

    # 1.发送请求
    def send_request(self,url):
        data = requests.get(url,headers=self.headers,proxies=self.proxies).content.decode('gbk')
        return data

    # 2.解析
    def analysis_data(self,data):
        result_list = self.first_pattern.findall(data)
        return result_list

    # 3.保存文件
    def write_file(self,data_list):
        with open('08neihanba.txt','a')as f:
            for content in data_list:
                f.write(content)
            print('写入成功')

    def run(self):
        # 1.拼接url
        url = self.url + '1' +'.html'
        # 2.发送请求
        data = self.send_request(url)
        # 3.解析数据
        result_list = self.analysis_data(data)
        # 4.保存数据
        self.write_file(result_list)

if __name__ == '__main__':
    NeihanBaSpider().run()