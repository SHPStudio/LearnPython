# cookie
# cookie中保存了这种有关登录信息等等的东西
# 所以我们可以使用cookie去模拟登录或者登录后访问其他页面

# 把访问的时候cookie放到文件中
# from urllib import request,parse
# from http import cookiejar
# filename = 'cookie.txt'
# cookie_jar = cookiejar.MozillaCookieJar(filename)
# handler = request.HTTPCookieProcessor(cookie_jar)
# opener = request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie_jar.save(ignore_discard=True, ignore_expires=True)
# ignore_discard表示cookie就算被丢弃也保存下来
# ignore_expires表示如果文件存在那么就覆盖写入

# 从文件中读取cookie去访问网站
from urllib import request
from http import cookiejar

cookie = cookiejar.MozillaCookieJar()
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
req = request.Request('http://www.baidu.com')
opener = request.build_opener(request.HTTPCookieProcessor(cookie))
res = opener.open(req)
print(res.read().decode('utf-8'))