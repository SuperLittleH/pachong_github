import random
import requests
from lxml import etree
import json


class TencentSPider(object):
    def __init__(self):
        self.base_url = 'https://hr.tencent.com/position.php'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        proxies = [{'Https': '139.208.194.21:8118'}, {'Https': '49.79.156.83:8000'}, {'Htpps': '60.255.186.169:8888'},{'Htpps': '115.46.73.162:8123'}, {'Https': '60.176.239.194:6666'}]
        self.proxies = random.choice(proxies)
        self.data_list = []
        self.page = 0

    # 1.发送请求
    def send_request(self,params):
        try:
            response = requests.get(self.base_url, headers=self.headers, proxies=self.proxies, params=params)
            print(response.url)
            data = response.content.decode()
            return data
        except Exception as e:
            print(e)

    # 2.解析数据
    def analysis_data(self,data):
        # 1.解析数据
        html_data = etree.HTML(data)
        # 2. 解析数据 获取所有 tr 的标签对象 list
        tr_list = html_data.xpath('//tr[@class="even"] | //tr[@class="odd"]')

        # 3. 遍历每一个 tr; 取出 td 里面的内容 text()
        for tr in tr_list:
            dict_data = {}
            dict_data['work_position'] = tr.xpath('td/a/text()')[0]
            dict_data['work_type'] = tr.xpath('td[2]/text()')[0]
            dict_data['work_count'] = tr.xpath('td[3]/text()')[0]
            dict_data['work_place'] = tr.xpath('td[4]/text()')[0]
            dict_data['work_time'] = tr.xpath('td[5]/text()')[0]

            # 添加到 集合list
            self.data_list.append(dict_data)
        # 根据下一页标签如果class有值就倒头了
        next_class = html_data.xpath('//a[@id="next"]/@class')

        return next_class

    # 3.保存数据
    def write_file(self):
        json.dump(self.data_list, open('03_tencent_05.json','w'))

    # 4.执行
    def run(self):
        while True:
            params = {
                "keywords": "python",
                "lid": "2156",
                "tid": "0",
                "start": self.page
            }
            # 2.发送请求
            data = self.send_request(params=params)

            self.page += 10
            # 3.解析数据
            judge_over = self.analysis_data(data)

            # 4.如果满足条件跳出循环
            if judge_over:
                break
        # 5.保存
        self.write_file()

if __name__ == '__main__':
    TencentSPider().run()