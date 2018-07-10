import re


if __name__ == '__main__':
    str_one = 'abc123'
    str_two = '456'
    pattern = re.compile('^\d+$')
    # 1.match 从头开始匹配一次 如果不是纯数字会报错
    # result = pattern.match(str_one).group()
    # 2.search从任意位置
    # result = pattern.search(str_one).group()
    # 3.findall 返回list
    str_thre = 'dsadsafsgsagsagsassssds'
    pattern = re.compile('s')
    # result = pattern.findall(str_thre)
    # finditer
    result = pattern.finditer(str_thre)
    print(result)
    for res in result:
        # print(res)
        print(res.group())


    # print(result)