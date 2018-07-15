from selenium import webdriver
import time

def load_data():
    # 创建浏览器
    driver = webdriver.Chrome()

    # 2.请求数据
    driver.get('https://www.lagou.com/jobs/list_django?px=default&xl=%E5%A4%A7%E4%B8%93&city=%E5%8C%97%E4%BA%AC#filterBox')

    js = 'window.scrollTo(0,document.body.scrollHeight)'

    driver.execute_script(js)
    # 截屏
    driver.save_screenshot('01_itcaast.png')

if __name__ == '__main__':
    load_data()