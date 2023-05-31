# Example 1: Basic Lambda Function
addition = lambda x, y: x + y
result = addition(3, 5)
print("Result of addition:", result)  # Output: 8

# Example 2: Sorting using Lambda Function
students = [
    {"name": "John", "age": 20},
    {"name": "Alice", "age": 19},
    {"name": "Bob", "age": 21}
]

students.sort(key=lambda x: x["age"])
print("Sorted students by age:")
for student in students:
    print(student)
"""
Output:
Sorted students by age:
{'name': 'Alice', 'age': 19}
{'name': 'John', 'age': 20}
{'name': 'Bob', 'age': 21}
"""

# Example 3: Filter using Lambda Function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)  # Output: [2, 4, 6, 8, 10]

# Example 4: Map using Lambda Function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Example 5: Reduce using Lambda Function
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print("Product of numbers:", product)  # Output: 120