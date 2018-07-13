import requests
import random
import json
from bs4 import BeautifulSoup


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
            data = requests.get(self.base_url,headers=self.headers,proxies=self.proxies,params=params).content.decode()
            return data
        except Exception as e:
            print(e)

    # 2.解析数据
    def analysis(self,data):
        # 1.转成解析类型
        html_data = BeautifulSoup(data,'lxml')
        # 2.解析数据
        tr_list = html_data.select('.even,.odd')
        print(tr_list)
        # 3.遍历每个tr取出text()
        for tr in tr_list:
            tr_dict = {}
            tr_dict['work_position'] = tr.select('td a')[0].get_text()
            tr_dict['work_type'] = tr.select('td')[1].get_text()
            tr_dict['work_count'] = tr.select('td')[2].get_text()
            tr_dict['work_city'] = tr.select('td')[3].get_text()
            tr_dict['work_time'] = tr.select('td')[4].get_text()
            self.data_list.append(tr_dict)

    # 3.保存数据
    def sava_data(self):
        json.dump(self.data_list,open('05_bs4.json','w'))
        print('保存完成')

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

        # 2.解析数据
        self.analysis(data)

        # 3.保存数据
        self.sava_data()



if __name__ == '__main__':
    Tencent_data().run()