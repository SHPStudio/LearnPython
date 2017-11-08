# IO
# IO相当于流 有两种一种是input一种是output
# input input相当于读取 把其他IO里的数据读取到内存中
# output output相当于写入 把内存中的数据写入到别的地方 比如网络磁盘
# 同步IO 同步IO指的是是一直等待 直到读完或者取完为止 cpu会一直保持阻塞状态
# 异步IO 就是不阻塞 让IO等等自己读完 读完之后再告诉cpu做其他的操作 在IO读取写入的时候cpu可以做其他事情
# 同步IO比异步IO要容易的多

# 读取文件
# 如果没有这个文件那么会报错误说没有这个文件路径
# 每次读取完之后要释放资源
# f = open('d:/test.txt','r')
# print(f.read())
# f.close()

# 正常的写法
# try:
#     f = open('d:/test.txt','r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# 但是每次那么写又有些太麻烦
# python引入了with语句来自动调用close()方法
# with open('d:/test.txt','r') as f:
#     print(f.read())

# read()方法读取是一次性读取 但是如果文件太大 可能会导致内存溢出
# 所以我们可以用read(size)循环的去读取
# 还有一种方法就是用readLine()
# with open('d:/test.txt','r') as f:
#     for line in f.readlines():
#         print(line.strip())

# file-like object
# 像open()方法返回的对象中带有read()函数的称为file-like对象
# 除了file之外 还有内存的字节流、网络、自定义流等等
# 并且他不要求必须要继承特定的类只有read()函数就可以了

# 读取二进制文件
# with open('d:/over.png','rb') as f:
#     print(f.read())

# 读取特定编码的文件
# with open('d:/gbk.txt','r',encoding='gbk') as f:
#     print(f.read())

# 如果文件编码有问题可能会导致错误那么我们可以忽略
# with open('d:/gbk.txt','r',encoding='iso 8859-1',errors='ignore') as f:
#     print(f.read())

# 写文件
# 写文件跟读文件差不多传入的标识符是w或者wb 表示写文本文件还是写二进制
with open('d:/text.txt','w') as f:
    print(f.write('mywrited233'))
with open('d:/text.txt','r') as f:
    print(f.read())
# 如果写入也需要特定编码就可以加上encoding就可以了