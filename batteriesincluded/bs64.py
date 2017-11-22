# base64
# base64是把任意的二进制数据编码为64个字符串的形式
# 在url或者cookie中用的比较广泛
# 原理就是base64是一个包含64字符的集合
# 我们先把二进制的字节进行分组按照6bit为一组正好对应了64个字符的索引
# 所以我们可以把没6bit的二进制转换成一个字节的字符
import base64
print(base64.b64encode(b'binctsString'))
# 如果缺字节 那么我们可以用\x00在末尾补充字节 这样在编码的最后会加==
print(base64.b64decode(b'YmluY3RzU3RyaW5n'))
# 由于转码后的base可能会带有+/等url中容易产生歧义的字符
# 所以有专门针对url编码的字符组合 把+/替换成_等等不产生歧义的字符
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode(b'abcd--__'))