# 高级部分
# 切片
# 比如有一个列表，我只想取第5个到第105个怎么办呢 这就可以使用python的切片功能了
# L = list(range(200))
# print(L[5:106])
# X:X 前一个代表起始位置 后一个代表结束位置但是不包括这个位置 5:106 其实就是5-105
# 如果:X 省略前面的起始位置代表就是从0开始 X: 省略后面的就是到结束 同时他也支持倒序的
# print(L[-10:])
# X:X:X 最后这个代表隔多少个取一次
# print(L[:10:2])
# 同样的 tuple也可以切片 还有字符串就相当于substring了
# print("abcd"[1:3])

# 迭代 也就是遍历
# for n in xxx 的形式
# 列表 tuple 字符串 甚至是dict都可以迭代
# my_dict = {'one':1,'two':2,'three':3}
# for key in my_dict:
#     print(key)
# for ch in 'ABCDE':
#     print(ch)
# 判断是否可以用迭代
# from collections import Iterable
# print(isinstance('abc',Iterable))
# print(isinstance([1,2,3,5],Iterable))
# print(isinstance(15454,Iterable))
# 如果想用index-element的形式取值怎么办 使用enumerate函数把列表转换成这种形式
# for x,y in enumerate([5,1,5,6,4]):
#     print(x,y)
# 元素中有多个值也可以迭代
for (x,y) in [(1,2),(3,4),(6,7)]:
    print(x,y)
