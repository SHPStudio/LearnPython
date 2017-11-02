# 返回是函数
# 求和
# def cal_sum(*args):
#     def sum():
#         ax = 0
#         for x in args:
#             ax = ax + x
#         return ax
#     return sum
# f = cal_sum(1,2,3,4,5,6)
# print(f())
# 闭包
# 闭包指的是外部函数里定义了内部函数，重要的操作和变量都存在在内部函数中，并且
# 内部函数可以操作外部函数里的变量并且外部函数返回内部函数的时候相关的变量和参数都放在内部函数中
# 他的好处就是对内部操作进行封装
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1,f2 = count()
print(f1())