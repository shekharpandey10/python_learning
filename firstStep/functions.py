"""
functions
"""
name="rox"
age=40
statement=f"this is the ,{name}"
print(statement)


def greeting(name,age):
    greeting=f"Hello i am {name}. i am {age}"
    print(greeting)
    return greeting

greeting('rox',20)
greeting('monty',30)