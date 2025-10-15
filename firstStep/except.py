"""
Try/Exception
"""
string ="this is the string"
try:
    print(string[50])
except IndexError:    #Exception can be replace with IndexError
    print("sorry! your string is not long enought")