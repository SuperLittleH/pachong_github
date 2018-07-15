import time
from bs4 import BeautifulSoup
from selenium import webdriver


class DouYuSpider(object):
    def __init__(self):
        self.url = 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Chrome()
        self.count = 0


    # 2.解析数据
    def analysis_data(self,data):
        soup = BeautifulSoup(data, 'lxml')
        room_list = soup.select('#live-list-contentbox .ellipsis')
        nick_list = soup.select('#live-list-contentbox .dy-name')
        hot_list = soup.select('#live-list-contentbox .dy-num')

        for room,nick,hot in zip(room_list, nick_list, hot_list):
            print('直播间的名称:' + room.get_text().strip()+'==', '直播间主播:' + nick.get_text().strip() + '==', '直播间热度:' + hot.get_text().strip())
            self.count += 1


    # 3.保存数据
    def save_data(self,data):
        if data:
            with open('02_douyu.txt','w')as f:
                f.write(data)

    # 4.调度
    def run(self):
        # 1.发送请求
        self.driver.get(self.url)
        data = self.driver.page_source
        self.analysis_data(data)
        # print(analysis)
        # self.save_data(analysis)

        while True:
            if data.find('shark-pager-disable-next') != -1:
                break

            # 循环点击下一页
            next_element = self.driver.find_element_by_class_name('shark-pager-next')
            next_element.click()

            time.sleep(3)
            data = self.driver.get(self.url)
            self.analysis_data(data)
            # self.save_data(analysis)
        print('总个数:',self.count)

        self.driver.quit()

if __name__ == '__main__':
    DouYuSpider().run()