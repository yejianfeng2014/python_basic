a_tuple = ('crazyit', 20, 3.33)
b_tuple = (127, 'crazyit', 'fkit', 3.33)

c = a_tuple + b_tuple

# 如果有重复元素不会去重
print(c)

list_a = [20, 30, 50, 100]

list_b = ["a", "b", "c"]

list_c = list_a + list_b

print(list_c)

# 列表的乘法，把列表复制多份


list_d = list_c * 3

print(list_d)  # [20, 30, 50, 100, 'a', 'b', 'c', 20, 30, 50, 100, 'a', 'b', 'c', 20, 30, 50, 100, 'a', 'b', 'c']

# 序列封包和解包
# *last 会把剩余的元素全部匹配

first, second, *last = range(10)

print(first)
print(second)
print(last)

# first保存第一个元素，last保存最后一个元素，middle保存中间剩下的元素
first, *middle, last = range(10)
print(first) # 0
print(middle) # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(last) # 9
