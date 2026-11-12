#Lists
numbers = [10, 20, 30]

numbers.append(40)
numbers.remove(20)

print(numbers)

#Stacks - Last In, First Out
stack = []

stack.append("A")
stack.append("B")
stack.append("C")

print(stack.pop()) 
print(stack.pop()) 
print(stack.pop())

#Queues
from collections import deque
queue = deque()

queue.append("A")
queue.append("B")
queue.append("C")

print(queue.popleft())  
print(queue.popleft())
print(queue.popleft())

#Dictionaries
student = {
    "name": "Alex",
    "age": 25,
    "course": "Software Engineering"
}

print(student["name"])

#Sets
numbers = {1, 2, 2, 3, 3, 4}

print(numbers)

students_a = {"Alex", "Jordan", "Sam"}
students_b = {"Sam", "Taylor", "Alex"}

print(students_a & students_b)
print(students_a | students_b)
print(students_a - students_b)



  

