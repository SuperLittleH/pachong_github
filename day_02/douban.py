import requests
import json


class Douban_Spider(object):
    def __init__(self):
        # url 查找到的url
        self.start_url = 'https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_domestic_hot/items?os=android&for_mobile=1&start={}&count=18&loc_id=108288&_=1531185255668'
        # 请求头 分为User-Agent和Referer字段
        self.headers = {
            'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1',
            'Referer':'https://m.douban.com/tv/chinese'
        }


    def send_data(self,url):
        # 发送请求
        data = requests.get(url, headers=self.headers).content.decode()
        return data

    # 提取数据
    def get_json(self,data):
        data_dict = json.loads(data)
        # 提取值
        content_list = data_dict['subject_collection_items']
        total = data_dict['total']
        return content_list,total

    # 保存数据
    def sava_data(self,content_list):
        with open('01.json','a',encoding='utf-8')as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n")
        print('保存成功')

    def run(self):
        num = 0
        total = 100
        while num < total+18:
            url = self.start_url.format(num)
            print(url)
            # 1.发送数据
            data = self.send_data(url)
            # 2.提取数据
            content_list,total = self.get_json(data)
            # 3.保存数据
            self.sava_data(content_list)
            num += 18

if __name__ == '__main__':
    douban = Douban_Spider()
    douban.run()