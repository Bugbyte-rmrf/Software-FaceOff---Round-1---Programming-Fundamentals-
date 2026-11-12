#Local variable
def greet():
    message = "Hello!"
    print(message)

greet()

#Global variable
name = "Alex"

def greet():
    print("Hello", name)

greet()

#shadowing
name = "Alex"

def greet():
    name = "Jordan"
    print(name)

greet()

print(name)



