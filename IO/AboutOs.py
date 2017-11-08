# 操作系统有关操作
# os.name 操作系统类型 nt是windows posix是linux等等
import os
# print(os.name)
# os.uname 可以看到操作系统更详细的信息 不过在windows系统上不支持
# 也就是说os模块中的一些函数受操作系统的影响
# os.uname()

# 获取环境变量  os.environ
# print(os.environ)
# 获取某个环境变量os.environ.get('key')
# print(os.environ.get('path'))

# 操作文件和目录
# os.path.abspath('.') 查看当前路径的绝对路径
# print(os.path.abspath('.'))
# 创建新的文件夹
# 先拼接新的文件夹 使用os.path.join 这样可以保证兼容各个操作系统的文件夹间隔符
# newpath = os.path.join('d:/','testdir')
# 然后使用mkdir创建
# print(os.mkdir(newpath))
# 删掉文件夹
# print(os.rmdir(newpath))
# 分离字符串
# 同理如果要分离路径的话那么不要直接分离字符串
# 要使用os.path.split
print(os.path.split(os.path.abspath('.')))
# 使用os.path.splitext可以获取到文件的扩展名
print(os.path.splitext('d:/test.txt'))
# os.rename()重命名文件
# os.remove() 删除文件

# shutil模块是os模块的补充 提供了很多有用的函数