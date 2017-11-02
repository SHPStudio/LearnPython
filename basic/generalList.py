# 列表生成式
# 用range()函数可以生成一个从开始数字到结束数字的数列然后使用list()转换成列表
# 但是如果要是生成[1x1,2x2,3x3]的列表就要需要使用列表生成器来方便生成了
# L = [x * x for x in range(1,11)]
# print(L)
# 把要生成的x * x 放在前面 后面定义x的数据来源
# 迭代提供x的数据来源 并且还可以对x进行二次处理
# L = [x * x for x in range(1,11) if x % 2 == 0]
# print(L)
# 两层循环 组成全排列
# L = [m + n for m in 'ABCD' for n in 'ZHWN']
# print(L)
# 用列表生成式来列出当前路径所有文件夹
# import os
# L = [d for d in os.listdir('.')]
# print(L)
# 其实for迭代器可以同时使用两个甚至更多的变量的 比如迭代dict字典
# my_dict = {'name':'shp','age':20,'app':'background'}
# for k,v in my_dict.items():
#     print(k,'=',v)
# 所以也可以用迭代来生成列表
# L = [k + '=' + v if isinstance(v,str) else k + '=' + str(v) for k,v in my_dict.items()]
# print(L)
# 但是如果列表中有int类型的值遍历生成的时候就会出错
# 我们可以对类型进行过滤 或者就只有字符串类型
# L = ['SHOP','OVER',18,'EEE']
# CL = [s.lower() if isinstance(s, str) else str(s) for s in L ]
# print(CL)
# 这句话表明如果是str类型的就转换小写 如果不是就转换成字符串

# generate 生成器
# 生成器与生成list的区别就是生成器是一种边循环边计算的机制
# 比如要有一个10万的列表 但是我们可能只需要其中的10个并且间隔特别大
# 这样就用generate在每次循环的时候去计算下次要取的值就要比直接在列表里查找要快捷省力的多
# 写法中的区别跟生成list的区别就是把[]换成()
# g = (x * x for x in range(10))
# 他的用法可以用next()方法去获取每一个元素 但是如果在最后没有了的话会报错
# 所以我们用for迭代的方式去获取
# for x in g:
#     print(x)
# 把普通的函数变成生成器
# def fab(max):
#     n,a,b = 0,0,1
#     while n < max:
#         print(b)
#         a,b=b,a+b
#         n = n+1
#     return 'done'
# print(fab(5))
# 注意这个赋值语句 相当于 t=（b,a +b)是一个tuple 然后把t[0]赋给a,t[1]赋给b
# 把函数改成生成器就把 print(b) 换成yield b
def fab(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b=b,a+b
        n = n+1
    return 'done'
# g = fab(5)
# print(next(g))
# 生成器的执行顺序与一般的函数不同 在执行next的时候遇到yield就返回
# 下次执行next的时候从上一次的yield的地方继续执行
# for x in fab(5):
#     print(x)
# 但是我们在使用for迭代的时候发现拿不到返回值done 这是因为返回值是在所有的yield都执行完成之后
# 最后一次next报错的时候放在StopIteration的value中的
# 所以我们要获取return的done的话就要捕获这个异常从value中取出
g = fab(6)
while True:
    try:
        x = next(g)
        print('g=',x)
    except StopIteration as e:
        print('genaerate return value:',e.value)
        break

