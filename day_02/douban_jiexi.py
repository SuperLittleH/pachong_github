import json
import jsonpath


def load_data():
    list = []
    with open('01.json','r')as f:
       for i in range(698):
            p = f.readline()
            dict_data = json.loads(p)
            list.append(dict_data)
            print(jsonpath.jsonpath(dict_data,'$..title'))
            print(list)

if __name__ == '__main__':
    load_data()