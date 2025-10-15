"""Dictionaries: kdy-value, unordered, mutable"""

mydict={   #define the  dictionary
    "name":"shekhar",
    "age":24,
    "city":"dehradun"
}
print(mydict)

mydict2=dict(name="rohit",age=27,city="garur")  #using dict keyword define
print(mydict2)
print(mydict2["name"])
mydict2["age"]=28 #mutable

# using del or popitem/pop method keyword i can delete the key 
del mydict["age"]
mydict2.popitem()
print(mydict)
print(mydict2)