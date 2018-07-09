import requests


class Seaech_Spider(object):
    def __init__(self):
        self.search_word = input('请输入搜索内容：')
        self.base_url = 'https://www.baidu.com/s'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 1.发送请求
    def send_request(self,url,params):
        response = requests.get(url,headers=self.headers,params=params)
        data = response.content.decode()
        return data



    # 2.保存
    def save_data(self,data):
        with open('06.html','w')as f:
            f.write(data)



    # 3.调度方法
    def run(self):
        # 拼接参数
        params = {
            'wd':self.search_word,
        }
        # 1.发送请求
        data = self.send_request(self.base_url,params=params)
        # 2.保存
        self.save_data(data)


if __name__ == '__main__':
    tool = Seaech_Spider()
    tool.run()

