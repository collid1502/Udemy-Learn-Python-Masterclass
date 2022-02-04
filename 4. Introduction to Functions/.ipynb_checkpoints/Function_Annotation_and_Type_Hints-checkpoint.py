"""
Function Annotation & Type Hints 
"""

# Take an example function, we will add some annotation & type info to it 
 
def is_palindrome(string: str) -> bool:      # This can makes things a bit clearer. We can see the argument type to enter is a string. That then returns a Boolean Value.
    return string[::-1].casefold() == string.casefold()  

