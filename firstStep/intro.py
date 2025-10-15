""""
hello how are you
"""

print('hello')
print()  #print the empty line
print(42)

"""
Variables
"""

_name="Sam"
name="shekhar"
name=33
print(name)

"""Data types

1->string
2->Integer (whole number)
3->float (decimal number)
4->boolean (one or the other)
5->List (set of elements)
6->Tuple
7->set  (set of unique value)
8->dictionary
"""
integer=33
text="this is a string"
decimal=33.4
boolean=False
my_list=[3,4,5,'a','g',33.4]
my_tuple=(1,2,3,4,'a','b','c')  # tuple is immutable -> can't change,update
my_set={1,2,2,2,4,3,4,'a','b'}  #only contains unique value
dictionary={   #it is a kind of hashmap
    "name":"Billy Bob",
    "age":14,
    "is_married":False,
    17:"seventeen",
    True:"one"
}

print(type(text))
print(type(integer))
print(type(decimal))
print(type(boolean))
print(type(my_list))
print(type(my_tuple))
print(type(my_set))
print(type(dictionary))
print(my_list)
print(dictionary["name"])
print(my_set)
