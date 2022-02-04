"""
Python 2 - String Interpolation

This is now old & being covered for understanding in case coming across old code/examples from other analysts
"""

# only used in Python 2, as being decomissioned for Python 3
# Interpolation is a method for formatting strings

age = 24
print("My age is %d years" % age)

# works on a strict left to right replacement. so, first %d is replaced by 'Age' variable.
# then %s is replaced by variable 'major', then the next %d is replaced by 6, then the next %s is replaced by variable 'minor'
major = "years"
minor = "months"
print("My age is %d %s, %d %s" % (age, major, 6, minor))

# to enter a float (decimal) in a string
print("PI is approx. %f" % (22/7))   # use the %f to be able to place a float (decimal number) into string

print()  # Blank Space to console
# more precise
print("PI is approx. %60.50f" % (22/7))
