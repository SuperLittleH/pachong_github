import random
from multiprocessing.dummy import Pool
from queue import Queue
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
        # 线程池
        self.pool = Pool(5)
        # 请求数
        self.request_num = 0
        # 响应数
        self.response_num = 0
        # url队列
        self.url_queue = Queue()
        # 判断是否递归
        self.running = True

    def get_request_url(self):
        # return [self.base_url.format(i) for i in range(1,14)]
        for i in range(1,14):
            self.url_queue.put(self.base_url.format(i))
            self.request_num += 1

    def send_data(self,url):
        # 1.发送请求
        time.sleep(2)
        response = requests.get(url, headers=self.headers, proxies=self.proxies)
        data = response.content.decode()
        self.response_num += 1
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
    def save_data(self,nick_name):
        if nick_name:
            with open('04_qiushi.txt','a')as f:
                f.write(nick_name)
        print('数据写入完成')

    # 调度任务
    def start_work(self):
        # 获取url
        url = self.url_queue.get()

        # 1.发送请求
        data = self.send_data(url)
        # 2.解析数据
        nick_name = self.analysis_data(data)
        # 3.保存数据
        self.save_data(nick_name)

        # 计数器减一
        self.url_queue.task_done()

    def _callback(self,item):
        if self.running:
            self.pool.apply_async(self.start_work, callback=self._callback)

    # 5.执行
    def run(self):
        start_time = time.time()

        # 1.操作url
        self.get_request_url()

        # 2.执行异步线程任务
        for i in range(3):
            self.pool.apply_async(self.start_work, callback=self._callback)


        # 阻赛主线程
        while True:
            # 防止cpu空转
            time.sleep(0.00001)
            if self.response_num >= self.request_num:
                self.running = False
                break

        end_time = time.time()

        print('总个数:',self.count)
        print('总耗时:',end_time - start_time)

if __name__ == '__main__':
    QiuShiSpider().run()