# if 的相关操错

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'audi':
        print(car.upper())
    else:
        print(car.lower())
# 比较时忽略大小写

if cars[0].upper() == 'AUDI' :
    print(True)

# 检查是否不想等
requested_topping = 'mushrooms'

if requested_topping != 'ac':
    print(1)

# 比较数字

age = 18

if age == 19:
    print(True)
else:
    print(False)


# 5.2.5 检查多个条件：

age_0 = 22
age_1 = 18
# 使用 and
print(age_0 > 20 and age_1 >2)

# 使用or

if age_0 > 25 or age_1 > 1:
    print(3)

#检查特定值在列表中

requested_toppings = ['mushrooms', 'onions', 'pineapple']

print('onions' in requested_toppings)


# 检查特定值不在列表中

print('onions'  not in requested_toppings)

# 布尔表达式

game_active = True

can_edit = False


