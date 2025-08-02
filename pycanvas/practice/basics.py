# --- Indentation ---
# What happens if you remove the indentation from a line inside a function?
# def some_function():
#     print("hello")

# How does Python respond if blocks are not indented consistently?
# It yells at you

# Can you use both tabs and spaces for indentation in the same file?
# def my_func():
#     print("test")
#     print("that")
# It does not yell at you, but it is best practice to just use one (tabs)

# --- Integers, Floats, Strings, Booleans ---
# What type does Python assign to the value 42? What about 3.14? "hello"? True?
# Use the type() function to explore the types of different literals.
data = type(99)
print(data)
print(type(99))
print(type("some string"))
print(type(True))
print(99)
print("some string")
print(True)

# Can you convert a float to an integer? What about a string to a float?
fav_float = 10.99
int_float = int(fav_float)
print(int_float)

# What happens if you try to add an integer and a string?
last_name = "Barkley"
jersey_number = 29
str_int = str(jersey_number)
print("My favorite player is " + last_name + str_int)

# --- Arithmetic Operators ---
# What is the result of 7 + 3, 7 - 3, 7 * 3, and 7 / 3?
# How does 7 // 3 differ from 7 / 3?
# What does 2 ** 3 evaluate to?
# What is the remainder when 10 is divided by 3?
# Can you combine arithmetic operations and control the order with parentheses?

# --- if, elif, else ---
print("========\n")
# Write code that prints different messages based on whether a number is positive, negative, or 0
n = -20 # The users choice
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# What happens if you use if without elif or else?
# Try using if...elif...else to check for different string values.
def do_i_have_class_today(day):
    if day == "Wednesday" or day == "Friday":
        return "Yes"
    elif day == "Monday":
        return "Depends on the week"
    elif day == "Thurkday":
        return "tf is a thurkday"

    return "No"

# Can you nest if statements inside each other?
def determine_status(logged_in, admin):
    # If a user is logged in and they have admin then tell them.
    # If they aren't logged in, tell them to log in.
    # If they are logged in but don't have admin, they are in the standard interface.
    if logged_in:
        if admin:
            print("Admin access granted")
        else:
            print("Normal user")
    else:
        print("Please log in")
    
# Food Ordering Problem
# To place an order, you must be at least 18
# To purchase something, the cost must be less than your money
# You are given a persons age, money, and the cost of the item
print("========\n")
age = 26
money = 11
cost = 19

if age >= 18:
    if money > cost:
        print("Your order has been taken")
    else:
        print("Please deposit cash in your account")
else:
    print("Not old enough")

# What does Python do if multiple elif conditions are true?
# Goes to the first one

# Try writing a nested if statement — how does indentation help you keep track of the logic?

# --- for loops ---
# How can you print every number from 1 to 10 using a for loop?
print("========\n")
for i in range(1, 11):
    print(i)

# What does range(5) return? What about range(2, 10, 2)?
print("========\n")
for i in range(5):
    print(i)

print("========\n")
for i in range(2, 10, 2):
    print(i)

# Can you loop over the characters in a string?
print("========\n")
my_string = "class"
for i in range(len(my_string)):
    print(my_string[i])

for letter in my_string:
    print(letter)

list_of_names = ["Jesus", "Andrew", "Ethan", "Corbin"]
print(list_of_names[0])
print(list_of_names[3])

# Write a for loop that sums the numbers in a list.
nums = [5, 10, 15, 20, 25]  # 75
total = 0
for number in nums:
    print("Adding " + str(number) + " to the total (currently at " + str(total) + ")")
    total = total + number
    
print(total)

# How can you use a for loop to create a new list based on some condition?
# We want to take nums and from it, create a new list called evens
evens = []
# To add to a list you can use list_name.append(value)
# Modulo % gives you the remainder of some division 
# Divides by some number (whatever you put after) and return the remainder
# 47 % 3
# 47 / 3 = 15.asdyuiaegy79joasnjl;asdjl 
# 15 * 3 = 45
# Remainder of 2

# 19 % 4 = 3
# 20 % 4 = 0
for number in nums:
    print(number)
    isEven = number % 2 == 0
    print(isEven)
    if isEven:
        # Add to the list 
        evens.append(number)

print(evens)
    
# --- Functions ---
# How do you define a function that takes no arguments and prints a message?
def prints_a_message():
    print("message")

# How do you define a function that takes two numbers and returns their sum?
def add_2_numbers(n1, n2):
    return n1 + n2

# add_2_numbers(11, 10) -> 21

# What happens if you call a function without the required arguments?
# Errors out
# add_2_numbers()

# Can you write a function that uses an if statement inside it?
# Try writing a function that takes a list and returns only the even numbers.

def extract_evens(old_list):
    new_list = []
    for number in old_list:
        if number % 2 == 0:
            new_list.append(number)
    return new_list

numbers = [
    8342, 17, 1001, 402, 59, 7383, 2234, 487, 9311, 240, 73, 9998, 3421, 876,
    125, 6002, 43, 1090, 3801, 2940, 73, 890, 54, 7711, 222, 7853, 689, 84, 905,
    1023, 614, 7452, 9021, 3100, 488, 369, 9001, 753, 82, 9110, 408, 11, 3392,
    199, 8703, 882, 76, 550, 3223, 104, 8771, 9982, 10000, 27, 5610, 710, 1401
]
print(extract_evens(numbers))

# The parity of a number can either be odd or even
def parity(old_list):
    parity_list = []
    for number in old_list:
        if number % 2 == 0:
            parity_list.append("even")
        else:
            parity_list.append("odd")
    return parity_list

numbers = [
    8342, 17, 1001, 402, 59, 7383, 2234, 487, 9311, 240, 73, 9998, 3421, 876,
    125, 6002, 43, 1090, 3801, 2940, 73, 890, 54, 7711, 222, 7853, 689, 84, 905,
    1023, 614, 7452, 9021, 3100, 488, 369, 9001, 753, 82, 9110, 408, 11, 3392,
    199, 8703, 882, 76, 550, 3223, 104, 8771, 9982, 10000, 27, 5610, 710, 1401
]
parity_list = parity(numbers)
print(parity_list)

# --- Recursion ---
# 0  1  2  3  4  5  6  7   8
# 0, 1, 1, 2, 3, 5, 8, 13, 21
def fib(n):
    # Fibonacci does not work for negative numbers
    if n < 0:
        return -1    

    if n <= 1:
        return [n]

    return fib(n - 1) + fib(n - 2)

# print(fib(7)) # 13
# [0, 1, 1, 2, 3, 5, 8, 13]

# fib(3)
# - fib(2)
#   - fib(1): 1 
#   - fib(0): 0
# - fib(1): 1

# Real Life Example
# Let's say we have a package (a collection of software)
# Packages have dependencies

# Node
#     value = 8
#     left_child = Node(3, left_child, right_child)
#     right_child = Node(10, None, right_child)

# class Node:
#     def __init__(self, val, left, right):
#         self.val = val
#         self.left = left
#         self.right = right

    
# og_left_child = Node(3, None, None)
# og_right_child = Node(10, None, None)
# top_node = Node(8, og_left_child, og_right_child)

# print(top_node)
# print(top_node.val)
# print(top_node.left.val)
# print(top_node.right)

# def get_leaf(root):
#     my_node = root
#     if my_node.left != Node:
#         return get_leaf(my_node.left)
#     elif my_node.right != Node:
#         return get_leaf(my_node.right)
#     else:
#         return my_node