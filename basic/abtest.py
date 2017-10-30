# 自定义的函数文件


# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x

# 给函数添加错误提示
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operated type')
    if x >= 0:
        return x
    else:
        return -x