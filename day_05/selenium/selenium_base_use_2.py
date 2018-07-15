from selenium import webdriver
import time

def load_data():
    # 1.创建浏览器
    driver = webdriver.Chrome()

    # 2.请求首页
    driver.get('https://www.baidu.com/')

    # 3.点击新闻按钮
    driver.find_element_by_name('tj_trnews').click()

    # 4.给输入框输入内容
    driver.find_element_by_id('ww').send_keys('德国战车')

    # 点击搜索按钮
    driver.find_element_by_class_name('btn').click()

    driver.find_element_by_xpath('//div[@id="1"]/h3/a').click()

    # 由于点击标签新开一个页面
    print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[1])

    # 保存快照
    driver.save_screenshot('02_xinwen.png')

if __name__ == '__main__':
    load_data()