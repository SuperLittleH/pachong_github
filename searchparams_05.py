import requests


class Search_Spider(object):
    def __init__(self):
        self.search_word = input('请输入您要搜索的内容：')
        self.base_url = 'https://www.baidu.com/s?wd='
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 1.发送请求
    def send_request(self,url):
        response = requests.get(url,headers=self.headers)
        # 数据
        data = response.content.decode()
        return data

    # 2.保存数据
    def save_data(self,data):
        with open('05.html','w')as f:
            f.write(data)

    # 3.调度方法
    def run(self):
        # 拼接url
        url = self.base_url + self.search_word
        # 1.发送请求
        data = self.send_request(url)
        # 2.保存文件
        self.save_data(data)
if __name__ == '__main__':
    tool = Search_Spider()
    tool.run()