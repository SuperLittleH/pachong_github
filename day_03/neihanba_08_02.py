import re
import requests


class NeiHanBaSpider(object):
    def __init__(self):
        self.base_url = 'https://www.neihan8.com/article/list_5_'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
        self.proxies = {'Https':'118.114.77.47:8080'}
        self.pattern = re.compile('<div class="f18 mb20">(.*?)</div>',re.S)
        self.sava_pattern = re.compile('<(.*?)>|&(.*?);|\s')

    # 1.发送请求
    def send_data(self,url):
        data = requests.get(url,headers=self.headers, proxies=self.proxies).content.decode('gbk')
        return data

    # 2.解析数据
    def analysis_data(self,data):
        result_data = self.pattern.findall(data)
        return result_data

    # 3.保存数据
    def sava_data(self,result_data,page):
        page_number = '------------第' + str(page) + '页' + '\n\n\n'
        print(page_number)
        with open('08_neibhanba_02.txt','a')as f:
            f.write(page_number)
            for content in result_data:
                new_content = self.sava_pattern.sub("",content) + '\n\n'
                f.write(new_content)
            print('数据写入完成')

    # 4.拼接大量url
    def get_url(self):
        list_url = []
        for page in range(1,507):
            url = self.base_url + str(page) + '.html'
            list_url.append(url)
        return list_url

    # 4.执行
    def run(self):
        # 根据url列表循环写入端子
        url_list = self.get_url()
        for url in url_list:
            # 2.发送请求
            data = self.send_data(url)
            # 3.解析数据
            result_data = self.analysis_data(data)
            # 4.保存数据
            page = url_list.index(url) + 1
            self.sava_data(result_data,page)


if __name__ == '__main__':
    NeiHanBaSpider().run()