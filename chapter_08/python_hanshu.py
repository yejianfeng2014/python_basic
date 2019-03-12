# 函数操作

def greet_user():
    '显示简单的问候语'
    print('hello')


greet_user()


def greet_user_1(name):
    print("hello user " + name.title())


greet_user_1("lisi")


def describe_pet(animal_type, pet_name):
    '''显示宠物的信息'''
    print('animal type: ' + animal_type)
    print('animal name: ' + pet_name)


describe_pet('cat', 'tom')

# 关键字实参 ，制定参数名称，不必和参数顺序一致了
describe_pet(animal_type='hamster', pet_name='harry')


# 8.2.3 默认值
def describe_pet_with_moren_name(pet_name, animal_type='dog'):
    print('animal name is :' + pet_name)
    print('animal tpye is :' + animal_type)


describe_pet_with_moren_name('cat', 'cat')
describe_pet_with_moren_name('cat')


# 8.3.1 函数的返回值

def get_formated_name(first_name, last_name):
    "返回完整的name"
    full_name = first_name + ' ' + last_name
    return full_name


formated_name = get_formated_name('li', "si")

print(formated_name)


# 返回一个字典
def build_person(first_name, last_name):
    '''返回一个字典包含一个人的信息'''
    person = {'first': first_name, 'last': last_name}

    return person


person = build_person('li', "si")

print(person['first'])
print(person['last'])


# 8,4  传递列表

def greet_users(names):
    '''向列表中的每一个用户问好'''
    for user in names:
        print('hello :' + user)


names = ['zhangsan', 'lisi', 'wangwu']

greet_users(names)


# 传递任意数量的实参,实际用一个用一个元组接受

def make_pizza(*toppings):
    ''' 打印顾客点的所有配料'''

    print(toppings)


make_pizza('a')
make_pizza('a', 'b', 'd')


# 8.5.1 使用位置实参，和任意数量的参数

def make_pizza_many(size, *toppings):
    '''要制作的披萨'''

    print('to make 披萨的 size:' + str(size))

    for t in toppings:
        print(t)


make_pizza_many(43, 'a', 'b', 'c')

# 将函数存在在模块中
