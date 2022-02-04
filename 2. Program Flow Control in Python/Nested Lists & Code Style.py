# -*- coding: utf-8 -*-
"""
Nested Lists & Code Style
"""

# Remember the example of concatenating two simple lists 
empty_list = []
even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = even + odd 
print(numbers)

#----------------------------------------------------
# what would happen if we did this instead:

empty_list2 = []
even2 = [2,4,6,8]
odd2 = [1,3,5,7,9]

numbers2 = [even2, odd2]  # Notice it creates a list holding Two Lists as its variables/observations
print(numbers2)


# We can then work through these nested lists
for number_list in numbers2:
    print(number_list)
    
    for value in number_list:
        print(value)

# Notice the output
# First, the even list is printed in it's list form, then, all the corresponding numbers in that list get printed
# Then repeats for odd etc.
  
#---------------------------------------------------------------------------------------------------------------------------

# Processing Nested Lists - Example 

menu = [
        ["egg", "bacon"],
        ["egg", "sausage", "bacon"],
        ["egg", "spam"],
        ["egg", "bacon", "spam"],
        ["egg", "bacon", "sausage", "spam"],
        ["spam", "bacon", "sausage", "spam"],
        ["spam", "sausge", "spam", "bacon", "spam", "tomato", "spam"],
        ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    if "spam" not in meal:
        print(meal)         # print only lists that don't contain spam 

        for item in meal:
            print(item)     # Now prints each item, in each menu list (not containing spam)
            
    else:
        print("{0} has a spam count of {1}".format(meal, meal.count("spam")))   # This provides a count of the times spam appears, per menu list, for when spam is present 

#----------------------------------------------------------------------------------------------------------------------------------------
## CHALLENGE
# Write code to output each meal but with Spam removed 
menu = [
        ["egg", "bacon"],
        ["egg", "sausage", "bacon"],
        ["egg", "spam"],
        ["egg", "bacon", "spam"],
        ["egg", "bacon", "sausage", "spam"],
        ["spam", "bacon", "sausage", "spam"],
        ["spam", "sausge", "spam", "bacon", "spam", "tomato", "spam"],
        ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item)
    print()
            
 
         