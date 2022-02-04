# -*- coding: utf-8 -*-
"""
Strings - The Split Method
"""

# This method splits a string up into words 

panagram = "The quick brown fox jumps over the lazy dog"

words  = panagram.split()
print(words) 
# outputs a list of each word inside the string

#---------------------------------------------------------------------------------------------------------------------------
# Above, we passed no arguments to split(), so it defaulted to splitting on white space, new lines etc.
# So as a demo, if we space the above string over several lines, lets see it still perform the same action 

panagram2 = """The quick brown 
fox jumps over 
the lazy dog"""

words2  = panagram2.split()
print(words2)      # we can see the same output as before 

#---------------------------------------------------------------------------------------------------------------------
# Lets run through an example of splitting out a string of numbers separated by a comma
numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))   # so, this spits out a list, containing each of our numbers from the numbers string

#---------------------------------------------------------------------------------------------------------------------
# Coding challenge User Example
"""
Write a python program which prompts the user to enter three integers separated by by a comma.
The user input is of the form: a,b,c  (where a b & c will be numbers).
The program must then use these input numbers to calculate:
    a + b - c
    
Run the example code for input numbers:   10, 11, 10
"""
# Step 1 - take input from user 
user_input = input("Please enter three numbers: ")

# Step 2 - Split the given string input into 3 parts 
string_split = user_input.split(",")

# Step 3 - convert each split section into an integer
numbers_list = []
for string in string_split:
    numbers_list.append(int(string)) 
    
# Step 4 - calculate the result:  a + b - c
result = numbers_list[0] + numbers_list[1] - numbers_list[2]

# Step 5 - Output result 
print(result) 
# and you get the answer of 11 as expected 
