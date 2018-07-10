import requests
import json
import jsonpath


def city_data():
    # 1.url
    url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"}
    # 2.发送请求
    response = requests.get(url, headers=headers)
    data = response.content.decode()
    # 如果url是json后缀,可以直接使用.json
    # data = response.json()

    # 3.解析数据
    dict_data = json.loads(data)
    result = jsonpath.jsonpath(dict_data,'$..name')
    print(result)

if __name__ == '__main__':
    city_data()