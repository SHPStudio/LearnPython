# 函数式编程
# 函数式编程是一种抽象度高的编程方式
# 推崇一种没有副作用的函数形式，也就是说只要输入确定，输出就确定。
# 但是有很多语言都是有变量的，所以一个函数的输出还受到其他变量的影响，所以这种函数就是有副作用的。
# 现在比较提倡函数式编程因为输入输出的确定代表要进行单元测试等等就会非常的简单容易，程序定位错误也简单。

# 高阶函数 即参数可以是函数 返回值也可以是函数
# 那参数是函数怎么写 其实就是函数的名字 函数的名字其实就相当于指向具体函数的指针
# b = abs
# print(b(-10))
# 如果我们改变abs的引用
# abs = 10
# print(abs(10))
# 那么他就会报错了
# print(abs(-10))
# def add(x,y,f):
#     return f(x) + f(y)
# f = abs
# print(add(2,-3,f))

# map 他有两个参数 一个是函数 一个是Iterable对象
# 函数也就是计算函数 把Iterable的每个值都传入这个函数并把得到的每个计算结果作为Iterator返回
# def my_pow(x):
#     return x * x
# L = list(range(1,11))
# reduce_L = map(my_pow,L)
# print(list(reduce_L))

# reduce函数
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 求和
from functools import reduce
# def my_sum(x,y):
#     return x + y
# sumd = reduce(my_sum,[x for x in range(1,6) if x % 2 != 0])
# print(sumd)
# str转换成int
# def transferToInt(s):
#     return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,}[s]
# def cal(x,y):
#     return x * 10 + y
# sum = reduce(cal,map(transferToInt,'1356'))
# 把函数整合到一起
# def str2int(s):
#     def ch2int(c):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, }[c]
#     def cal(x,y):
#         return x * 10 + y
#     return reduce(cal,map(ch2int,s))
# print(str2int('2645'))
# 还可以使用lamda表达式把计算那步优化掉
# def str2int(s):
#     def ch2int(c):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, }[c]
#     return reduce(lambda x,y:x*10+y,map(ch2int,s))
# print(str2int('23234234'))

# filter函数
# filter函数的作用是用来过滤元素的 跟map很像，不过就是把每个元素传入到过滤逻辑函数 返回的True代表留下元素 False去掉元素
# def odd(n):
#     return n % 2 == 1
# print(list(filter(odd,[1,2,5,3,4,8])))
# 除None和空的字符串
# def not_empty(str):
#     return str and str.strip()
# L = list(filter(not_empty,['15','  0',' ',None,'shp']))
# print(L)
# str = '1'
# print(bool(str and str.strip()))

# sorted函数排序函数
# L = [5,6,4,2,1,8,6,89]
# print(sorted(L))
# key属性是一个处理函数 比如按照绝对值排序
L = [-9,5,-1,56,-88,15,-41]
print(sorted(L,key=abs))
# 反向排序
print(sorted(L,key=abs,reverse=True))