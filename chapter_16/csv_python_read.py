# csv 文件操作

import csv

from matplotlib import pyplot as plt

file_name = "files/school_name_cn_en_1.csv"

with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # 读取csv 文件的首行
    print(header_row)

    for index, column in enumerate(header_row):
        print(index, column)


    hights = []
    #获取第二列
    for row in reader:
        hights.append(len(row[1]))
    print(hights)


    # 绘图

    plt.figure(dpi= 128, figsize= (10,6))

    plt.plot(hights,c = 'red')

    plt.show()

#datetime 模块

from datetime import  datetime


first_date = datetime.strptime('2014-7-1','%Y-%m-%d')

print(first_date)