# 异常处理
# try:
#     print('try...')
#     r = 10 / 0
#     print('result',r)
# except ZeroDivisionError as e:
#     print('except:',e)
# finally:
#     print('finally...')
# print('End')
# 可以捕获多个异常如果没有异常可以加一个else代表没有捕获到异常
# try:
#     print('try...')
#     r = 10/int('a')
#     print('result:',r)
# except ZeroDivisionError as e:
#     print('except:',e)
# except ValueError as e:
#     print('value error',e)
# else:
#     print('no error')
# finally:
#     print('finally')
# print('end')
# 捕获异常时需要注意 如果第一个异常类型是第二个异常类型的父类，那么永远也捕获不到第二个异常

# 抛出异常
# 很多时候需要我们自己去抛异常
# class FooError(ValueError):
#     pass
# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError('param is zero')
#     return 10 / n
# def main():
#     print(foo('0'))
# main()

# 还有我们应该记录一下错误的日志 这样我们就比较容易判定错误
# 记录使用logging.exception
import logging
class FooError(ValueError):
    pass
def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('param is zero')
    return 10 / n
def main():
    try:
        print(foo('0'))
    except FooError as e:
        logging.exception(e)
    print('end')
main()
print('finall end')
