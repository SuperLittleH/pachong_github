import json

import requests
from lxml import etree
import random


class TencentSpider(object):
    def __init__(self):
        self.base_url = 'https://hr.tencent.com/position.php'
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
        proxies = [{'Https': '139.208.194.21:8118'}, {'Https': '49.79.156.83:8000'}, {'Htpps': '60.255.186.169:8888'},{'Htpps': '115.46.73.162:8123'}, {'Https': '60.176.239.194:6666'}]
        self.proxies = random.choice(proxies)
        # 数据集合
        self.data_list = []

    # 1.发送请求
    def send_request(self,params):
        try:
            response = requests.get(self.base_url, headers=self.headers, proxies=self.proxies,params=params)
            data = response.content.decode()
            print(response.url)
            return data
        except Exception as e:
            print(e)

    # 2.解析数据
    def analysis_data(self,data):
        # 1.转换成解析类型
        html_data = etree.HTML(data)
        # 2.解析数据
        tr_list = html_data.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        # 循环取出td的文本数据
        for tr in tr_list:
            dict_data = {}
            dict_data['work_position'] = tr.xpath('td/a/text()')[0]
            dict_data['work_type'] = tr.xpath('td[2]/text()')[0]
            dict_data['work_count'] = tr.xpath('td[3]/text()')[0]
            dict_data['work_place'] = tr.xpath('td[4]/text()')[0]
            dict_data['work_time'] = tr.xpath('td[5]/text()')[0]

            # 添加到对应的集合中
            self.data_list.append(dict_data)

        # 4.取出最大页数
        all_number = html_data.xpath('//div[@class="pagenav"]/a/text()')[-2]
        return int(all_number)

    # 3.保存数据
    def write_file(self):
        json.dump(self.data_list, open('03_tencent2.json','w'))


    # 4先发送请求解析最大页数
    def get_all_number(self):
        # 1.拼参数
        params = {
            "keywords": "python",
            "lid": "2156",
            "tid": "0",
            "start": 0
        }
        # 2.发起请求
        data = self.send_request(params=params)

        # 3.解析数据
        all_number = self.analysis_data(data)
        return all_number

    # 5.执行
    def run(self):
        # 1.先发送请求获取最大页数
        all_number = self.get_all_number()

        # 2.根据最大页数开启循环
        for page in range(1,all_number):
            # 1.拼参数
            params = {
                "keywords": "python",
                "lid": "2156",
                "tid": "0",
                "start":page * 10
            }
            # 2.发起请求
            data = self.send_request(params=params)

            # 3.解析数据
            self.analysis_data(data)

        # 4.保存
        self.write_file()


if __name__ == '__main__':
    TencentSpider().run()