#O(1) — Constant time
def get_first(items):
    return items[0]


#O(n) — Linear time
def print_items(items):
    for item in items:
        print(item)

#O(n²) — Quadratic time
def print_pairs(items):
    for first in items:
        for second in items:
            print(first, second)

        
#O(log n) — Logarithmic time
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



