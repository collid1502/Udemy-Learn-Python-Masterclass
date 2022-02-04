# -*- coding: utf-8 -*-
"""
Function Signatures - Print Revisted
"""

# Function signatures are where the function allows us to pass arguments/parameters to it, in order to achieve different performance than 
# the default actions set. Below we will be looking at the Pritn function, and the different elements we can change to modify its output

name = "Tim" 
age = 10

print(name, age, "Python", 2020)   # You'll see this prints out >>>   Tim 10 Python 2020 to the console


# Sep keyword argument 
print(name, age, "Python", 2020, sep=", ")   # separator set to comma & space for output 

# End keyword argument 
"""
When we looked at the printing meals from a list code, all the items were printed to new lines.
This is because, the default argument for the end keyword in print function is /n (aka new line).
If we set this to something else, say a space (" ") then we can continue printing output to one line, with just spaces between & so on.
"""


