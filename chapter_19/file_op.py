from pathlib import *

# 获取当前的路径
p = Path(".")

# 遍历当前目录下所有文件和子目录
for x in p.iterdir():
    print(x)

cwd = p.cwd()
print()

