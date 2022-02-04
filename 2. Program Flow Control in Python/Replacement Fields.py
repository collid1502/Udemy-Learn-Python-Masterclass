"""
Replacement fields  - i.e. turning data types to strings
"""

age = 24
print("My age is " + str(age) + " years")

# In Python 3 - there is a newer method rather than STR everything
print("My age is {0} years".format(age))   # And it generates same output as above

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))  # Replacement fields enter each respective number in order

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}"
      .format(28, 30, 31))
"""
So, wherever {0} exists, is replaced by value at Index 0 in the .format() text.
Likewise, {1} is replaced by value at index 1 (so in example above - 30)
& {2} is replaced by index 2 (example above - 31) 
"""
# could make it look neater by doing:
print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}""".format(28, 30, 31))

