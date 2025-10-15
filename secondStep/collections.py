"""collections: couter,namedtuple,ordereddict,defaultdice,deque"""

from collections import Counter
from collections import namedtuple

a="afabbbbffffcccc"  
my_counter=Counter(a)    #counter data structure
print(my_counter)   #-> Counter({'f': 5, 'b': 4, 'c': 4, 'a': 2})
print(my_counter.keys())   #keys
print(my_counter.values()) #values
print(my_counter.most_common())


Point=namedtuple('Point','x,y')
pt=Point(1,-4)
print(pt.x,pt.y)


from collections import OrderedDict
ordered_dict=OrderedDict()  #it keep store element by the assignment order
ordered_dict['a']=1
ordered_dict['b']=2
ordered_dict['c']=5
ordered_dict['d']=4
print(ordered_dict)

from collections import defaultdict
d=defaultdict(int)   #default dictionary
d['a']=1
d['b']=2

print(d['a'])
print(d['c'])  #default type(whatever the type) value return here ->0

from collections import deque
d=deque()
d.append(1)
d.append(2)
d.append(2)
d.append(1)
d.appendleft(50)

print(d)
d.pop()
print(d)
d.extend([4,56])
print(d)