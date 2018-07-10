import re


if __name__ == '__main__':
    # 1.替换sub
    str_one = 'chuan1 zhi2545'
    str_two = 'a b;dsafsan,Asds Bdsaf'
    pattern = re.compile(' |;|,')
    # result = pattern.sub("",str_two)

    pattern2 = re.compile('(\w+) (\w+)')
    result = pattern2.sub(r'\2\1',str_two)
    # 2.匹配中文unicode字符集
    chinese_str = '小明和老王的故事 no'
    chi_pattern = re.compile('[\u4e00-\u9fa5]+')
    result = chi_pattern.findall(chinese_str)

    # 3.spit分割
    str_thre = 'a,fsdsa,,,f;gffg l k'
    split_pattern = re.compile('[,; ]+')
    result = split_pattern.split(str_thre)

    print(result)