"""
Docstrings
"""


# we create a function to create an integer based on what the user types/inputs 
def get_integer(prompt):
    """
    Gets an integer from Standard Input (stdin). 
    
    The function will continue to loop, prompting the user, until a 
    valid `integer` is enetered.

    Args:
        prompt: The string user will see, when they're prompted to 
            enter the value..

    Returns: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)   # when conditions for return is met, it processes and then leaves loop, rather than running again 
        else:
            print("You have not entered a valid number. Please try again.")


# we can then collect the documentation from this function by doing the following           
print("*" * 70)
print(get_integer.__doc__)
print("*" * 70)
            

# You can also use help(<function_name>) to return information, and thsi works well especially when inside IPython Shell
help(get_integer)   # AKA - you can type this directly in the shell and it will work 
