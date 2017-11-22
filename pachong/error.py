# 爬虫还会遇到很多的错误
#URLError
# 这个错误的产生原因有以下几个
# 1.网络无连接 本地上不了网
# 2.连接不到特定服务器
# 3.服务器不存在
from urllib import request,response
# try:
#     request.urlopen('http://www.shpcoder.cn')
# except request.URLError as e:
#     print(e.reason)

# HTTPError
# 这个是比如遇见404 500 这种有关http状态码错误等等的可以捕捉这个错误
# 然后根据返回的状态码去进行下一步处理
# 301 重定向 处理方式是重定向header中的地址
# 302 重定向到临时的url地址中
try:
    req = request.urlopen('http://www.baidu.com')
    print(req.msg)
except request.HTTPError as e:
    print('%s:%s' % (e.code,e.reason))
