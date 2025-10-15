"""Ordered,immutable, allows duplicate elements"""

myTuple=tuple([2,3,4])   #define using tuple keyword
second=(2,3,4,4,5,6)   #without tuple keyword
print(type (second))
print(myTuple[2])


for x in myTuple:
    print(x)

#unpacking
my_tuple="max",33,"boston"
name,age,city=my_tuple   #distracture the elements
 
print(name)
print(age)
print(city)


#another way
it,*it2,it3=my_tuple
print(it)   #first ele
print(it2) #in between ele as a list
print(it3)   #last ele

ml=[1,2,3,4,5]
mt=(1,2,3,4,5)
import sys
print("LIST byts are ",sys.getsizeof(ml))
print("TUPLE byts are ",sys.getsizeof(mt))   #tuple is more optimse via space and time