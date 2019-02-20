# 写入json 文件

import json

numbers =[1,23,2,4,22,245,78]

file_name = 'number.json'

with open(file_name,'w') as fobj:
    json.dump(numbers,fobj)