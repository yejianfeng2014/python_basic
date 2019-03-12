# 列表

bicycle = ["trek","cannondale","reline","specialized"]

print(bicycle)
# ['trek', 'cannondale', 'reline', 'specialized']

# 访问元素处演示了访问列表元素的语法。当你请求获取列表元素时，P
# ython只返回该元素，而不包
# 括方括号和引号：
print(bicycle[0])
print(bicycle[0].title())

# 访问最后一个元素

print(bicycle[-1])

#3.2 修改删除和添加
motorcycles = ['honda','ymaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# 末尾添加元素

motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)

motorcycles.append('ducati')

print(motorcycles)

# 在列表中插入元素

list_1 = ['honda','yamaha','suzuki']

list_1.insert(0,'ducati')

print(list_1)

# 从列表中删除元素 要删除的元素在列表中的位置，可使用 del 语句。

list_2 = [1,2,3,4,5]

del list_2[2]

print(list_2)

# 使用pop 删除元素 从list 里面删除该值，而且还要使用该值

list_3 = [7,8 ,9]
print(list_3)

pop_1 = list_3.pop() # 删除末尾元素

print(pop_1) # 9

print(list_3)

#删除列表任何位置的元素

list_4 = [1,2,3,4,5]

pop_4 = list_4.pop(0)

print(pop_4)

print(list_4)

# 根据值删除元素 remove()

list_5 = [3,4,5,6]

list_5.remove(4)
print(list_5)

list_5.insert(0,4)
list_5.insert(0,4)
print(list_5)

list_5.remove(4)

print(list_5)

list_5.remove(4)

print(list_5)
# 如果没有使用remove 会报错

try:
     list_5.remove(4)
except:
     print('报错了')
print(list_5)


# 确定列表的长度

print(len(list_5))












