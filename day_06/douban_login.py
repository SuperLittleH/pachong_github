from selenium import webdriver
import time

from day_06.yundama import indetify
import requests

def login_douban():
    driver = webdriver.Chrome()
    driver.get('https://www.douban.com/')

    # 用户名
    driver.find_element_by_id('form_email').send_keys('mr.mao.tony@gmail.com')
    # 密码
    driver.find_element_by_id('form_password').send_keys('ALARMCHIME')

    # 验证码的图片
    image_url = driver.find_element_by_id('captcha_image').get_attribute('src')
    response = requests.get(image_url)

    code = indetify(response.content)

    # 验证码
    driver.find_element_by_id('captcha_field').send_keys(code)

    # 登陆点击
    driver.find_element_by_class_name('bn-submit').click()

    time.sleep(3)

login_douban()