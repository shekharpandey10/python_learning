"""
String formatting

"""

string="hello, world!"+" this is shekhar"
string2="hello, {name}"
print(string)
username="boss"
print(string2.format(name=username)) ## this assign the value to the string2 string name value
username="shekhar"
print(f"hello, {username}")


print(username.upper()) 
print(username.replace("shekhar","chandra shekhar").upper())  #mehod channing (still immutable)
print(username.title(),' this is the title')
print(username.count('sk'))
print((username.startswith('she')))
