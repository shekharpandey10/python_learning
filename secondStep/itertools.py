"""Eteratools: products,permutation,combinations,accumulate,groupby,and infinite iterators"""

from itertools import product
a=[1,2]
b=[3,4]

prod =product(a,b)
print(list(prod))
print()
print()
print()
from itertools import permutations
a=[1,2,3]
perm=permutations(a)
print(list(perm))

from itertools import combinations
a=[1,2,3,4]
print()
comb=combinations(a,3)
print(list(comb))

from itertools import accumulate
import operator
a=[1,2,3,4]
acc=accumulate(a,func=operator.mul)   #second argument is which operation i have to perform
print()
print(list(acc))

from itertools import groupby
a=[1,2,3,4,5]
# group_obj=groupby(a,key=)