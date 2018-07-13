from bs4 import BeautifulSoup
import re

if __name__ == '__main__':
    html_data = '''
            <html><head><title>The Dormouse's story</title></head>
            <body>
            <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
            <p class="story">Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
            and they lived at the bottom of a well.</p>
            <p class="story">...</p>
        '''

    # 1.转换类型
    soup = BeautifulSoup(html_data,'lxml')

    # 2.解析数据
    # 1.find 符合条件的第一个标签
    result = soup.find(name='p')
    result = soup.find(attrs={'id':'link2'})
    result = soup.find(text='...')
    pattern = re.compile('^a')
    result = soup.find(pattern)

    # 2.find_all返回列表
    result = soup.find_all('a')

    # 3.select css选择器
    # 1.标签选择器
    result = soup.select('title')
    # 2.类选择器
    result = soup.select('.title')
    # 3.id选择器
    result = soup.select('#link3')
    # 4.层级选择器
    result = soup.select('p a')
    # 5.组选择器
    result = soup.select('.story,.title')
    # 6.属性选择器
    result = soup.select('a[id="link3"]')

    # 7.找标签包裹的内容
    result = soup.select('#link3')[0].get_text()
    # 8.包含的属性
    result = soup.select('#link3')[0].get('href')

    print(result)