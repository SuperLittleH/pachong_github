import requests
import random
from lxml import etree
import json


class Tencent_data(object):
    def __init__(self):
        self.base_url = 'https://hr.tencent.com/position.php'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
        proxies = [{'Https':'139.208.194.21:8118'},{'Https':'49.79.156.83:8000'},{'Htpps':'60.255.186.169:8888'},{'Htpps':'115.46.73.162:8123'},{'Https':'60.176.239.194:6666'}]
        self.proxies = random.choice(proxies)
        self.data_list = []

    # 1.发送请求
    def send_request(self,params):
        try:
            response = requests.get(self.base_url,headers=self.headers,proxies=self.proxies,params=params)
            print(response.url)
            data = response.content.decode()
            return data
        except Exception as e:
            print(e)

    # 2.解析数据
    def analysis_data(self,data):
        # xpath对象
        html_data = etree.HTML(data)
        # 2.解析
        tr_data = html_data.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        # 循环取出文本数据
        for tr in tr_data:
            # 字典保存取出的数据
            data_dict = {}
            data_dict['work_position'] = tr.xpath('td/a/text()')[0]
            data_dict['work_type'] = tr.xpath('td[2]/text()')[0]
            data_dict['work_count'] = tr.xpath('td[3]/text()')[0]
            data_dict['work_city'] = tr.xpath('td[4]/text()')[0]
            data_dict['work_time'] = tr.xpath('td[5]/text()')[0]

            # 写入字典
            self.data_list.append(data_dict)

    # 3.保存数据
    def sava_data(self):
        json.dump(self.data_list,open('03_tencent_03.json','w'))
        print('保存成功')

    # 执行
    def run(self):
        for page in range(0,90,10):
            # 1.拼接参数
            params = {
                'keywords':'python',
                'tid':'0',
                'lid':'2156',
                'start':page
            }


            # 1.发送请求
            data = self.send_request(params=params)

            # 2.解析数据
            self.analysis_data(data)

            # 3.保存数据
            self.sava_data()



if __name__ == '__main__':
    Tencent_data().run()