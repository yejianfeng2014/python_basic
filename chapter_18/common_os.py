import  os

# 显示导入依赖模块的操作系统的名称
print(os.name)

# 显示当前路径
print(os.getcwd())

# 获取PYTHONPATH环境变量的值
print(os.getenv('PYTHONPATH'))

# 返回当前系统的用户登录名

print(os.getlogin())

# 获取当前进程id

print(os.getpid())

# 获取当前进程的ppid

print(os.getppid())

# 获取当前系统的cpu个数

print(os.cpu_count())

# 返回路径分隔符

print(os.sep)

# 环境变量的分隔符
print(os.pathsep)

# 获取当前系统的换行符

print(os.linesep)




