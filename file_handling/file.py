
""" read the file"""
file =open('./a.txt')
print(file.read())
print(type(file))

#read the first line

first_line=file.readlines()
print(first_line)
file.close()


with open('a.txt','a') as f:  #append
    f.write('this is appeded line \n')
    

with open('a.txt','w') as f:
    f.write('Updated written content \n')


import os  #remove the file
if os.path.exists('./b.txt'):
    os.remove('./a.txt')
else:
    print('this file doesnt exists')