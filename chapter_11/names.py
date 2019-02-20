
from name_function import get_formatted

print('enter q exit ...')

while True:
    first = input('请输入名称')
    if first == 'q':
        break
    else:
        last_name = input('enter your last name')
        formatted = get_formatted(first, last_name)

        print('your full name is ',formatted)
