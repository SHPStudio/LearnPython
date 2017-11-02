# 迭代器
# Iterator 可以使用next()不断获取值的对象 并且可以使用isinstance()判断对象是否是迭代器
# Iterable 是可以使用for迭代去获取值的对象 叫可迭代对象但并不一定是Iterator
# 比如generater生成器一定是迭代器对象 list tuple set等等可能就不是迭代器对象
# 但是他们可以使用iter()变为迭代器对象
from collections import Iterable,Iterator
print(isinstance('adfa',Iterable))
print(isinstance([1,1,2,3],Iterable))
print(isinstance((1,1,2,3),Iterable))
print(isinstance((1,1,2,3),Iterator))
print(isinstance([1,1,2,3],Iterator))
print(isinstance(iter([1,1,2,3]),Iterator))
# 为什么list tuple等等不是interator对象
# 因为像迭代器这种通过next()获取数据直到报错表示没有数据
# 也就是说他是一种懒加载数据的方式，并不知道什么时候才是头
# 也就是相当于无限数据流Interator可以存储无穷自然数 但是list这种不就可能了