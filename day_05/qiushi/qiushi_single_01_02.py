import random
import requests
import time
from lxml import etree


class QiuShiSpider(object):
    def __init__(self):
        self.base_url = 'https://www.qiushibaike.com/8hr/page/{}'
        self.headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        proxies = proxies = [{'Https': '139.208.194.21:8118'}, {'Https': '49.79.156.83:8000'},{'Htpps': '60.255.186.169:8888'}, {'Htpps': '115.46.73.162:8123'},{'Https': '60.176.239.194:6666'}]
        self.proxies = random.choice(proxies)
        self.count = 0


    def get_request_url(self):
        return [self.base_url.format(i) for i in range(1,14)]

    def send_data(self,url):
        # 1.发送请求
        time.sleep(2)
        response = requests.get(url, headers=self.headers, proxies=self.proxies)
        data = response.content.decode()
        print(response.url)
        print(self.proxies)
        return data

    # 2.解析数据
    def analysis_data(self,data):
        html_data = etree.HTML(data)
        div_list = html_data.xpath('//div[@id="content-left"]/div')
        print('解析的个数是:', len(div_list))
        for div in div_list:
            nick_name = div.xpath('.//h2/text()')[0]
            print(nick_name.strip())
            self.count +=1


    # 3.保存数据
    def save_data(self,nick_name,page):
        page_number = '----------第' + str(page) + '页-----------------'
        print(page_number)
        if nick_name:
            with open('01_qiushi_02.txt','a')as f:
                f.write(page_number)
                f.write(nick_name)
                print('数据写入完成')

    # 调度任务
    def start_work(self):
        # 获取url
        url_list = self.get_request_url()
        for url in url_list:
            # 1.发送请求
            data = self.send_data(url)
            # 2.解析数据
            nick_name = self.analysis_data(data)
            # 3.保存数据
            page = url_list.index(url) + 1
            self.save_data(nick_name, page)

    # 5.执行
    def run(self):
        start_time = time.time()

        self.start_work()

        end_time = time.time()

        print('总个数:',self.count)
        print('总耗时:',end_time - start_time)

if __name__ == '__main__':
    QiuShiSpider().run()