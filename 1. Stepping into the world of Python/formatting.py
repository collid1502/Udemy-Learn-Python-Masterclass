"""
Formatting strings
"""

for i in range(1, 13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i **2, i **3))

# Formatted
for i in range(1, 13):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i **2, i **3))
# :2 is the field width, so, we are basically reserving 2 spaces for teh digits to enter into. Look how 1 down to 12 lines up neatly in output
# :4 is field width, again reserving 4 spaces, as each calculation of i**2 & i**3, results in a number no greater than 4 digits, so again, prints neatly by reserving 4 spaces

print()   # prints blank line space in console


# to left align the values
for i in range(1, 13):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i **2, i **3))

# and notice the output is now left aligned, and nice & neat

print()

# An example of formatting strings containing numbers with decimal points (like the number Pi)
print("Pi is approx. {0:12}".format(22 / 7))       # General format - defaults to printing 15 decimals
print("Pi is approx. {0:12f}".format(22 / 7))      # when using the 'f' defaults to 6 spaces after decimal point
print("Pi is approx. {0:12.50f}".format(22 / 7))   # each of the next lines, has a precision of 50 decimal places (python maxes out at 53 decimal places precision)
print("Pi is approx. {0:52.50f}".format(22 / 7))
print("Pi is approx. {0:62.50f}".format(22 / 7))
print("Pi is approx. {0:72.50f}".format(22 / 7))

# so, nice & neat for Pi
print("Pi is approx. {0:<52.50f}".format(22 / 7))   # Creates a left aligned output with up to 50 decimal precision

print()
print()
"""
--------------------------------------------------------------------------------------------------------------------------------------------
"""

## F Strings ~ only available in newer version of Python (3.6 upwards)
# It's a way to get around having a number variable in a string, more easily
# Example:
name = "Dan"
age = 27
print(name + f" is {age} years old")

# or
pi = 22/7
print(f"Pi is approx. {pi:12.50f}")

# or
print(f"Pi is approx. {22/7 :12.50f}")
