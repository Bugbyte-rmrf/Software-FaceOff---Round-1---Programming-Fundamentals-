#def function
def greet():
    print("Hello!")

greet()

# name is a parameter
def greet(name):  
    print("Hello", name)

# "Alex" is an argument
greet("Alex")     

#Return values
def add(a, b):
    return a + b

result = add(10, 5)

print(result)

# Give parameter a default value
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Alex")

#side effects
numbers = [1, 2, 3]

def add_number(items):
    items.append(4)

add_number(numbers)

print(numbers)
