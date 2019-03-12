# python 字典的相关操作

alien_0 = {'color': 'green',
           'point': 5}

print(alien_0['point'])

# 添加元素

alien_0['x'] = 0.0

alien_0['y'] = 1.1

print(alien_0)

# 创建一个空字典，然后给字典里面添加值

map_1 = {}

map_1['value_1'] = 1

map_1['name'] = 'zhangsan'

map_1['age'] = 'ssss'

print(map_1)

# 修改字典中的值

map_1['name'] = 'lisi'

print(map_1)

# 6.2.5 删除元素

map_del_test = {}

map_del_test['name'] = "name_1"
map_del_test['age'] = 23

map_del_test['color'] = 'red'

print(map_del_test)
del map_del_test['color']

print(map_del_test)
#
try:
    del map_del_test['color']
except:
    print("删除不存在的会报错")

print(map_del_test)

# 由类似对象组成的字典 ，所以可以使用嵌套
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# 6.3.1遍历字典

user_0 = {
    'username': 'efermi',
    'first': 'enrio',
    'last': 'fermi'

}

for key, value in user_0.items():
    print('\n key :' + key)
    print("value : " + value)

# 遍历所有的key

for name in user_0.keys():
    print(name)

# 遍历所有的value
print('遍历所有的value >>>>>>>>')
for valu in user_0.values():
    print(valu)

# 嵌套 列表中嵌套 字典

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# 字典中嵌套 列表

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(pizza)

# 字典中存储字典

uers = {
    'person1': {
        'first': 'alert',
        'name': 'zhangsan',
        'age': 23

    },
    'person2': {
        'first': 'alert',
        'name': 'zhangsan',
        'age': 24

    }
}

for k,v in uers.items():
    print(k)
    print(v)


