
"""
Functions calling Functions
"""

# Lets say we create a first function, which checks if a string is a palindrome
def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()  # This will produce the same True/False answer as above - case insensitive 


# For example, we have a second function that checks if a sentence is a palindrome 
# But notice line 20. We use the same code as above...
def palindrome_sentence(sentence):
    new_string = ""                # Sets up an empty string for us to add to 
    for letter in sentence:
        if letter.isalnum():       # Checks if the letter is alpha-numeric, if so, returns True, otherwise False. So if True, add it to empty string
            new_string += letter   # This adds the letter into the current new_string variable  
    print(new_string)              # Prints out the new string we hav created, so that we can check & debug if needed 
    return new_string[::-1].casefold() == new_string.casefold()



# This is a case where we could call a function, within a function, rather than copying and pasting loads of code.
def palindrome_sentence(sentence):
    new_string = ""               
    for letter in sentence:
        if letter.isalnum():      
            new_string += letter   
    print(new_string)              
    return is_palindrome(new_string)  # we make use of the already defined 'Is_Palindrome' function 

