# 偏函数
# 更方便的调用函数
# 比如我们做进制转换
# base参数是几就按照几进制转换
# print(int('0123',base=8))
# print(int('1237',base=8))
# print(int('1011',base=2))
# print(int('0x16',base=16))
# print(int('AB',16))
# 如果大量要转换二进制什么那么都要去填是几进制 那么我们可以去做一个函数
def int2(n):
    return int(n,base=2)
print(int2('101011'))
# 我们可以使用functool.partial来创建
# 他的作用就是把函数的某些参数固定住 特别是关键字参数
import functools
int2 = functools.partial(int,base=2)
print(int2('1011'))
# 他可以有三个参数 一个是函数对象，一个是可变参数，还有一个就是关键字参数
max2 = functools.partial(max,10)
# 其实这个是个可变函数把max中的对比序列加一个10在最开始的地方
print(max2(1,3,5))