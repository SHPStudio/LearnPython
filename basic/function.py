# 函数
'''
python有很多内置的函数 比如abs()函数就是求绝对值的函数 而且可以通过help(abs) 来查看函数的相应信息
官网函数链接 http://docs.python.org/3/library/functions.html#abs
'''
# help(abs)

# 调用函数 如果函数参数个数有问题或者参数类型有问题都不会通过编译的 会报错
# abs() 绝对值函数
# print(abs(-10))
# print(abs(10))

# max(n1,n2,...) 求最大值函数
# print(max(1, 2, 4, 8, 6))
# print(max('sdf', 'dd', 'zfee'))

# 数据类型转换
# print(int('123'))
# print(int(12.36))
# print(float('12.36'))
# print(str(100))
# print(bool(1))
# print(bool(''))

# 给函数起别名 函数的名字其实就是一个引用 把引用传给别的变量 也就相当于给函数起一个别名了
# a = abs
# print(a(-3))

# 定义函数 如果想要return None的话可以简写为return
# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
#
#
# print(my_abs(-1))

# 从文件中导入函数
# from abtest import my_abs
#
# print(my_abs('-1'))

# 定义空函数 比如你可能开发一个模块 方法之间的架构已经想好了 那么可以先定义空函数 让它先跑通
# pass相当于一个占位符 为了能够让程序跑通 可以放在程序的任何位置
# def test():
#     pass
# a = 6
# if a > 15:
#     pass

# 函数返回多个值
# 函数返回的多个值其实就是一个tuple
# import math
# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y + step * math.sin(angle)
#     return nx, ny
#
#
# x, y = move(100, 100, 60, math.pi / 6)
# r = move(100, 100, 60, math.pi / 6)
# print(x, y)
# print(r)

# 参数的默认值
'''
为什么要设置参数的默认值呢
就是为了能够减少函数调用的复杂程度 比如你一开始写了一个函数就两个参数就够了等后期你要加功能需要加入新的参数
那么新加的参数如果很多并且没有设默认值，那么之前其他地方调用的时候就会报错，参数个数不匹配
所以需要加入参数的默认值，这样其他调用也不会出错，想要调用新的函数传入的参数也比较灵活可变
并且默认参数的应该放在必选参数的后面 把变化小的参数放到后面 还有 默认参数一定要是不可变的
'''
# 计算平方
# def my_pow(x):
#     return x * x
# def my_pow(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# print(my_pow(12, 4))
# 多个参数默认值不按照顺序传入参数
# 比如enroll(name,gender,age=7,city='beijing') 他有两个默认参数，如果不想按照顺序传参数的话那需要传入参数的时候把参数名字带上
# def enroll(name, gender, age=7, city='beijing'):
#     print(name)
#     print(gender)
#     print(age)
#     print(city)
# enroll('shp', '5', city='beijign')
# 默认参数的坑 默认参数是可变的
# 如果默认参数是可变的比如空列表那么每次调用会记住这个变量
# def add_end(L=[]):
#     L.append('End')
#     return L
# print(add_end([1, 2, 3, 4])) # 正常调用
# print(add_end([1, 2, 3, 4,5]))
# print(add_end()) # 非正常调用
# print(add_end()) # 会出现两个End
# 现在改为不可变
# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('End')
#     return L
# print(add_end())
# print(add_end())


# 可变参数
# 比如传入参数为一个列表或者tuple
# def calc(numbers):
#     sum = 0
#     for item in numbers:
#         sum = sum + item * item
#     return sum
# print(calc([1,2,3,4]))
# print(calc((1,2,3,4)))
# 但是这样写有点儿麻烦 python中在参数前面加一个星号代表可变参数可以简化调用
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# print(calc(1,2,3,4))
# print(calc())
# 比如我们想要传入一个列表或者tuple呢 那么就通过星号把列表tuple转换为可变参数 就像c语言中把对象转换成指针引用差不多
# nums = [1,2,3,4]
# print(calc(*nums))

# 关键字参数 用**表示 他是代表可以传入任意个带有参数名的参数，python会自动转换为dict字典
# def test_key(name,age,**keyparam):
#     print('name',name,'age',age,'other',keyparam)
# test_key('shp',20,city='beijing',country='xingshu')
# 它的作用主要是扩展函数的功能 比如做一个注册一开始可能只需要姓名和年龄，但是随着需求的不断变化
# 他需要更多的参数什么身份证号、住址、等等等等，就可以用一个关键字参数来扩展了
# 同样的我们可以建立一个dict变量 然后在调用函数的时候使用**把变量转换为关键字参数
# 注意：传入的keyparam只是my_dict的副本 并不会改变my_dict的值
# my_dict = {'city':'beijing','country':'xingshu'}
# test_key('shp',28,**my_dict)

# 命名关键字
# 使用关键字参数按照字典的形式传参数，但是如果要是传入不相关的key-value值是没用的，我们如果要想让用户按照规定的key来传值
# 就要用到命名关键字了
# 用法是如果后面的是需要限定的参数的关键字那么就在必须参数和关键字参数之间加个*来进行分割
# def test_limitkey(name,age,*,city,country):
#     print('name',name,'age',age,'city',city,'country',country)
# test_limitkey('shp',30,city='sdf',country='dd')
# limitkey = {'city':'beijing','country':'xingshu'}
# test_limitkey('shp',30,**limitkey)
# 如果有可变参数了就不需要加*来分割了 就用可变参数就可以来当做分割
# 把命名关键字参数加入默认值那么就可以不传这个关键字的参数
# def test_limitkey(name,age,*,city='beijing',country):
#     print(name,age,city,country)

# 参数的组合
# 可以使用各种参数进行组合
# 注意：组合的顺序 必选参数->默认参数->可选参数->命名参数->关键字参数
# 任何带有参数的方法都可以用 function(*args,**args2)来调用

# 递归函数
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(50000))
# 因为递归函数每次递归的时候都会增加一个调用栈，如果很多的话就会导致调用栈溢出报错
# 所以可以进行尾递归优化 尾递归优化就是在return的时候调用自身 没有任何多余的操作，这样让解释器或者编译器优化为只用一个调用栈这样就不会溢出
# def fact_op(n,product):
#     if n == 1:
#         return product
#     else:
#         return fact_op(n-1,n * product)
# print(fact_op(5,1))
# 因为大部分解释器或者编译器没有做这种优化，所以依然会导致栈溢出