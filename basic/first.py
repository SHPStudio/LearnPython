# 输入 name = input()
# 输出 print('name', name)
# a = -100 赋值

# 如果以：为结尾的话那么就代表缩进的为代码块
# if a > 0:
#     print('大于0', a)
# else:
#     print('小于0', -a)

# 如果要转义的字符串特别的多 可以用r''去表示不要转义字符串
# print(r'/r/s/e')

# 使用'''...''' 来输出多行数据
# print('''shpshp2
#         shp3''')

# python代表Null是None

# python中的常量是全部大写的比如 PI=3.1415926

# 除法
# / 除法 就算是整除也是浮点数
# print(9/3)
# print(10/3)
#
# // 地板擦除 只保留整数
# print(10//3)

# 中文 python3使用的是unicode字符
# print('我的是')
# ord('A') ord是把字符转换为整数标识 chr()是把整数转换为字符
# print(ord('A'))
# print(chr(65))

# 字符的转码 比如如果要进行网络传输或者写入磁盘的话一般要把字符转换成字节byte流
# 把字符串转换成以字节为单位的bytes 每个字符只占一个字节 也就是ascii码
# x = b'abc'
# print(x)
# asc = 'ABC'.encode('ascii')
# unic = '中文'.encode('utf-8')
# asczh = '中文'.encode('ascii') # 如果用ascii码的话就会报错因为中文要占用两个字节
# print(unic)

# 字符的解码 从网络上获取到流或者从磁盘上获取到流需要对流进行解码
# bstream = b'\xe4\xb8\xad\xe6\x96\x87'
# dstream = bstream.decode('utf-8')
# print(dstream)

# 计算字符长度
# strLength = len('asdfadgadsg')
# print(strLength)
# 如果计算流的话就变成计算字节数了
# streamLength = len(b'sdfkljgwe')
# streamLengthZH = len('中文') # 2字符数
# streamLengthZh = len('中文'.encode('utf-8')) # 6字节数
# print(streamLengthZh)

# 避免乱码 因为python的源代码也是文本文件所以也需要进行编码的设置
# 在文件的开头加上
#!/usr/bin/env python3 # 这一行代表告诉Linux的操作系统这是python3的可执行文件
# -*- coding: utf-8 -*- # 告诉python解释器要用utf-8来编码

# 字符串格式化 就像c语言中的 %d %s
# %s 字符串
# %d 整数
# %x 十六进制数
# %f 浮点数
# 有几个%？ 就对应几个变量 如果只有一个%？ 那么就不需要写括号了  用% 来分割变量与要格式化的字符串
# print('hello %s my name is %s' % ('sunhaipeng','sunhaipeng2'))
# 整数可以用 %d %02d 0代表是否补0 2代表格式化的位数
# 浮点数也是一样 %.2
# 如果想要表示 30% 的 % 怎么办 那么就用 %% 来表示 %
# print('%2d-%03d' % (3,5))
# print('%.4f' % 3.03)
# print('%02d%%' % 3)

# list 列表 它是有序的 可以随便的添加和删除 用[]来表示
# customList = ['Mical','Mary','Jack']
# len(xx) 可以计算列表的长度
# print(len(customList))
# 可以和其他语言一样按照索引去访问列表中的元素 从0开始 如果超出索引范围会报错
# print(customList[0])
# print(customList[1])
# print(customList[2])
# print(customList[3])
# 索引为负数的时候表示按照倒序来访问 比如-1 代表访问倒数第一个元素 -2 -3 以此类推 注意倒序也有索引访问报错
# print(customList[-1])
# print(customList[-2])
# print(customList[-3])
# 往列表里添加元素用xxx.append('xxx')
# customList.append('NewOne')
# 指定位置添加xxx.insert(index,element)
# customList.insert(2,'newone')
# 删除末尾元素 使用pop()函数 还可以删除指定位置元素pop(index)
# print(customList.pop())
# 列表里可以添加列表也就可以来组成多维的列表
# customList.append(['imOk','imNotOk'])
# print(customList)
# 列表里的元素也可以为不同类型的元素
# customList.append(True)
# customList.append(123)
# customList.append(3.1546)
# print(customList)

# tuple 元组 用()表示 它与list区别就是他的元素是不可变的 同时它也没有insert等等的操作函数
# customTuple = (1,2,3)
# print(customTuple)
# 可变的元组 其实往元组里放入list 改变list中的值是可以的 只是不能修改元组的元素 改变元素的引用中的值是可以的
# 这也就变相改变了元组中的元素的值
# 能用tuple的地方就用tuple因为比较的安全

# 条件判断
# a = 28
# if a > 18:
#     print('大于18')
# elif a <= 18 & a > 9:
#     print('大于9小于18')
# else:
#     print('小于9')
# 用户输入判断 用户输入的都当做字符串来处理 所以和数字比较的时候需要做类型转化 用int()函数
# birth = input('birth:')
# birth = int(birth)
# if birth > 2000:
#     print('是00后')
# else:
#     print('00前')

# 循环迭代 使用 for item in collection:
# customList = ['Mical','Mary','Jack']
# for item in customList:
#     print(item)

# 生成数列 如果写一个从0到1000的数列手写的话太麻烦
# rang(number) 这个函数可以生成从0到number-1的整数数列 然后可以使用list() 把它转换成列表 这样就容易多了
# createList = list(range(101))
# sum = 0
# for item in createList:
#     sum += item
# print(sum)

# while 循环
# n = 99
# sum = 0
# while n > 0:
#     sum += n
#     n = n - 2
# print(sum)

# break 和 continue的用法和其他语言一样 break结束循环 continue结束当前循环

# 字典 dict 也就是其他语言的map 用{}表示 以键值对的形式 并且插入key的顺序跟存储顺序不一致 是无序的
# customDict = {'mical' : 95, 'mary' : 100, 'shp' : 101}
# print(customDict['shp'])
# key只准有一个 如果有重复的key 后面的会把前面的值冲掉 并且如果key没有那么会报错
# 可以直接给key赋值
# customDict['shp2'] = 123
# 如果防止没有key会报错可以提前检查一下字典里是否有key
# print('Toms' in customDict)
# 还有一种办法就是使用dict.get('xxx') 这种如果没有这个key的话就会返回一个None值
# print(customDict.get('Tomca'))
# 删除字典中的值dict.pop('xxx')
# customDict.pop('shp2')
# print(customDict)

# set 是一组key的集合 不存在重复的key 用set([])表示 set其实就是一个函数 他可以把相应的不可变集合转换成set 只要集合中有可变元素 那么就会报错
# customSet = set([1,2,3,5,4,2])
# print(customSet)
# 可以使用add(element)和remove(element) 去添加元素和删除元素
# customSet.add('56454')
# print(customSet)
# customSet.remove('56454')
# print(customSet)
# set可以理解为数学事实上的无序集合 可以对set进行交集和并集的操作
# firstSet = set([1,2,3,4])
# secondSet = set([2,3,5,6])
# print(firstSet & secondSet)  # 交集
# print(firstSet | secondSet)  # 并集
# set和dict一样 都不能放入可变的key  比如把list作为key的话就会报错