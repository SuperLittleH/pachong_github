import json

if __name__ == '__main__':
    # json_str = '{"name":"雷布斯","age":56}'
    #
    # json_dict = json.loads(json_str)

    json_dict = {'name':'ji','age':56}

    json_str = json.dumps(json_dict)

    # 文件对象
    # fp = open('01.json','r')
    # fp_dict = json.load(fp)

    fp = open('02.json','w')
    fp_str = json.dump(json_dict,fp)

    print(type(fp_str))