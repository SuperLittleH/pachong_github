import requests

def renren_login():
    # 1.url
    url = 'http://www.renren.com/872201594/profile'
    # 2.请求头 包括用户信息和cookie
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Cookie':'anonymid=jjcavjlya36tr4; depovince=BJ; _r01_=1; jebecookies=0c5c584d-7602-483a-a975-a1c5b167e51a|||||; JSESSIONID=abczNALV8zssW-Tmic-rw; ick_login=1a79ee1f-1dea-4728-bdb5-8d08e828dc92; jebe_key=f7591884-ad27-41e1-8c1a-a1fda48f7327%7C7902e4be46be2684f75b3264439d28ab%7C1531021949188%7C1%7C1531139637736; _de=BE93F2BDAF8C751ED28173EB34A8CC93; p=72ccbb57a423594bb4ac3069040e87784; first_login_flag=1; ln_uact=15971306907; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=8810c9c495e9e2e44b474f7f7a46fdd54; societyguester=8810c9c495e9e2e44b474f7f7a46fdd54; id=966837944; xnsid=80f711e4; ver=7.0; loginfrom=null; wp_fold=0'
        }
    # 3.发起请求
    data = requests.get(url, headers=headers).content.decode()
    # 4.保存数据
    with open('02renren.html','w')as f:
        f.write(data)
        print('数据保存成功')
if __name__ == '__main__':
    renren_login()