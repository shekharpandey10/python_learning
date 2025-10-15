"""sets: unordered,mutable, no duplicates"""

myset={1,2,3,5,4,6,7,7}  #does not allowed duplicates
set2=set([2,3,4,3,1,5,8,6])
print(myset)
print(set2)

myset.add(10)
myset.remove(4)
myset.discard(5)

myset.pop()    #return last ele and remove it
set2.clear() #clear the set
print(myset)


for i in myset:
    print(i)

odds={1,3,5,7,9}
evens={0,2,4,6,8}
primes={2,3,5,7}

u=odds.union(evens)
print(u)