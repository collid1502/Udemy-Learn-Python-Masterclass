"""
Sequence Operators
"""

string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)

# or could do (this is how Python interprets the above)
print("he's " "probably " "pining " "for the " "fjords")

print("Hello " * 5)  # This prints >> Hello Hello Hello Hello Hello

"""
print("Hello " * 5 + 4) # This won't work unless 5 + 4 is in () and operates before trying to multiply Hello str
"""
# Example:

print("Hello " * (5+4))    # Prints Hello .... Hello 9 times
print("Hello " * 5 + "4")  # Prints Hello .... Hello 5 times, with a '4' at the end of the string


"""
Operator to check if one string is a substring of another 
"""
today = "friday"
print("day" in today)       # True
print("fri" in today)       # True
print("thur" in today)      # False
print("parrot" in "fjord")  # False


