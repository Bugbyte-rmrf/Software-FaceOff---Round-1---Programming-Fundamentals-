#Even and Odd Numbers
number = int(input("Enter a whole number: "))

if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")

#Division by zero
denominator = 0

if denominator == 0:
    print("Cannot divide by zero.")
else:
    print(10 / denominator)

#Comparison
age = 20

print(age >= 18)  
print(age == 20)  
print(age != 20)  

#Logical operators
age = 22
has_id = True

print(age >= 18 and has_id)  
print(age < 18 or has_id)    
print(not has_id)





