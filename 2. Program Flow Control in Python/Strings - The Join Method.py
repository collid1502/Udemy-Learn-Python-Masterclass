# -*- coding: utf-8 -*-
"""
Strings - The Join Method
"""

# let's start by looking at the old example of a food menu (meals recorded as lists) 
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
    for index in range(len(meal) -1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
            
    print(meal) 

# the output of the above method prints lists, with their square brackets still intact etc.
# if we wanted to tidy this up a bit, the join method can be used to make nicer output, and we can use it during the print step 
for meal in menu:
    for index in range(len(meal) -1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
            
    print(", ".join(meal))  

# now you'll see we simply output each meal item, followed by a comma, to create a more "usual" looking output list.

#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
    
"""
More details on the join method with some simple examples
"""

# create list called flowers
flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavendar",
    "Sunflower",
    "Tiger Lily",
    ]
# print each flower out
for flower in flowers:
    print(flower)       

# Now, if we use the join method, it can iterate through an iterable (aka a list) without needing to be placed into a For Loop
separator = " | "
output = separator.join(flowers)
print(output) 

# Notice the output, we print each flower to the same line, separated by a pipe delimiter
# Obviously, we could tidy this all up and place on one line of code if we wanted to be neat 
print(" | ".join(flowers))
# And we get the same output 
