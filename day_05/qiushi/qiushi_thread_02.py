import random
import threading
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
        # 记录个数
        self.count = 0
        # url队列
        self.url_queue = Queue()
        # 响应队列
        self.response_queue = Queue()
        # 数据队列
        self.data_queue = Queue()

    def get_request_url(self):
        # return [self.base_url.format(i) for i in range(1,14)]
        for i in range(1,14):
            self.url_queue.put(self.base_url.format(i))

    def send_data(self):
        while True:
            url = self.url_queue.get()
            # 1.发送请求
            time.sleep(2)
            response = requests.get(url, headers=self.headers, proxies=self.proxies)
            print(response.url)
            if response.status_code == 200:
                # 入队列
                self.response_queue.put(response)
            else:
                self.url_queue.put(url)

            # 计数器减1
            self.url_queue.task_done()


    # 2.解析数据
    def analysis_data(self):
        while True:
            data = self.response_queue.get().content.decode()
            html_data = etree.HTML(data)
            div_list = html_data.xpath('//div[@id="content-left"]/div')
            print('解析的个数是:', len(div_list))
            for div in div_list:
                nick_name = div.xpath('.//h2/text()')[0]
                self.data_queue.put(nick_name)
            # 计数器减一
            self.response_queue.task_done()

    # 3.保存数据
    def save_data(self):
        while True:
            # 从数据队列获取数据
            data = self.data_queue.get()
            print(data.strip())
            if data:
                with open('01_qiushi_02.txt','a')as f:
                    f.write(data)
            print('数据写入完成')
            self.count += 1
            self.data_queue.task_done()
    # 调度任务
    def start_work(self):
        t_list = []
        # 1.url线程
        t_url = threading.Thread(target=self.get_request_url)
        t_list.append(t_url)

        # 1. request 线程
        for i in range(3):
            t_request = threading.Thread(target=self.send_data)
            t_list.append(t_request)

        # 1. 解析数据
        t_nanalysis = threading.Thread(target=self.analysis_data)
        t_list.append(t_nanalysis)

        # 1. save
        t_save = threading.Thread(target=self.save_data)
        t_list.append(t_save)

        # 线程守护 开启线程
        for t in t_list:
            t.setDaemon(True)
            t.start()

        # 主线程守护
        for q in [self.url_queue, self.response_queue, self.data_queue]:
            q.join()



    # 5.执行
    def run(self):
        start_time = time.time()

        self.start_work()

        end_time = time.time()

        print('总个数:',self.count)
        print('总耗时:',end_time - start_time)

if __name__ == '__main__':
    QiuShiSpider().run()