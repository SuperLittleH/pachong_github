import random
import requests



class QiuShiSpider(object):
    def __init__(self):
        self.base_url = 'https://www.qiushibaike.com/8hr/page/{}'
        self.headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        proxies = proxies = [{'Https': '139.208.194.21:8118'}, {'Https': '49.79.156.83:8000'},{'Htpps': '60.255.186.169:8888'}, {'Htpps': '115.46.73.162:8123'},{'Https': '60.176.239.194:6666'}]
        self.proxies = random.choice(proxies)

    def get_request_url(self):
        return [self.base_url.format(i) for i in range(1,2)]

    def send_data(self,url):
        # 1.发送请求
        response = requests.get(url, headers=self.headers, proxies=self.proxies)
        data = response.content.decode()
        print(self.proxies)
        return data

    # 2.解析数据
    def analysis_data(self,data):
        pass

    # 3.保存数据
    def save_data(self,data):
        with open('01_qiushi.html','w')as f:
            f.write(data)
            print('数据写入完成')

    # 4.执行
    def run(self):
        # 获取url
        url_list = self.get_request_url()
        for url in url_list:
            # 1.发送请求
            data = self.send_data(url)
            # 2.保存数据
            self.save_data(data)

if __name__ == '__main__':
    QiuShiSpider().run()