import  requests


class TiebaSpider(object):
    def __init__(self):
        self.tieba_name = input('请输入您想看的贴吧:')
        self.tieba_url = 'https://tieba.baidu.com/f?'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 1.发送请求
    def send_request(self,url,params):
        response = requests.get(url,headers=self.headers,params=params)
        data = response.content.decode()
        return data

    # 2.保存
    def sava_data(self,data):
        with open('07.html','w')as f:
            f.write(data)

    # 3.执行
    def run(self):
        # 1.参数
        params = {
            'kw':self.tieba_name,
            'pn':0
        }
        # 2.发送请求
        data = self.send_request(self.tieba_url,params=params)
        # 3.保存
        self.sava_data(data)

if __name__ == '__main__':
    tool = TiebaSpider()
    tool.run()