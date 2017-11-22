# get请求
# from urllib import request,parse
# url = 'http://www.baidu.com/s'
# data = {
#     'wd': '宁哥的小站'
# }
# data = parse.urlencode(data)
# fullurl = url + '?' + data
# print(fullurl)
# with request.urlopen(fullurl) as res:
#     print(res.read())


# post请求
from urllib import request,parse
urlData = parse.urlencode([
    ('USERNAME','141501140216'),
    ('PASSWORD','141501140216'),
    ('RANDOMCODE','zbnm'),
    ('useDogCode',None),
    ('useDogCode',None),
    ('x','52'),
    ('y','5')
])
url = request.Request('http://jwgl.nepu.edu.cn/Logon.do?method=logon')
url.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)')
url.add_header('Origin','http://jwgl.nepu.edu.cn')
url.add_header('Referer','http://jwgl.nepu.edu.cn/')
url.add_header('Cookie','JSESSIONID=90F09DE0D05CF5EE469BB8151430B455')
temp = False
with request.urlopen(url,urlData.encode('utf-8')) as res:
    print('Status:', res.status, res.reason)
    for k, v in res.getheaders():
        print('%s: %s' % (k, v))
        if k == 'Transfer-Encoding':
            temp = True
    if temp==True:
        print('登录成功')
        print(res.read().decode('utf-8'))
    else:
        print('登录失败')

url2 = request.Request('http://jwgl.nepu.edu.cn/xszqcjglAction.do?method=queryxscj')
url2.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)')
url2.add_header('Host','jwgl.nepu.edu.cn')
url2.add_header('Referer','http://jwgl.nepu.edu.cn/jiaowu/cjgl/xszq/query_xscj.jsp?tktime=1511321466000')
url2.add_header('Cookie','JSESSIONID=90F09DE0D05CF5EE469BB8151430B455')
queryScoreData = parse.urlencode([
    ('xsfs','qbcj')
])
if temp:
    with request.urlopen(url2,queryScoreData.encode('utf-8')) as res:
        print(res.read().decode('utf-8'))
