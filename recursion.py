#Countdown
def countdown(number):
    if number == 0:
        print("Done!")
        return

    print(number)
    countdown(number - 1)


countdown(5)

#Factorial
def factorial(number):
    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


print(factorial(5))

#Fibonacci
def fibonacci(number):
    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(6))

#Improving recursion with memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(number):
    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(40))
