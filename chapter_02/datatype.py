# int  类型
#
# Python 3 dynamically extends int, when it’s too big
# In Python 3 there is not maximal int value
# You can use _ for easier read especially with big numbers


value = 30

million = 1000000

million_new = 100

print(value)
print(value)
print(million_new)


# convert to int

i = int(10)
print(int(10.9))
print(int(1.23))
print(int(-1.23))
print(i)


# 2 float

value = 10.0

value = .44 # 0.44

# 2.2 科学计数

mill = 1e6


# foalt 的最大值和最小值

import  sys
print(sys.float_info.min)


print(sys.float_info.max)


# conver to float

print(float(2.3))

print(float("2.4"))

# bool 布尔值


my_var = True
my_var_new = False


# convert to bool

print(bool(1))

print(bool(0))


# 等于false 的bool 的情况
#
# False
# 0
# 0.0
# () - empty tuple
# {} - empty dict
# [] - empty list
# '' - empty str
# set() - empty set
# None


# 3.4 逻辑判断 and

True and True


1 or 0



# 4 none


my_var_none = None




# 5 字符串


text = ''' first line
        second line
        third line'''

# type convert to str

print(str(123))

print(str(True))