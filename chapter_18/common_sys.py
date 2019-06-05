import  sys

#显示本地字节的指示符
print(sys.byteorder)
# 显示版权信息
print(sys.copyright)

# 显示当前python解析器的路径
print(sys.executable)

# 显示当前系统保存文件所用的字符集

print(sys.getfilesystemencoding())

# 显示Python整数支持的最大值
print(sys.maxsize)
# 显示当前的平台
print(sys.platform)

# 显示当前解析器的版本
print(sys.version)

# 显示当前主版本号
print(sys.winver)


# 运行时传入参数

from  sys import argv

print('传入参数个数： ',len(argv))

for arg in argv:
    print(arg)


# 模块动态加载路径：
import sys
# 动态添加g:\fk_ext路径作为模块加载路径
sys.path.append('g:\\fk_ext')
# 加载g:\fk_ext路径下的hello模块
import hello