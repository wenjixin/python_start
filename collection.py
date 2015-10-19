# coding=utf-8

# list can modify and  is order as insert
classmates = ['1', '', 2]
print classmates
print len(classmates)
print classmates[0]
print classmates[-1]

classmates.append(2)
classmates.append(['1', 2])
print classmates
print classmates[4][0]

# tuple
classmates = (1, '2', '4')
print classmates
print(1)
print(1,)

# tuple change, item cann not modify,but list is ok

classmates = (1, 2, [1, 3], (1, 2))
print classmates
classmates[2][1] = 10
print classmates
