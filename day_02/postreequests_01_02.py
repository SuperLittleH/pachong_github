import requests
import json

def fanyi_baidu():
    # 1.根据用户翻译内容
    words = input('请输入您要翻译的内容:')
    # 2.url
    url = 'http://fanyi.baidu.com/basetrans'
    # 3.请求头
    headers =  {"User-Agent": 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'}
    # 4.参数
    data = {
        'query':words,
        'from':'zh',
        "to":"en"
    }
    # 5.发起请求
    data_str = requests.post(url,data=data,headers=headers).content.decode()
    # 6.解析数据
    dict_data = json.loads(data_str)
    result = dict_data['trans'][0]['result'][0][1]

    print('翻译的结果是：{}'.format(result))

if __name__ == '__main__':
    fanyi_baidu()