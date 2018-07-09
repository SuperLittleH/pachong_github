import requests


class TiebaSpider(object):
    def __init__(self):
        self.tieba_name = input('请输入您要查看的贴吧：')
        self.start_page = int(input('请输入您要查看的开始页：'))
        self.end_page = int(input('请输入您查看的结束页：'))

        self.tieba_url = 'https://tieba.baidu.com/f?'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 1.发起请求的方法
    def send_request(self,url,params):
        response = requests.get(url, headers=self.headers, params=params)
        data = response.content.decode()
        return  data


    # 2.保存数据
    def sava_data(self,data,page):
        # 保存路径
        file_path = 'Tieba/' + str(page) + '页.html'
        # 保存页数
        print('正在下载{}页...'.format(page))
        # 打开写入文件
        with open(file_path,'w')as f:
            f.write(data)
            print('保存成功')

    # 执行
    def run(self):
        # 1.参数
        for pns in range(self.start_page,self.end_page+1):
            params = {
                'kw':self.tieba_name,
                'pn':(pns-1)*50
            }
            # 2.发送请求
            data = self.send_request(self.tieba_url,params=params)
            # 3.保存数据
            self.sava_data(data,pns)

if __name__ == '__main__':
    tool = TiebaSpider()
    tool.run()