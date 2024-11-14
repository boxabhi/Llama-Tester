# Sample Python File with Poor and Good Functions

# Poorly written function: 
def calculate_area_of_circle(radius):
    return 3.14 * radius * radius  # Hardcoded pi value, lacks error handling

# Good function: 
import math

def calculate_area_of_circle_v2(radius):
    if radius <= 0:
        raise ValueError("Radius must be greater than zero")
    return math.pi * radius ** 2  # Uses math.pi, more accurate and handles edge cases

# Poorly written function:
def add_numbers(x, y):
    return x + y + 0  # Redundant addition of 0

# Good function:
def add_numbers_v2(x, y):
    return x + y  # Simple and clear

# Poorly written function:
def find_max_number(lst):
    max_num = None
    for i in lst:
        if max_num == None:
            max_num = i
        elif max_num < i:
            max_num = i
    return max_num  # This can be simplified and optimized

# Good function:
def find_max_number_v2(lst):
    if not lst:
        raise ValueError("The list cannot be empty")
    return max(lst)  # Built-in function that handles edge cases and is optimized

# Poorly written function:
def filter_even_numbers(lst):
    even_numbers = []
    for number in lst:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers  # It works but can be optimized using list comprehension

# Good function:
def filter_even_numbers_v2(lst):
    return [num for num in lst if num % 2 == 0]  # More concise and efficient using list comprehension

# Poorly written function:
def divide_numbers(a, b):
    if b == 0:
        return 0  # Incorrect handling of division by zero, should raise an exception
    return a / b

# Good function:
def divide_numbers_v2(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")  # Correct error handling for division by zero
    return a / b
