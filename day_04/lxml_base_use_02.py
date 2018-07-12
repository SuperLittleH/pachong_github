from lxml import etree


if __name__ == '__main__':
    html_str = '''
            <div>

                <p class="one"  id="first"></p>
             <ul>
            <li class="item-1"><a href="link1.html">first item</a></li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-inactive"><a href="link3.html">third item</a></li>
            <li class="item-1"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a>
            </ul> </div>
        '''


    # 1.转成可解析的类型
    html_data = etree.HTML(html_str)

    # 2.解析数据xpath('//a')返回list
    result = html_data.xpath('//a/text()')

    # 3.取出link3的标签
    result = html_data.xpath('//li[@class="item-inactive"]/a/text()')
    result = html_data.xpath('//a[@href="link3.html"]/text()')[0]

    # 取出标签的属性@属性名字
    result = html_data.xpath('//p/@id')

    result = html_data.xpath('//li[1]/a/text()')
    all_data = etree.tostring(html_data)

    print(all_data)