import random
import requests
from lxml import etree


class TiebaSpider(object):
    def __init__(self):
        self.base_url = 'https://tieba.baidu.com/f?kw=美食吧&pn=0'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        proxies = [{'Https': '139.208.194.21:8118'}, {'Https': '49.79.156.83:8000'}, {'Htpps': '60.255.186.169:8888'},{'Htpps': '115.46.73.162:8123'}, {'Https': '60.176.239.194:6666'}]
        self.proxies = random.choice(proxies)

        # 第一次解析
        self.first_xpath = '//div[@class="t_con cleafix"]/div/div/div/a/@href'

        # 第二次解析
        self.second_xpath = '//img[@class="BDE_Image"]/@src'

    # 1.发送请求
    def send_request(self,url):
        data = requests.get(url, headers=self.headers, proxies=self.proxies).content
        return data

    # 2.保存本地文件
    def sava_data(self,data,image_name):
        file_name = 'images/' + image_name
        print(file_name)
        with open(file_name,'wb') as f:
            f.write(data)

    # 3.解析
    def analysis_data(self, data, xpath_str):
        # 1.转换类型
        html_data = etree.HTML(data)

        # 2.解析
        result_list = html_data.xpath(xpath_str)

        return result_list


    # 4.执行
    def run(self):
        # 1.发送请求
        data = self.send_request(self.base_url)

        # 2.发送详情的请求解析
        # 2.1 详情url
        details_url_list = self.analysis_data(data, self.first_xpath)
        for link in details_url_list:
            url = 'http://tieba.baidu.com' + link
            details_data = self.send_request(url)
            # 3.请求图片
            img_url_list = self.analysis_data(details_data,self.second_xpath)
            for img_url in img_url_list:
                image_data = self.send_request(img_url)

                image_name = img_url[-11:]
                self.sava_data(image_data,image_name)


if __name__ == '__main__':
    TiebaSpider().run()