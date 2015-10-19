# coding=utf-8
# condition stat
if True:
    print True


if not True:
    print 'Not hadppen'
else:
    print 'Yes'

age = 100
if age < 0:
    print 'negative'
elif age < 60:
    print u'不及格'
else:
    print 'ok'
if '1':
    print True

# while
names = ['1', 'afhsd']
for name in names:
    print name


for x in xrange(1, 100):
    print x

# while
sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n - 1
print sum

# dict && set

# dict key cannot modify,so list cannnot be a key
dict_example = {'1': 1, 1111: 1, (1, 2): (1, 2)}
print dict_example
dict_example['ccc'] = 'new'
print dict_example
print 'Not in' in dict_example
print dict_example.get((1, 2, 3), -1)
print dict_example.get((1, 2))

# set ,key not dup and key cannot modify
s = set([1, 2, 3, 1, 2, 3])
print s

# str cannot modify
a = ['c', 'a', 1]
a.sort()
print a
a = 'a nv c'
a.replace('a', 'A')

# tuple in dict,if tuple has muta
dict_example = {(1, 2, [1, 2]): 1}

print dict_example
