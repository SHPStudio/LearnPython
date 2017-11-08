# 匿名函数 也就是lambda表达式
# print(list(map(lambda x : x * x,[2,3,5,4,8,5,5])))
# 格式
# lambda x : x * x 前面是参数，后面跟着对参数的相应操作，也就是表达式
# 不过lambda只有一个表达式 该表达式的运算结果就是返回值
# lambda也可以作为一个函数来用或者被返回
# f = lambda x : x * x
# print(f(5))
def cal_pow(x,y):
    return lambda: x * x + y * y
print(cal_pow(1,3)())