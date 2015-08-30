from collections import Counter
from collections import namedtuple

'''
a subclass of dict
'''
c = Counter('which')

# tally
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
  cnt[word] += 1
print(cnt)
print(cnt['red']) # 2

cnt = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(cnt['red']) # 2 

cnt = Counter(('red', 'blue', 'red', 'green', 'blue', 'blue'))
print(cnt['red']) # 2 

# update 
c = Counter('which')
c.update('witch')
d = Counter('watch')
c.update(d)
print c['h']  # 4 h's

# make a named tuple class
Point = namedtuple('Location', ['x', 'y'])

p = Point(11, y=22)
print(p[0], p[1])
print(p.x, p.y)
print(p)
print(p._replace(x=33))
print(p._fields)


d =  dict(x=22, y=11)
Point(**d)  # unpack the dictionary


