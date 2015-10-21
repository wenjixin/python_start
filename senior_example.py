# coding=utf-8

a_list = ['abc', 'def', 'ddd']

print a_list[0:3]
print a_list[-3:]
print a_list[-3:-1]
print a_list[-3:2]

a_tuple = (1, 2, 3, 4, 5)

# 前2个
print a_tuple[:2]
# 后两个
print a_tuple[-2:]
# 前5个，每个2个取一个
print a_tuple[:5:2]
# copy
print a_tuple[:]

"""
    字符串'xxx'或Unicode字符串u'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
    在很多编程语言中，针对字符串提供了很多各种截取函数，其实目的就是对字符串切片。Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单。
"""
print u'xxx'[:]

# iteration
a_dict = {'1': 1, 'c': 's'}
for key in a_dict:
    print key


for k, v in a_dict.iteritems():
    print k, v


from collections import Iterable
print isinstance('abc', Iterable)
print isinstance(123, Iterable)

# need index

for index, value in enumerate((1, 2, 3)):
    print index, value


for x, y in [(1, 2)]:
    print x, y

"""
   list builder
"""
print range(1, 200, 3)
print[x * x for x in range(1, 11)]
print[x * x for x in range(1, 11) if x % 3 == 0]
print[m + n for m in 'abc' for n in 'xyz']
import os
print[d for d in os.listdir('.')]

L = ['Hello', 'World', 19, 'IBM', 'Apple']
print[s.lower() if isinstance(s, str) else s for s in L]


"""
    通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器（Generator）。

"""
L = [x * x for x in range(10)]
print L
g = (x * x for x in range(10))
print g
for n in g:
    print n


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1


def fib_g(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
for n in fib_g(10):
    print n

"""
    map && reduce
"""


def char2int(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
            '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2int, s))


print str2int('1234567')


names = ['adam', 'LISA', 'barT']

print map(lambda x: x.capitalize(), names)


def prod(L):
    return reduce(lambda x, y: x * y, L)
print prod([100])


"""
    filter
"""

print filter(lambda x: len(x) == 5, names)


"""
    sorted
"""


def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0


print sorted(names, cmp_ignore_case)

"""
    funcation is a return value
"""


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(*[1, 2, 3])
print f
print f()

# so we can have a closures,note that i can change.

"""
全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
"""


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1, f2, f3 = count()

print f1(), f2(), f3()


def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j
            return g
        fs.append(f(i))
    return fs
f1, f2, f3 = count()

print f1(), f2(), f3()

"""
    lambda limit:匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
"""

"""
装饰模式
"""


def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper


@log
def now():
    print '2013-12-25'

now()

# same as @log


def now_1():
    print '2013-12-25'
log(now_1)()


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator


@log("hello")
def now():
    print '2013-12-25'

now()

print now.__name__


import functools


def log_next(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper


@log_next
def now():
    print '2013-12-25'

now()

print now.__name__


import functools


def log_second(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator


@log_second('ccc')
def now():
    print '2013-12-25'

now()

print now.__name__


import functools


# TODO ,dynamic func
def log_second(args_text):
    print 'args_text:', args_text

    if callable(args_text) == True:
        print 'hello'

        @functools.wraps(args_text)
        def wrapper(*args, **kw):
            print 'call %s():' % args_text.__name__
            return args_text(*args, **kw)
        return wrapper

    else:

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print '%s %s():' % (args_text, func.__name__)
                return func(*args, **kw)
            return wrapper
        return decorator


@log_second('ccc')
def now():
    print '2013-12-25'

now()


@log_second
def now():
    print '2013-12-25'
now()


"""
    偏函数,简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
"""


import functools
int10 = functools.partial(int, base=10)
print int10('1234567')
print int10('1000000', base=8)


max2 = functools.partial(max, 10)
print max2(5, 6, 7)
