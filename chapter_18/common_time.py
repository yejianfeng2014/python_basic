import time

# 把当前时间转成字符串

print(time.asctime())

# 返回当前进程使用cpu时长

print(time.process_time())


# 返回性能计数器的值
print(time.perf_counter())


# 将当前时间转换为指定格式的字符串
print(time.strftime('%Y-%m-%d %H:%M:%S'))



st = '2018年3月20日'
# 将指定时间字符串恢复成struct_time对象。
print(time.strptime(st, '%Y年%m月%d日'))

#  返回从1970年1970年1月1日0点整到现在过了多少秒。
print(time.time())


# 返回时区的偏移值

print(time.timezone)

