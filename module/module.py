# 模块
# 如果做一个比较大的工程的话那么就需要对庞大的代码进行管理
# 就可能需要划分模块 每个.py文件就可以作为一个模块
# import hello
# hello.test()
# 包的管理
# python中包和普通的文件夹很类似 所以需要在包的下面建立一个__init__.py的文件标记为当前文件夹是一个包
# 不过python有很多内置的模块比如sys就要注意不要引入重复的否则会被覆盖

# 作用域
# 正常的变量都是 xxx 相当于public变量
# 比如private的变量是_xx或者__xxx 这种相当于private的变量 但是不是说不能直接引用 是不应该引用
# 像 __name__ 这种是特殊的变量 可以被直接引用 但是一般是有特殊用途
# import pv_module
# pv_module.greeting('32')

# 安装第三方模块
# 安装第三方模块是使用pip模块管理 第三方库都会在Python官方的pypi.python.org网站注册
# 安装模块 pip install Pillow
# Pillow 图片处理库
# mysql-connector-python mysql链接驱动
# numpy 科学计算库
# Jinja2 生成文本工具库

# 模块路径模糊搜索
# 如果导入一个模块那么python会从一个路径列表去模糊搜索
import sys
print(sys.path)
# 我们还可以在这个路径里添加