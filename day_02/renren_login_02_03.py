import requests


def renren_profile():
    # 1.登录时的url
    login_url = 'http://www.renren.com/PLogin.do'
    # 2.请求头
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    # 3.登录时参数
    login_data = {
        'email':'153546',
        'password':'165456'
    }
    # 登录请求 session对象自动保存cookie
    session = requests.session()
    session.post(login_url,headers=headers,data=login_data)
    profile_url = 'http://www.renren.com/250179934/profile'
    # 发起get请求请求下一步的数据
    data = session.get(profile_url, headers=headers).content.decode()
    # 保存数据
    with open('02renren3.html','w')as f:
        f.write(data)
        print('数据保存完成')
if __name__ == '__main__':
    renren_profile()