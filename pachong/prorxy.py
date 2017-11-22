# 使用代理
# 因为在使用爬虫的时候可能有的网站你一个ip访问很多次就不让访问了
# 所以我们可以使用代理池 可以使用代理的ip去访问
from urllib import request
proxy_handler = request.ProxyHandler({'http':'http://112.25.41.136:80'})
opener = request.build_opener(proxy_handler)
request.install_opener(opener)
with request.urlopen('http://www.baidu.com') as res:
    print('Status:', res.status, res.reason)
    for k, v in res.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', res.read().decode('utf-8'))