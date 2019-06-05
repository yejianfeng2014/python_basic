# collections 包下的 Counter 也是一个很有用的工具类，它可以自动统计容器中各元素出现的次数。


from collections import Counter

c1 = Counter()

print(c1)


c2 = Counter('hannah') # 每一个字符是一个原色
print(c2)



c3 = Counter(['Python', 'Swift', 'Swift', 'Python', 'Kotlin', 'Python'])
print(c3)


print(c3["Python"])

print(type(c3))


from collections import Counter
# 创建Counter对象
cnt = Counter()
# 访问并不存在的key，将输出该key的次数为0.
print(cnt['Python']) # 0

for word in ['Swift', 'Python', 'Kotlin', 'Kotlin', 'Swift', 'Go']:
    cnt[word] += 1
print(cnt)

