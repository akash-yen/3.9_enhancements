from collections import OrderedDict
d = OrderedDict()

d[100] = 'sunny'
d[200] = 'bunny'
d[300] = 'cunny'
d[400] = 'vunny'

for k,v in d.items():
    print(k,'--->',v)

# From 3.7 insetion order is preserved in dict as well

# reversed()

l = [1,2,3,4]
l2 = reversed(l)
print(list(l2))

t = (1,2,3,4)
t2 = reversed(t)
print(tuple(t2))

#reversed not applicable for set and dict u can use d.keys() and reverse in 3.7

# From 3.8 version we can apply reversed for dict as well


d = {100 : 'Sunny' , 200: 'Bunny' , 300: 'Junny'}
r = reversed(d)
print(r)
for k in r:
    print(k,'-->',d[k])

# 3.9 Enhancements

d1 = {100 : 'Sunny' , 200: 'Bunny' , 300: 'Junny'}
d2 = {300 : 'xunny' , 400: 'cunny' , 500: 'vunny'}

# merging operations
d3 = {**d1,**d2}

print(d3)

#or

d3 = d1.copy()
for k,v in d2.items():
    d3[k] = v
print(d3)

# in python 3.9 onwards just a simple | operetor

d4 = d1 | d2
print(d4)


# how to update an existing dict with items of another dict

d1.update(d2)
print(d1) # {100: 'Sunny', 200: 'Bunny', 300: 'xunny', 400: 'cunny', 500: 'vunny'}
print(d2) # {300: 'xunny', 400: 'cunny', 500: 'vunny'}

# from 3.9 it is

d1 |= d2