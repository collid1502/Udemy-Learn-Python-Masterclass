"""
Augmented Assignment
"""

# Augmented assignment is basically a shorthand way of assigning values to a variable

# An Example:
"""
guesses = guesses + 1

# we could write it as:
guesses += 1              # which is shorthand
"""

"""
So, what is going on?

when we use += (augmented assignment form) Python needs only evaluate the assignee (guesses in the example) once!

in the guesses = guesses + 1 form (where guesses appears twice) Python has to evaluate the variable each time 
it appears (so twice in this example). This is thus less efficient.
"""

# An Example run through

x = 23

x += 1
print(x)   # x is now 24

x -= 4
print(x)   # x is now 20

x *= 5
print(x)   # x is now 100

x //= 4
print(x)   # x is now 25  (100 divided by 4 - through INTEGER division)

x /=5
print(x)   # x is now 5.0  (note, float division so where x was integer now converted to float)

x **=2
print(x)   # 5.0 to the power of 2 is 25.0 (x is still a float)

x %= 5
print(x)   # 0.0 - 25 is exactly divisible by 5 with 0 remainder etc.


# Another example

greeting = "Good "
greeting += "morning "
print(greeting)       # creates Good Morning as one string

greeting *= 5
print(greeting)       # has now printed the message 5 times


# NB - good place to check for style of Python code is PEP8 (just google it)