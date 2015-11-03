# coding=utf-8
import base64
import struct
import hashlib
import itertools

print base64.b64encode('binary\x00string')
print base64.b64decode('YmluYXJ5AHN0cmluZw==')
print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.urlsafe_b64decode('abcd--__')

# Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
print struct.pack('>I', 10240099)
print struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')


md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()


md5 = hashlib.md5()
md5.update('how to use md5 in ')
md5.update('python hashlib?')
print md5.hexdigest()


sha1 = hashlib.sha1()
sha1.update('how to use sha1 in ')
sha1.update('python hashlib?')
print sha1.hexdigest()


# 如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。


natuals = itertools.count(1)
# for n in natuals:
#     print n
cs = itertools.cycle('ABC')
ns = itertools.repeat('A', 10)

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)


for c in itertools.chain('ABC', 'XYZ'):
    print c


for key, group in itertools.groupby('AAABBBCCAAA'):
    print key, list(group)

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print key, list(group)


"""imap() 无穷序列  ifilter()无穷序列"""


"""xml operation"""
from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):

    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)
xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)


L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append('some & data')
L.append(r'</root>')
print ''.join(L)


"""HtmlParser"""
from HTMLParser import HTMLParser

import htmlentitydefs


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print('data')

    def handle_comment(self, data):
        print('<!-- -->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed(
    '<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')
