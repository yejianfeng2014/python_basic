# 类的操作

# 创建类

class Dog():
    '''一次模拟小狗的简单尝试'''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def site(self):
        ''' 定义命令式坐下'''
        print(self.name.title() + 'now is siting')

    def roll_over(self):
        '模拟小狗收到命令是打滚'

        print('dog is roll overing...')


my_dog = Dog('while', 6)

print(my_dog)
print(my_dog.name)
print(my_dog.age)
my_dog.roll_over()

my_dog.site()


class Car():
    def __init__(self, make, model, year):
        '''初始化汽车的属性'''
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        print(self.make, self.model, self.year)


my_car = Car('zhongguo', 'a4', '2014')

print(my_car.model)

my_car.description()


# 给属性添加默认值

class Car_with_moren():
    def __init__(self, make, model, year):
        '''初始化默认值'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def read_odometer(self):
        print('this car odometer', self.odometer)


my_car_new = Car_with_moren('audo', 'a4', 2019)

my_car_new.read_odometer()

# 继承
