import re


if __name__ == '__main__':
    str_one = '''
                ahhhhb
                fasfasfsa
                lpokokB
    '''
    # 1.创建正则对象
    patter = re.compile('a(.*)b',re.S|re.IGNORECASE)




    # 2.findall
    result = patter.findall(str_one)
    print(result)

    # 3.原始字符串
    str_two = r'a\nb'
    str_thre = r'a\bn'
    print(str_thre)