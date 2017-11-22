# 做web项目
# 使用wsgI来做统一接口服务
# 通过wsgI来处理用户的请求并做相应的回应
from wsgiref.simple_server import make_server
from helloweb import application

httpd = make_server('',8080, application)
print('Server is listening 8080...')
httpd.serve_forever()