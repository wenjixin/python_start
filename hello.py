# coding=utf-8

"""
hello world.

@author: tongwei

@date: 2015/10/19

"""
print 'hello world.'

print 'this is a day', 100 + 100

# input
# name = raw_input()
# print name

# datatype && varible
# integer
integer_value = 100
# float
float_value = 1.100
# str
print 'I\'m tongwei.'
print r'\\\\\\'
print r"""hello .
    \\\this is a article."""
print True
print False
print(True and False)
print(True or False)
result = not True
print result, 100
print "end"
print None
print 100 / 3
print 100 / 3.0

print ord('A')
print chr(65)

print '中文', '?'
print u'中文'
print u'\u4e2d'
print u'\\u4e2d'

# in memory is unicode. out can encode to utf-8,you can see in
# http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819196283586a37629844456ca7e5a7faa9b94ee8000
u'中文'.encode('utf-8')
print len('ABC')
print len(u'ABC')
print len('中文')
print len(u'中文')
print len('\xe4\xb8\xad\xe6\x96\x87')
# decode utf-8 into unicode
print 'abc'.decode('utf-8')
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')


# format you str
"""
    %d %f %s %x
"""
print 'Hello,%s' % 'world'

print 'Hello,%s,%s' % ('1', '2')
print '%2d-%02d' % (3, 1)
print '%.2f' % 3.1415926
