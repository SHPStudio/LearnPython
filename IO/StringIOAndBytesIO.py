# StringIO
# 代表在内存中进行读取写入字符串 其实也就是在内存中做缓存 然后一块把缓存的数据用IO流发送出去等等
# from io import StringIO
# f = StringIO()
# f.write('Hello')
# f.write(' ')
# f.write('World')
# print(f.getvalue())
# 初始化读取
# from io import StringIO
# f = StringIO('Hello\nI\nLove\nYou')
# for line in f.readlines():
#     print(line.strip())

# BytesIO
# 操作二进制流
from io import BytesIO
# f = BytesIO()
# f.write('中文'.encode('utf-8'))
# print(f.getvalue())
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())