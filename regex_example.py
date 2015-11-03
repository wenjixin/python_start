# coding=utf-8
import re

print re.split(r'\s+', 'a b   c')
print re.split(r'[\s\,]+', 'a,b, c  d')
print re.split(r'[\s\,\;]+', 'a,b;; c  d')


m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')

# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符, 加个?就可以让\d+采用非贪婪匹配
print re.match(r'^(\d+)(0*)$', '102300').groups()
print re.match(r'^(\d+?)(0*)$', '102300').groups()

# 预编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
