# WSGI接口定义
# def application(environ,start_response):
#     start_response('200 OK',[('Content-Type','text/html')])
#     return [b'<h1>hello web</h1>']

# environ
# 包含所有请求信息的请求头信息等等 他是一个dict对象

# start_response
# 请求响应函数 他有两个参数
# 一个参数是响应码 200 404 等等
# 第二个参数是一个list 表示header信息 每个header使用str和tuple表示

def application(environ,start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello,%s</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]