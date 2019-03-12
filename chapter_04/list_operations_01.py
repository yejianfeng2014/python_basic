# 列表的操作

# 列表的遍历

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician)

# 创建数值列表 range() 不包含结束元素

for value in range(1, 10):
    print(value)

print(range(1, 9))
# 使用range 创建list

list_1 = list(range(1, 11))

print(list_1)

# 数字列表统计
print(min(list_1))

print(max(list_1))

print(sum(list_1))

# 4.4 切片 不包含最后一个

plays = ['charls', 'martia', 'michael', 'florence', 'eli']
print(plays)
print(plays[0:3])

# 如果没有起始索引，代表从头开始

print(plays[:2])

# 如果没有结束索引，代表到最后一个

print(plays[2:])

# 从末尾切片使用 负数

print(plays[-3:])

# 4.4.3 复制列表

my_foods = ['pizza', 'falafel', 'carrot cake']

friend_food = my_foods[:]

print("my favorite")

print(my_foods)

print("myfriend food")

print(friend_food)

my_foods.append('cannoli')

friend_food.append('ice cream')

print(my_foods)
print(friend_food)

# 4.5 元组

# 4.5.1 元组的定义 使用圆括号
dimensions = (2, 3)
print(dimensions[0])

print(dimensions[1])

#4.5.2遍历 元组中的元素

tuples = (200,30)

for t in tuples:
    print(t)

# 修改元组的值，采用定义元组的模式 因为给元组变量赋值是合法的
dimensions = (200, 50)

dimensions = (1,3)

print(dimensions)



