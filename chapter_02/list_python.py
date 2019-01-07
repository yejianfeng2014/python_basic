# list


# 构建
a = list()  # 方法1

a1 = []  # 方法2

mylist = [1]

# 多维度
mylist_1 = [
    [1, 2],
    [3, 4]
]

# 添加元素


mylist.append(2)

print(mylist)

# 在指定位置插入


mylist.insert(0, 1)

print(mylist)

# 截取


my_list_t0 = [1, 2.0, None, False, "zifu"]

print(my_list_t0[0])
print(my_list_t0[3:4]) # [False]
print(my_list_t0[::2])

print(my_list_t0[-1])
print(my_list_t0[:2])


