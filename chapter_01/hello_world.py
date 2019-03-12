print("hello")

# 变量

msg = "hello world "

print(msg)

# 字符串
# title()实现了单词的首字母大写
name = "ada lovelace"
print(name.title())

# 转大写，转小写
print(name.upper())  # ADA LOVELACE
print(name.lower())  # ada lovelace

# 拼接字符串

first_name = "ada"

last_name = "lovelace"

full_name = first_name + " " + last_name

print(full_name)

# 删除空白
favorate_language = "python "

print(favorate_language)  # 打印输出结果带了空格
# 删除右边空格
print(favorate_language.rstrip())

favorate_language = ' python '
# 删除做空格
print(favorate_language.lstrip())

favorate_language = ' python '
print(favorate_language)
# 删除两边的空格
print(favorate_language.strip())

# 双引号中套单引号
message = "One of Python's strengths is its diverse community."
print(message)

## 2.4 数字

print(2 + 2)

print(3 - 1)

print(3 * 3)

print(9 / 3)

print(3 / 2)

# 浮点数

print(0.1 + 0.1)

print(0.2 + 0.1)

print(3 * 0.1)

# 数字和字符串的拼接不能直接用加号，需要用str 转下
age = 23
message = " Happy " + str(age) + "rd Birthday"

print(message)

