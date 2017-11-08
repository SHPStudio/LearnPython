# 装饰器
# 在运行时动态的增加函数的功能比如在调用函数之前打个日志
# 拿到函数对象的名字 func.__name__
# 对函数进行包装 并以*args，**kws为通用参数
# def log(func):
#     def wraper(*args,**kws):
#         print('call %s' % func.__name__)
#         return func(*args,**kws)
#     return wraper
# @log 相当于 now = log(now())
# @log
# def now():
#     return '2017-11-03'
# print(now())
# 三次包装
# 比如我们要传入我们自定义的一些参数就需要在包装一层了
# def log(text):
#     def decorate(func):
#         def wraper(*args,**kw):
#             print('%s %s()' % (text,func.__name__))
#             return func(*args,**kw)
#         return wraper
#     return decorate
# @log('execute')
# def now():
#     return '2017-11-03'
# print(now())
# 解析
# 我们使用@log('execute') 先返回的decorate函数然后通过定义包装函数利用通用参数函数做相应的操作
# 返回我们要调用now()函数 然后返回wrapper
# 其实我们包装过的now现在指向的是wrapper函数通过执行wraper函数才能调用我们自己的函数
# print(now.__name__) # wraper
# 如果有需要原始方法签名的时候 那么我们就需要把原始的方法签名赋给wraper函数
# 我们可以使用@functools.wraps(func)来修改方法的签名
import functools
def log(text):
    def decorate(func):
        @functools.wraps(func)
        def wraper(*args,**kw):
            print('%s %s()' % (text,func.__name__))
            fs = func(*args,**kw)
            print('end call')
            return fs
        return wraper
    return decorate

@log('execute')
def now():
    print("sss")
now()
