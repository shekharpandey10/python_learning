"""Lists: Ordered,mutable,allows duplicate elements"""

myList=["banana","apple","cherry"]
print(myList)
item=myList[1]
print(item)
# myList=[]        #mutable 
# print(myList)

for I in myList:   #iterate the list
    print(I)

if "banana" in myList:   #check the element present in the list.
    print("yes")
else:
    print('no')

print(len(myList)) #length of the list
myList.append("mango")   #append the ele at end of the lise
print(myList)

myList.insert(1,"blueberry")  #inset the ele in the perticuler index then the existing index element goes to the next index.
print(myList)

myList.pop()  #remove the last index from the list.
print(myList)

myList.reverse() #reverse the list
print(myList)

myList.sort() #sort the list
print(myList)

newList=sorted(myList)   #return sorted list
print(newList,"new list")
myList.clear() #clear the whole list and give the empty list
print(myList)


secondList=[0]*5   #return the length of list with zero element
print(secondList)

myList=newList+secondList   # append the list
print(myList)

a=myList[1:5]  #slice the list
print(a)

a=myList[::2]  #skip the every given item
print(a)

list_org=["banana","cherry","apple","aalo"]

list_copy=list_org  #copy the ref address only shallow copy
# list_copy.append("kela")
list_copy=list_org.copy()  #now its the deep copy
list_copy.append("kela")
print(list_copy)
print(list_org)\


a=[1,2,3,4,5,6]
b=[i*i for i in a]
print(b)