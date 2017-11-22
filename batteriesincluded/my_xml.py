# xml解析
# xml解析有两种方式 一种是dom把整个文件加载进内存随便加载任何东西
# sax是以一种流的形式边读边解析
# 一般使用sax模式

from xml.parsers.expat import ParserCreate
class DefaultSaxHandler(object):
    def start_element(self,name,attr):
        print('sax:start_Element:%s,attrs: %s' % (name,str(attr)))
    def end_element(self,name):
        print('sax:end_element:%s' % name)
    def char_data(self,text):
        print('sax:char_data:%s' % text)

xml1 = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parse = ParserCreate()
parse.StartElementHandler = handler.start_element
parse.EndElementHandler = handler.end_element
parse.CharacterDataHandler = handler.char_data
parse.Parse(xml1)