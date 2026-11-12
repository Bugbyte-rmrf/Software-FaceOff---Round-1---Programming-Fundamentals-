#Strings
word = "PYTHON"

print(word[0])  
print(word[1])  
print(word[2]) 
print(word[-1])
print(word[-2])

#Slicing
word = "PYTHON"

print(word[0:3])
print(word[2:])
print(word[:4]) 

# Strings are Immutable
word = "PYTHON"
word[0] = "J"

word = "PYTHON"
word = "J" + word[1:]

print(word)

#Common string operations
text = "  Hello World  "

print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("World", "Python"))
print(text.split())

#String formatting using f-strings
name = "Alex"
age = 25

print(f"My name is {name} and I am {age} years old.")





