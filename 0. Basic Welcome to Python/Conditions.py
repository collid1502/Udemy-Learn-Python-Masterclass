"""
Working with conditions
"""

# AND / OR
age = int(input("How old are you? "))

if age >=16 and age <= 65:
    print("Have a good day at work")

# Simplifying chained comparisons - aka can remove the need for AND
if 16 <= age <= 65:
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("-" * 80)

# Using OR
if age < 16 or age > 65:
    print("Enjoy your free time")


"""
Booleans 
"""
# A Boolean value is a value that can be either True or False
# So a Boolean expression is something that evaluates to True or False etc.

day = "Monday"
temperature = 30
raining = True

if day == "Saturday" and temperature > 27 and not raining:
    print("Go Swimming")
else:
    print("Learn Python")

# using AND & OR for conditional programming
if (day == "Saturday" and temperature > 27) or not raining:
    print("Go Swimming")
else:
    print("Learn Python")

"""
-------------------------------------------------------------------------
"""
"""
if 0:
    print("True")     # 0 is evaluated to False when used in boolean expression, hence IDE says code unreachable
else:
    print("False")
"""

name = input("Please enter your name: ")
if name:
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")

"""
-------------------------------------------------------------------------
"""

# Using IN & NOT IN

parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")


# Not In
activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold():        # Casefold function converts strings to lowercase - aka caseless string
    print("But I want to go to the cinema")
else:
    print("Great! Let's go")

"""
-----------------------------------------------------------------------------
"""
# Example

name = input("Please enter your name: ")
age = int(input("How old are you? "))

if 18 <= age < 31:
    print("Welcome to the 18-30 Holiday Club, {0}".format(name))
else:
    print("I'm sorry, but you cannot enter the 18-30 Holiday Club due to your age")

