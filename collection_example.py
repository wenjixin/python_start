# coding=utf-8
from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter


Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print p

Circle = namedtuple('Circle', ['x', 'y', 'r'])

q = deque(['a', 'b', 'c'])
print q


dd = defaultdict(lambda: 'N/A')
print dd['key2']


od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print od

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print c
