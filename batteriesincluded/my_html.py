# 解析Html
# html不想xml那么严格所以不怎么容易使用xml那一套去解析
from html.parser import HTMLParser
class MyHtmlParse(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s> attr: %s' % (tag,str(attrs)))

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parse = MyHtmlParse()
hm ='''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>'''
parse.feed(hm)