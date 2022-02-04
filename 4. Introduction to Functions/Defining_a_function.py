"""
Defining a Function 
"""

# Use the keyword 'def' to begin defining a function 
# You can name it as you like, but should be lower case, no spaces, and not start with numbers 


def multiply():        # if it takes parameters, they will decalred within the ()
    result = 10.5 * 4
    return result      # tells the function to return the output/calculation 

                    # 2 blank lines before & after functions is best style practice 
answer = multiply() 
print(answer)       # prints 42.0 to the console 


# Some Notes 
# The definition within the defined function, only exists during the function, and is removed after.
# This basically means, if you run the multiply functon defined above, then do print(result) - you wont get anything 
print(result) # you'll get an error saying 'result' not defined.
# so, instead, we bind the output of the function (through the return key) to a new variable
# like above, you "answer=" for this

# you could of course, do this:
print(multiply())  # which gives the answer 42.0 as expected
# but the point here is, 'result' is not a saved variable with a bound value that can be called later, but 'answer' would be

#----------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------

# Building a more useful function
def multiply(x, y):      # Basically like defining a SAS macro, where you pass arguments to the macro when calling it 
    result = x * y 
    return result 

answer = multiply(3, 4) 
print(answer)             # prints 12, as would be expected 

# or, printing some times tables 
for val in range(1,5):
    two_times = multiply(2, val)
    print(two_times)
    print("-" * 20) 
    
# we get the answers -  2, 4, 6, 8 


#----------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------
# an example of checking if a string is a palindrome or not 
    
def is_palindrome(string):
    backwards = string[::-1]     # this step reverses the passed string 
    return backwards == string   # this step returns true/False for cases where the reversed string = passed string. AKA - a palindrome 


# we could write the above more simply, as 
def is_palindrome_better(string):
    return string[::-1].casefold() == string.casefold()  # This will produce the same True/False answer as above - case insensitive 


print(is_palindrome_better('Racecar'))  # Prints answer True to console 
print(is_palindrome_better('hello'))    # Prints answer False to console 


# A complete example using the function would be
word = input("Please enter a word you would like to check: ")
if is_palindrome_better(word):
    print("'{}' is a palindrome".format(word)) 
else:
    print("'{}' is not a palindrome".format(word)) 


# CHALLENGE 
# create a function palindrome_sentence. This function should check if a sentence is a plaindrome.
# we will only care about the alpha-numeric characters from the sentence, so can get rid of anything else 
    
 
def palindrome_sentence(sentence):
    new_string = ""                # Sets up an empty string for us to add to 
    for letter in sentence:
        if letter.isalnum():       # Checks if the letter is alpha-numeric, if so, returns True, otherwise False. So if True, add it to empty string
            new_string += letter   # This adds the letter into the current new_string variable  
    print(new_string)              # Prints out the new string we hav created, so that we can check & debug if needed 
    return new_string[::-1].casefold() == new_string.casefold()


print(palindrome_sentence('Do geese see god?'))  # should be True 
print(palindrome_sentence('What is your name?')) # should be False 

