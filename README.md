# Software Engineering Face-Off --- Round 1

## Section 3: Programming Fundamentals (Python)

> A comprehensive study guide and practical reference covering the big
> picture through Object-Oriented Programming.\
> Environment: Python 3, Visual Studio Code, Ubuntu/Linux terminal.

------------------------------------------------------------------------

## Table of Contents

1.  [Understanding the Big Picture](#1-understanding-the-big-picture)
2.  [Values and Data Types](#2-values-and-data-types)
3.  [Variables and Scope](#3-variables-and-scope)
4.  [Functions and Parameters](#4-functions-and-parameters)
5.  [Strings](#5-strings)
6.  [Data Structures](#6-data-structures)
7.  [Big O Notation](#7-big-o-notation)
8.  [Recursion](#8-recursion)
9.  [How Code Runs](#9-how-code-runs)
10. [Object-Oriented Programming](#10-object-oriented-programming)
11. [Face-Off Revision Checklist](#12-face-off-revision-checklist)
12. [Common Errors and Debugging](#13-common-errors-and-debugging)
14. [Glossary](#14-glossary)

------------------------------------------------------------------------

# 1. Understanding the Big Picture

Programming is the process of giving a computer precise instructions to
perform a task. A program receives or accesses data, processes it
according to rules, and produces a result.

Programming terms:

1.  **Input** --- data enters the program.
2.  **State** --- the program stores information in variables and data
    structures.
3.  **Processing** --- expressions, operators and functions transform or
    inspect the data.
4.  **Decisions** --- conditions determine which instructions should
    run.
5.  **Repetition** --- loops or recursion repeat work.
6.  **Output** --- the program displays, saves, returns or transmits a
    result.

------------------------------------------------------------------------

# 2. Values and Data Types

## 2.1 What is a value?

A **value** is a piece of data a program can work with. Examples
include:

``` python
25
3.14
True
"Hello"
2 + 3j
```

A **data type** classifies a value and determines the kinds of
operations that make sense for it.

The type belongs to the object, and a
name can later refer to an object of a different type.

``` python
value = 100
print(type(value))  # <class 'int'>

value = "Hello"
print(type(value))  # <class 'str'>

value = 5.5
print(type(value))  # <class 'float'>
```

## 2.2 Common Python built-in types


Inspect types using `type()`:

``` python
age = 24
height = 1.75
is_student = True
name = "Alex"
complex_number = 2 + 3j

print(type(age))
print(type(height))
print(type(is_student))
print(type(name))
print(type(complex_number))
```


## 2.3 Type conversion (type casting)

Type conversion changes a value from one type to another when the
conversion is valid.

``` python
age_text = "25"
age_number = int(age_text)

print(age_number + 5)  # 30
```

Common conversions:

``` python
int("25")       # 25
float("3.14")   # 3.14
str(100)        # "100"
bool(1)         # True
```

Not every conversion is valid:

``` python
int("hello")    # Raises ValueError
```


## 2.4 Arithmetic operators

### True division and floor division

Python's `/` performs true division:

``` python
print(7 / 2)  # 3.5
```

Python's `//` performs floor division: it rounds the quotient down
toward negative infinity.

``` python
print(7 // 2)    # 3
print(-7 // 2)   # -4
```

Do not describe `//` as simply "remove the decimal part"; that would be
incorrect for negative values.

### Modulo

The modulo operator `%` gives the remainder according to Python's
division rule:

``` python
print(17 % 5)  # 2
print(10 % 3)  # 1
print(8 % 2)   # 0
```

A common use is checking whether a number is even or odd:

``` python
number = 17

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

-   If `number % 2 == 0`, the number is even.
-   Otherwise, it is odd.

### Division by zero

Python raises an exception when dividing by zero:

Handle a possible zero divisor explicitly:

``` python
denominator = 0

if denominator == 0:
    print("Cannot divide by zero.")
else:
    print(10 / denominator)
```

Or use exception handling:

``` python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

## 2.5 Comparison and logical operators

Comparison operators produce Boolean values:

  Operator   Meaning
  ---------- --------------------------
  `==`- Equal to

  `!=` - Not equal to

  `>` - Greater than

  `<` - Less than

  `>=` - Greater than or equal to

  `<=` - Less than or equal to

``` python
age = 20

print(age >= 18)  # True
print(age == 20)  # True
print(age != 20)  # False
```

Logical operators combine conditions:

``` python
age = 22
has_id = True

print(age >= 18 and has_id)  # True
print(age < 18 or has_id)    # True
print(not has_id)            # False
```

-   `and` is true when both conditions are true.
-   `or` is true when at least one condition is true.
-   `not` reverses a Boolean value.

## 2.6 Practical: `02_even_odd.py`

Create a file named `02_even_odd.py` in VS Code:

``` python
# 02_even_odd.py

number = int(input("Enter a whole number: "))

if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")
```

Run it from the terminal:

``` bash
python3 02_even_odd.py
```

Example:

``` text
Enter a whole number: 17
17 is odd.
```

``` text
Enter a whole number: 24
24 is even.
```

This exercise combines input, conversion, variables, modulo, conditions
and output.

------------------------------------------------------------------------

# 3. Variables and Scope

## 3.1 What is a variable?

A variable is a name that refers to an object. It gives a program a
readable way to access a value.

``` python
name = "Alex"
age = 25
```

A variable is also a label or reference, not a physical box containing the value.

## 3.2 What is scope?

**Scope** determines where a name can be accessed in a program.

### Local scope

A variable assigned inside a function is normally local to that
function:

``` python
def greet():
    message = "Hello!"
    print(message)

greet()
```

Trying to access `message` outside the function causes a `NameError`:

``` python
def greet():
    message = "Hello!"

greet()
print(message)  # NameError
```

### Global scope

A name assigned at module level is global to that module:

``` python
name = "Alex"

def greet():
    print("Hello", name)

greet()
```

### Shadowing

**Shadowing** occurs when a name in an inner scope has the same name as a
name in an outer scope:

``` python
name = "Alex"

def greet():
    name = "Jordan"
    print(name)

greet()
print(name)
```

Output:

``` text
Jordan
Alex
```

Inside `greet()`, the local `name` is used. The global `name` remains
unchanged.

## 3.3 Python's LEGB name-resolution rule

When Python resolves a name inside a function, it searches these scopes
in order:

1.  **L --- Local:** The current function.
2.  **E --- Enclosing:** Any enclosing function scope.
3.  **G --- Global:** The module's global scope.
4.  **B --- Built-in:** Python's built-in names, such as `print`, `len`
    and `range`.

Example:

``` python
name = "Global"

def outer():
    name = "Enclosing"

    def inner():
        name = "Local"
        print(name)

    inner()

outer()
```

Output:

``` text
Local
```

The local name is found first.


------------------------------------------------------------------------

# 4. Functions and Parameters

## 4.1 What is a function?

A function is a reusable block of code that performs a task. Functions
help organize programs, reduce repetition and make code easier to test.

``` python
def greet():
    print("Hello!")

greet()
```

-   `def` begins a function definition.
-   `greet` is the function name.
-   `Parentheses` contain parameters, if any.
-   The `indented block` is the function body.
-   `greet()` calls the function.

## 4.2 Parameters versus arguments

A **parameter** is a name in a function definition. An **argument** is a
value supplied when the function is called.

``` python
def greet(name):       # name is a parameter
    print("Hello", name)

greet("Alex")          # "Alex" is an argument
```

Functions can accept more than one parameter:

``` python
def add(a, b):
    return a + b

print(add(10, 5))  # 15
```

## 4.3 Return values

`return` sends a value back to the caller and ends the current function
call.

``` python
def add(a, b):
    return a + b

result = add(10, 5)
print(result)  # 15
```

Do not confuse `return` with `print()`:

-   `print()` displays information.
-   `return` gives a value back to the calling code.
-   A function without an explicit return statement returns `None`.

``` python
def first():
    print(10)

def second():
    return 10

value = second()
print(value + 5)  # 15
```

The result of `first()` cannot be used as the returned integer because
`first()` returns `None`.

## 4.4 Default parameters

A parameter can have a default value:

``` python
def greet(name="Guest"):
    print("Hello", name)

greet()         # Hello Guest
greet("Alex")   # Hello Alex
```

Parameters with defaults generally follow parameters without defaults in
a function definition.

## 4.5 Side effects

A **side effect** is an observable change caused by a function other
than simply returning a value.

Examples:

-   Changing a global variable.
-   Modifying a mutable object supplied by the caller.
-   Printing to the terminal.
-   Writing to a file.
-   Sending a network request.

Example: modifying a list:

``` python
numbers = [1, 2, 3]

def add_number(items):
    items.append(4)

add_number(numbers)
print(numbers)  # [1, 2, 3, 4]
```

The list was modified in place.

## 4.6 How Python passes arguments

Python is often described as using **object-sharing** or
**pass-by-assignment** semantics.

A function parameter becomes a local name referring to the object
supplied by the caller. Reassigning that local name does not reassign
the caller's variable. Mutating a shared mutable object can be visible
to the caller.

Rebinding a local parameter:

``` python
def change_number(number):
    number = 100

value = 10
change_number(value)

print(value)  # 10
```

The local name `number` is rebound; the caller's `value` is unchanged.

Mutating a shared list:

``` python
def change_list(items):
    items.append(100)

values = [10, 20]
change_list(values)

print(values)  # [10, 20, 100]
```

The function and caller refer to the same list object, so the in-place
mutation is visible to both.

------------------------------------------------------------------------

# 5. Strings

## 5.1 What is a string?

A string (`str`) is an ordered sequence of text characters.

``` python
message = "Software Engineering"
```

Strings support indexing and slicing.

## 5.2 Indexing

Python sequence indexes start at zero:

``` python
word = "PYTHON"

print(word[0])   # P
print(word[1])   # Y
print(word[-1])  # N
```

Positive indexes count from the beginning. Negative indexes count from
the end.

## 5.3 Slicing

The general slicing form is:

``` python
sequence[start:stop:step]
```

The `stop` position is excluded.

``` python
word = "PYTHON"

print(word[0:3])   # PYT
print(word[2:])    # THON
print(word[:4])    # PYTH
print(word[::-1])  # NOHTYP
```

## 5.4 Strings are immutable

Strings are **immutable**, which means their contents cannot be changed
in place after the string object is created.

This raises a `TypeError`:

``` python
word = "PYTHON"
word[0] = "J"
```

Instead, create a new string:

``` python
word = "PYTHON"
word = "J" + word[1:]

print(word)  # JYTHON
```

The name `word` now refers to a new string.

## 5.5 Common string operations and methods

``` python
text = "  Hello World  "

print(len(text))                         # Length
print(text.upper())                      # Uppercase
print(text.lower())                      # Lowercase
print(text.strip())                      # Remove surrounding whitespace
print(text.replace("World", "Python"))   # Replace text
print(text.split())                      # Split into a list of words
print("Hello" in text)                   # Membership test
print(text.startswith("  Hello"))        # Prefix check
print(text.endswith("  "))               # Suffix check
print(text.count("l"))                   # Count occurrences
```

Methods such as `upper()` and `replace()` return new strings; they do
not mutate the original string.

## 5.6 String formatting

F-strings are a readable way to insert values into text:

``` python
name = "Alex"
age = 25

print(f"My name is {name} and I am {age} years old.")
```

## 5.7 Repeated concatenation and efficiency

Because strings are immutable, repeated concatenation may create new
strings and repeatedly copy existing content. In a loop, this can lead
to alot of work.

A common alternative is to collect pieces in a list and join them:

``` python
parts = []

for i in range(1000):
    parts.append(str(i))

result = "".join(parts)
```

`str.join()` combines an iterable of strings into one string. It is
generally the preferred pattern when building a string from many pieces.

------------------------------------------------------------------------

# 6. Data Structures

## 6.1 What is a data structure?

A **data structure** is a way of organizing and storing data so that it
can be accessed, updated and processed.

Choosing an appropriate
structure can make a program simpler and more efficient.

## 6.2 Lists

A Python list is an ordered, mutable collection. It can contain
duplicate values and values of different types.

``` python
numbers = [10, 20, 30]

numbers.append(40)
numbers.remove(20)

print(numbers)  # [10, 30, 40]
```

A list can contain mixed types:

``` python
items = ["Alex", 25, True, 3.14]
```

## 6.3 Stacks --- Last In First Out

A **stack** follows Last In, First Out (LIFO). The most recently added
item is removed first.

Think of a stack of plates: a plate is placed on top and the top plate
is removed first.

Python list implementation:

``` python
stack = []

stack.append("A")
stack.append("B")
stack.append("C")

print(stack.pop())  # C
print(stack.pop())  # B
print(stack.pop())  # A
```

Common uses:

-   Undo functionality.
-   Browser navigation history.
-   Function-call management.
-   Expression evaluation.
-   Depth-first search.

The usual stack operations are:

-   `push`: add an item.
-   `pop`: remove the most recently added item.
-   `peek` / `top`: inspect the top item without removing it.

In Python, `append()` and `pop()` at the end of a list are commonly used
for stack operations.

## 6.4 Queues --- First In First Out

A **queue** follows First In, First Out (FIFO). The earliest item added
is removed first.

Think of people waiting in a line: the person who joined first is served
first.

Use `collections.deque` for an efficient queue:

``` python
from collections import deque

queue = deque()

queue.append("A")
queue.append("B")
queue.append("C")

print(queue.popleft())  # A
print(queue.popleft())  # B
print(queue.popleft())  # C
```

Common uses:

-   Task scheduling.
-   Customer-service systems.
-   Message processing.
-   Breadth-first search.

## 6.5 Dictionaries --- hash tables

A Python dictionary stores key-value pairs:

``` python
student = {
    "name": "Alex",
    "age": 25,
    "course": "Software Engineering"
}

print(student["name"])
```

Add or update values:

``` python
student["age"] = 26
student["grade"] = "A"
```

A dictionary's keys must be hashable. Strings, integers and many
immutable objects can be keys. A list cannot be a dictionary key because
it is mutable and unhashable.


### How a hash table works

A hash table uses a hash function to help determine where a key-value
entry should be stored.

Conceptually:

1.  The program supplies a key.
2.  The hash function computes a hash value.
3.  The hash value helps determine a table location.
4.  The table uses that location and equality checks to find the
    associated entry.

A **hash collision** happens when different keys map to the same table
location or bucket.

Two common collision-handling strategies are:

-   **Chaining:** entries that collide are stored together in a bucket
    or linked structure.
-   **Open addressing:** the table searches for another available slot
    according to a probing strategy.

Python dictionaries use a hash-table design based on open addressing.
The exact implementation is an internal detail and may evolve between
Python versions.

## 6.6 Sets

A set is an unordered collection of unique, hashable elements.

``` python
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)  # Contains 1, 2, 3 and 4
```

Sets are useful for removing duplicates and performing mathematical set
operations.

``` python
students_a = {"Alex", "Jordan", "Sam"}
students_b = {"Sam", "Taylor", "Alex"}

print(students_a & students_b)  # Intersection
print(students_a | students_b)  # Union
print(students_a - students_b)  # Difference
```

-   **Intersection (`&`):** elements shared by both sets.
-   **Union (`|`):** all unique elements from either set.
-   **Difference (`-`):** elements in the first set but not the second.


------------------------------------------------------------------------

# 7. Big O Notation

## 7.1 What is Big O?

Big O notation describes how an algorithm's resource requirements grow
as the input size grows.

It is commonly used to discuss:

-   **Time complexity:** how the amount of work grows.
-   **Space complexity:** how memory requirements grow.

Big O is not a direct measurement of execution time in seconds. It
describes growth as input size increases, usually focusing on the
dominant term for large inputs.

## 7.2 Common time complexities

### O(1) --- Constant time

The amount of work stays approximately constant as the input grows.

``` python
def get_first(items):
    return items[0]
```

Accessing a list element by index is typically O(1).

### O(log n) --- Logarithmic time

The problem size is repeatedly reduced, often by half.

Binary search on a sorted collection is O(log n).

### O(n) --- Linear time

The work grows in proportion to the number of input elements.

``` python
def print_items(items):
    for item in items:
        print(item)
```

### O(n log n) --- Linearithmic time

This is common for efficient comparison-based sorting algorithms,
including Python's Timsort in typical complexity discussions.

``` python
numbers.sort()
```

### O(n²) --- Quadratic time

A common pattern is a loop nested inside another loop, where both
iterate over the input:

``` python
def print_pairs(items):
    for first in items:
        for second in items:
            print(first, second)
```

There are approximately n × n operations, so the time complexity is
O(n²).

### O(2ⁿ) --- Exponential time

The amount of work can roughly double for each additional input element.
Naive recursive Fibonacci is a familiar example of exponential growth.

Exponential algorithms become impractical quickly as n grows.

## 7.3 Illustrative growth comparison

The following values illustrate growth rates. They are not
execution-time measurements.

    Input size n   O(1)   O(log₂ n)     O(n)         O(n²)
  -------------- ------ ----------- -------- -------------
              10      1         \~3       10           100
             100      1         \~7      100        10,000
           1,000      1        \~10    1,000     1,000,000
          10,000      1        \~13   10,000   100,000,000

## 7.4 Recognizing complexity from code

### One constant-time operation

``` python
def get_first(items):
    return items[0]
```

Typical time complexity: **O(1)**.

### One loop over n items

``` python
def print_items(items):
    for item in items:
        print(item)
```

Time complexity: **O(n)**.

### Two nested loops

``` python
def print_pairs(items):
    for first in items:
        for second in items:
            print(first, second)
```

Time complexity: **O(n²)**.

### Two separate loops

``` python
def process(items):
    for item in items:
        print(item)

    for item in items:
        print(item)
```

The work is approximately 2n. Big O drops constant factors, so the
complexity is **O(n)**, not O(2n).

### Binary search

Binary search requires sorted input. It repeatedly halves the remaining
search range, giving **O(log n)** time.

``` python
def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1
```

The function returns the index if the target is found, otherwise `-1`.

## 7.5 Amortized complexity

Appending to the end of a Python list is generally **O(1) amortized**.

A dynamic array has a capacity. When it runs out of capacity, Python may
allocate a larger memory area and move existing references. That
individual append can cost O(n).

However, resizing does not happen on every append. Across a long
sequence of appends, the average cost per append remains O(1) amortized.

Amortized analysis considers the cost across a sequence of operations
rather than judging only the most expensive individual operation.

------------------------------------------------------------------------

# 8. Recursion

## 8.1 What is recursion?

Recursion occurs when a function calls itself to solve a smaller version
of the same problem.

A sound recursive function needs:

1.  **A base case:** the condition that stops further recursive calls.
2.  **A recursive case:** the function calls itself.
3.  **Progress:** each call moves closer to the base case.

Without a reachable base case, recursion can continue until Python
raises `RecursionError`.

## 8.2 Example: countdown

``` python
def countdown(number):
    if number == 0:
        print("Done!")
        return

    print(number)
    countdown(number - 1)


countdown(5)
```

Output:

``` text
5
4
3
2
1
Done!
```

The base case is `number == 0`. Each recursive call subtracts one,
moving toward that case.

## 8.3 Example: factorial

The factorial of a non-negative integer n is the product of all positive
integers from 1 to n. By definition, 0! is 1.

For example:

``` text
5! = 5 × 4 × 3 × 2 × 1 = 120
```

Recursive implementation:

``` python
def factorial(number):
    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


print(factorial(5))  # 120
```

For valid non-negative input, this function makes one recursive call for
each decrement until it reaches 1 or 0.

Its time complexity is O(n), and its call-stack space complexity is
O(n).

A production-ready version should validate that input is a non-negative
integer.

## 8.4 The call stack

Each active function call needs a stack frame containing information
such as local variables and where execution should resume.

For `factorial(4)`, the calls expand conceptually like this:

``` text
factorial(4)
    4 * factorial(3)
            3 * factorial(2)
                    2 * factorial(1)
                            returns 1
                    returns 2 * 1 = 2
            returns 3 * 2 = 6
    returns 4 * 6 = 24
```

The calls first move down toward the base case. Then the returned values
are combined as execution unwinds back up the call stack.

## 8.5 Fibonacci and repeated work

The Fibonacci sequence begins:

``` text
0, 1, 1, 2, 3, 5, 8, 13, 21, ...
```

Each number after the first two is the sum of the preceding two.

A simple recursive implementation:

``` python
def fibonacci(number):
    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(6))  # 8
```

This implementation is inefficient because it repeatedly calculates the
same values. Its time complexity is exponential; O(2ⁿ) is a commonly
used upper-bound description.

## 8.6 Memoization

**Memoization** stores previously calculated results so that repeated
requests can reuse them.

Python's `functools.lru_cache` provides a convenient cache:

``` python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(number):
    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(40))
```

With memoization, each Fibonacci value from 0 through n is calculated
once. The time complexity becomes O(n), with O(n) cache storage and O(n)
maximum recursion depth for this recursive implementation.

An iterative implementation can avoid the recursive call-stack cost:

``` python
def fibonacci_iterative(number):
    if number < 0:
        raise ValueError("number must be non-negative")

    a, b = 0, 1

    for _ in range(number):
        a, b = b, a + b

    return a


print(fibonacci_iterative(40))
```

## 8.7 When is recursion useful?

Recursion is natural for problems with recursive structure, such as:

-   Tree traversal.
-   Directory and file-system traversal.
-   Divide-and-conquer algorithms.
-   Backtracking.
-   Parsing nested structures.

Recursion is not automatically better than iteration. In Python, deep
recursion can hit the recursion limit, and each call uses stack space.
Choose the clearest approach that has acceptable resource costs.

## 8.8 Practical: `09_recursion.py`

Implement a recursive sum:

``` python
def sum_numbers(n):
    # Base case:
    # If n is 1, return 1.

    # Recursive case:
    # Return n + sum_numbers(n - 1).
    pass


print(sum_numbers(5))  # Expected: 15
```

One possible completed implementation:

``` python
def sum_numbers(n):
    if n == 1:
        return 1

    return n + sum_numbers(n - 1)


print(sum_numbers(5))  # 15
```

This version assumes n is a positive integer. Think about how you would
handle zero, negative input or invalid types.

------------------------------------------------------------------------

# 9. How Code Runs

## 9.1 Source code and machine instructions

Programmers write source code in programming languages. A processor
executes machine instructions. A compiler or runtime bridges that gap.

Different languages and runtimes use different approaches to translation
and execution.

## 9.2 Compiled languages

A compiler translates source code into another form, often native
machine code, before the program is run.

Examples include C, C++, Go and Rust.

A simplified workflow:

``` text
Source code
    |
    v
Compiler
    |
    v
Machine-code executable
    |
    v
Processor executes instructions
```

Compilation can detect certain errors before execution and can enable
optimizations. Exact behaviour depends on the language, compiler and
build process.

## 9.3 Interpreted languages

An interpreter or runtime executes a program by processing its
instructions in an execution environment.

Python is commonly called an interpreted language, but that label hides
important implementation details.

## 9.4 How CPython generally executes Python code

CPython, the standard and most widely used Python implementation,
generally follows this process:

``` text
Python source code (.py)
        |
        v
Compilation to bytecode
        |
        v
Python bytecode
        |
        v
CPython virtual machine
        |
        v
Program execution
```

The important distinction:

-   **Source code** is the Python code written by the programmer.
-   **Bytecode** is an intermediate set of instructions produced by
    Python's compiler.
-   **The Python virtual machine** executes the bytecode.

Python is therefore not simply reading each source line and translating
it directly into native processor instructions as it goes.

Other Python implementations can use different execution strategies.
Some runtimes use just-in-time (JIT) compilation to compile selected
code during execution.

## 9.5 Assembly language and machine code

Assembly language is a low-level language whose instructions correspond
closely to a processor's instruction set.

A simplified assembly example:

``` asm
MOV AX, 5
ADD AX, 3
```

The exact syntax and registers depend on the processor architecture and
assembler.

Machine code is the binary instruction representation executed by the
processor. Assembly is a human-readable representation of low-level
instructions.

## 9.6 Why C is sometimes called a middle-level language

C is sometimes described as a middle-level language because it combines
high-level constructs such as functions, loops and structured control
flow with low-level capabilities such as pointers and direct memory
manipulation.

This is a descriptive teaching label rather than a strict, universally
defined language category.

## 9.7 Practical: `10_bytecode.py`

``` python
# 10_bytecode.py

import dis

def add(a, b):
    return a + b


print(add(5, 3))

dis.dis(add)
```

Run it:

``` bash
python3 10_bytecode.py
```

The `dis` module displays the bytecode for the function. Exact
instructions can vary by Python version.

The objective is not to memorize bytecode instructions. It is to
understand where bytecode fits between Python source code and execution
by the runtime.

------------------------------------------------------------------------

# 10. Object-Oriented Programming

## 10.1 What is object-oriented programming?

Object-oriented programming (OOP) is a programming paradigm that
organizes software around objects.

An object combines:

-   **State:** data represented by attributes.
-   **Behaviour:** actions represented by methods.

A **class** defines the structure and behaviour that its instances can
have. An **object** is an instance of a class.

## 10.2 Classes and objects

Example:

``` python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.brand} is driving.")


car1 = Car("Toyota", "Red")
car2 = Car("BMW", "Black")

car1.drive()
car2.drive()
```

Output:

``` text
The Red Toyota is driving.
The Black BMW is driving.
```

Key terms:

  Term           Meaning
  -------------- -----------------------------------------------------
  `class Car`    Defines a class named `Car`
  `__init__`     Initializer called when a new instance is created
  `self`         Conventionally names the current instance parameter
  `self.brand`   An instance attribute
  `drive()`      An instance method
  `car1`         An object / instance of `Car`

`self` is not a special reserved keyword. It is the conventional name
for the first parameter of an instance method. Python passes the
instance to that parameter when the method is called through an
instance.

`__init__` initializes an already-created instance. It is commonly
called a constructor in beginner explanations, although technically
`__new__` is responsible for creating the instance.

## 10.3 Instance attributes and class attributes

An instance attribute belongs to an individual object:

``` python
class Dog:
    def __init__(self, name):
        self.name = name
```

Each dog can have a different name.

A class attribute is defined on the class and is shared through the
class unless shadowed by an instance attribute:

``` python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name):
        self.name = name


dog1 = Dog("Rex")
dog2 = Dog("Milo")

print(dog1.species)
print(dog2.species)
```

Be cautious with mutable class attributes such as lists: all instances
may share the same list. Use an instance attribute when each object
needs its own collection.

## 10.4 The four pillars of OOP

### 1. Encapsulation

Encapsulation groups data and methods together and provides a controlled
way to interact with an object's state.

Example:

``` python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def get_balance(self):
        return self._balance


account = BankAccount(100)
account.deposit(50)

print(account.get_balance())  # 150
```

The underscore in `_balance` is a Python convention indicating that the
attribute is intended for internal use.

Python does not enforce strict private access in the same way as some
other languages. A single leading underscore is a convention. Double
leading underscores trigger name mangling, which helps avoid accidental
name clashes but is not a security mechanism.

A stronger design can expose methods or properties that validate changes
instead of allowing arbitrary updates to internal state.

### 2. Inheritance

Inheritance allows a class to reuse and extend another class's
behaviour.

``` python
class Animal:
    def speak(self):
        print("The animal makes a sound.")


class Dog(Animal):
    def bark(self):
        print("Woof!")


dog = Dog()

dog.speak()  # Inherited from Animal
dog.bark()   # Defined in Dog
```

`Animal` is the parent or base class. `Dog` is the child or derived
class.

The `super()` function provides a way to call methods from the next
class in the method resolution order. It is often used to extend parent
initialization:

``` python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
```

### 3. Polymorphism

Polymorphism means that different object types can respond to the same
operation or interface in different ways.

``` python
class Dog:
    def speak(self):
        print("Woof!")


class Cat:
    def speak(self):
        print("Meow!")


animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
```

Output:

``` text
Woof!
Meow!
```

The loop does not need to know the concrete class of every object. It
calls `speak()` on each one.

Python commonly supports this through **duck typing**: an object can be
used wherever it provides the operations the code needs, regardless of
its declared class hierarchy.

### 4. Abstraction

Abstraction exposes essential operations while hiding implementation
details.

For example, a caller can use:

``` python
car.drive()
```

without needing to know every internal step used to make the car move.

Python supports formal abstract base classes through the `abc` module:

``` python
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def process(self):
        pass


class CardPayment(Payment):

    def process(self):
        print("Processing card payment.")


payment = CardPayment()
payment.process()
```

`Payment` defines an abstract operation. A concrete subclass must
implement it before it can be instantiated.

## 10.5 Method overriding versus method overloading

These terms are often confused.

### Method overriding

Overriding occurs when a subclass provides its own implementation of an
inherited method:

``` python
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def speak(self):
        print("Woof!")


dog = Dog()
dog.speak()  # Woof!
```

The `Dog` implementation overrides the inherited `Animal.speak()`
behaviour.

### Method overloading

In languages such as Java and C++, conventional method overloading means
defining multiple methods with the same name but different parameter
signatures.

Python does not support that same signature-based method overloading
directly. Defining the same method name again in a class generally
replaces the earlier definition.

Similar flexibility can be achieved with default arguments:

``` python
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c


calculator = Calculator()

print(calculator.add(2, 3))     # 5
print(calculator.add(2, 3, 4))  # 9
```

Other Python techniques include `*args`, `**kwargs`, singledispatch and
explicit type checks. These are not identical to Java-style compile-time
overload resolution.

------------------------------------------------------------------------


# 11. Face-Off Revision Checklist

Use this as a self-assessment. You should be able to explain each
concept in your own words and demonstrate it in Python.

## 11.1 Values and types

-   [ ] Explain what a value and data type are.
-   [ ] Identify `int`, `float`, `bool`, `str` and `complex`.
-   [ ] Explain why Python has no separate built-in character type.
-   [ ] Explain dynamic typing.
-   [ ] Convert between common types.
-   [ ] Explain `/`, `//` and `%`.
-   [ ] Predict the result of positive and negative modulo.
-   [ ] Explain what happens when a program divides by zero.
-   [ ] Use comparison and logical operators.

## 11.2 Variables and scope

-   [ ] Explain what a variable name refers to.
-   [ ] Explain local and global scope.
-   [ ] Explain shadowing.
-   [ ] State the LEGB lookup order.
-   [ ] Explain `global` and `nonlocal`.
-   [ ] Predict which variable a function will access.

## 11.3 Functions and parameters

-   [ ] Define and call a function.
-   [ ] Explain parameters versus arguments.
-   [ ] Return a value from a function.
-   [ ] Explain the difference between `print()` and `return`.
-   [ ] Use default parameters.
-   [ ] Explain side effects.
-   [ ] Explain Python's object-sharing / pass-by-assignment behaviour.
-   [ ] Distinguish rebinding a parameter from mutating an object.

## 11.4 Strings

-   [ ] Explain strings as ordered sequences.
-   [ ] Index a string.
-   [ ] Slice a string.
-   [ ] Explain string immutability.
-   [ ] Use common string methods.
-   [ ] Format strings with f-strings.
-   [ ] Explain why repeated concatenation can be inefficient.
-   [ ] Use a list and `join()` to build a string.

## 11.5 Data structures

-   [ ] Explain lists and their common operations.
-   [ ] Explain LIFO and implement a stack.
-   [ ] Explain FIFO and implement a queue.
-   [ ] Explain why `deque` is useful for queues.
-   [ ] Explain dictionaries and key-value lookup.
-   [ ] Explain hash functions and collisions at a conceptual level.
-   [ ] Explain chaining and open addressing.
-   [ ] Explain sets, uniqueness, intersection, union and difference.
-   [ ] Choose a suitable data structure for a given task.

## 11.6 Big O

-   [ ] Explain time complexity and space complexity.
-   [ ] Explain why Big O is about growth rather than seconds.
-   [ ] Recognize O(1), O(log n), O(n), O(n log n), O(n²) and O(2ⁿ).
-   [ ] Identify a linear loop.
-   [ ] Identify nested-loop behaviour.
-   [ ] Explain why O(2n) simplifies to O(n).
-   [ ] Explain binary search and its sorted-input requirement.
-   [ ] Explain amortized O(1) list append.

## 11.7 Recursion

-   [ ] Define recursion.
-   [ ] Identify the base case.
-   [ ] Identify the recursive case.
-   [ ] Explain why each call must make progress.
-   [ ] Trace a recursive countdown.
-   [ ] Implement factorial recursively.
-   [ ] Explain the call stack.
-   [ ] Explain why naive Fibonacci is inefficient.
-   [ ] Explain memoization.
-   [ ] Compare recursive and iterative approaches.

## 11.8 How code runs

-   [ ] Explain source code and machine code.
-   [ ] Explain compilation at a high level.
-   [ ] Explain interpretation at a high level.
-   [ ] Explain how CPython compiles source to bytecode.
-   [ ] Explain the role of the Python virtual machine.
-   [ ] Define assembly language.
-   [ ] Explain why C is sometimes called a middle-level language.
-   [ ] Explain that different language runtimes can execute code
    differently.

## 11.9 OOP

-   [ ] Explain the difference between a class and an object.
-   [ ] Create a class and instantiate objects.
-   [ ] Explain `self` and `__init__`.
-   [ ] Distinguish instance and class attributes.
-   [ ] Explain encapsulation.
-   [ ] Explain inheritance.
-   [ ] Explain polymorphism.
-   [ ] Explain abstraction.
-   [ ] Use `super()`.
-   [ ] Distinguish overriding from overloading.
-   [ ] Explain Python's approach to method overloading.

------------------------------------------------------------------------

# 13. Common Errors and Debugging

Errors are part of programming. Read the exception type and the
traceback instead of guessing.

## 13.1 `NameError`

A name is used before it has been defined or is not available in the
current scope.

``` python
print(username)
```

If `username` has not been defined, Python raises `NameError`.

## 13.2 `TypeError`

An operation is applied to an incompatible type.

``` python
age = "25"
print(age + 5)
```

Convert the value first:

``` python
age = int(age)
print(age + 5)
```

## 13.3 `ValueError`

The type may be appropriate, but the value cannot be converted or
accepted.

``` python
age = int("hello")  # ValueError
```

Handle user input carefully:

``` python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid whole number.")
```

## 13.4 `ZeroDivisionError`

A division or modulo operation uses zero as the divisor.

``` python
result = 10 / 0
```

Check the divisor before dividing or catch `ZeroDivisionError`.

## 13.5 `IndexError`

A sequence is accessed using an index outside its valid range.

``` python
numbers = [10, 20]
print(numbers[5])  # IndexError
```

Valid list indexes for this list are `0` and `1`, or `-1` and `-2`.

## 13.6 `KeyError`

A dictionary is accessed using a key that does not exist.

``` python
student = {"name": "Alex"}
print(student["age"])  # KeyError
```

Use `.get()` when a missing key is expected:

``` python
print(student.get("age", "Not provided"))
```

## 13.7 `IndentationError`

Python uses indentation to define blocks.

Incorrect:

``` python
if True:
print("Hello")
```

Correct:

``` python
if True:
    print("Hello")
```

Use consistent indentation, typically four spaces per level.

## 13.8 `RecursionError`

A recursive function makes too many calls, often because its base case
is missing or its recursive step does not make progress.

Always check that a recursive call moves toward a reachable base case.

------------------------------------------------------------------------

## Final study advice

Do not aim only to memorize definitions. For each topic, practise four
abilities:

1.  **Explain it:** describe the concept clearly in your own words.
2.  **Trace it:** predict what a short piece of code will do.
3.  **Build it:** write a small working example without copying.
4.  **Defend it:** explain why you chose a particular solution or data
    structure, including its trade-offs.

For the Software Engineering Face-Off, prioritize being able to read
unfamiliar code, predict output, identify errors, explain complexity,
and justify design choices.

