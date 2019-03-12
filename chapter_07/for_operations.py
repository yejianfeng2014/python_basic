# 循环和用户输入

message = "tell me something and i repeate it to you "

print(message)

# name = input("please enter your name : ")
#
# print(name)

# 字符串转数字
age = '17'

int_age = int(age)

print(type(age))
print(type(int_age))

# 求模运算

number = 100
if number % 2 == 0:
    print('是一个偶数')

# while 循环
current_number = 1

while current_number < 5:
    print(current_number)
    current_number = current_number + 1

# 使用break 推出循环
#
# promp = "please input a city name  if name equals quit exit..."
# while True:
#     city = input(promp)
#
#     if city == 'quit':
#         break
#     else:
#         print(" i love to go to " + city.title())

# 使用continue

current_number = 0

while current_number < 10:
    current_number +=1
    if current_number % 2 == 0:
        continue
    print(current_number)




