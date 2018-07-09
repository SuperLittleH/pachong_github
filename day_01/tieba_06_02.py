import requests


class TiebaSpider(object):
    def __init__(self):
        self.tieba_name = input('您想看的贴吧名称是:')
        self.tieba_url = 'https://tieba.baidu.com/f?'
        self.headers =  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 1.发起请求
    def send_request(self,url,params):
        response = requests.get(url,headers=self.headers,params=params)
        data = response.content.decode()
        return data

    # 2.保存
    def sava_data(self,data,page):
        file_name = 'Tieba/' + str(page) + '页.html'
        print('正在下载第{}页....' .format(page))
        with open(file_name,'w')as f:
            f.write(data)
            print('保存成功')

    # 3.运行
    def run(self):
        # 1.参数
        for pns in range(0,500,50):
            params = {
                'kw':self.tieba_name,
                'pn':pns
            }
            # 2.发起请求
            data = self.send_request(self.tieba_url,params=params)

            # 3.保存数据
            page = pns/50 + 1
            self.sava_data(data,page)

if __name__ == '__main__':
    tool = TiebaSpider()
    tool.run()