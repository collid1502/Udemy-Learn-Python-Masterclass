"""
2. Strings in Python
"""

print("Today is a good day to learn Python")
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')

# concat strings using plus
print("hello" + " world")

#################################################

greeting = "hello"
name = "Bruce"

# if we want a space we can add that too
print(greeting + ' ' + name)

#################################################
# collecting user input from a function
name2 = input("Please enter your name")
print(greeting + ' ' + name2)

age = 24
print(age)

# Data Types
print(type(greeting))   # class = 'str' aka string
print(type(age))        # class = 'int' aka integer

age = "2 years"   # age would now be bound to a string value, no longer an integer
print(age)
print(type(age))   # class now shows 'str'   - so we have 'rebound' age to string from integer
