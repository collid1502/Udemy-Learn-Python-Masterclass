"""
Introduction to 'Lists' in Python
"""

# Very simple list example
computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]

for part in computer_parts:
    print(part)

# we can use the index position to collect list items
print()
print(computer_parts[2])

# collecting multiple items from the list
print(computer_parts[0:3])

# last item in the list
print(computer_parts[-1])

# NOTES
"""
Strings are 'Immutable' , whilst Lists are 'Mutable' 

Essentially, when something is immutable, it means it cannot be changed.
Immutable types built into Python:
    > int
    > float 
    > bool (True or False)
    > str (string)
    > tuple
    > frozenset 
    > bytes 
    
Mutable:
    > list 
    > dict 
    > set 
    > Bytearray 
"""

# Immutable Object
result = True
another_result = result
print(id(result))          # ID returns the identity of the object
print(id(another_result))

# looking at the printed ID, both have the same, because they are bound off the same 'True'

# Now
result = False
print(id(result))   # result now has a different id.

#######################################################################################################

# Mutable Object
shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))   # The IDs for both should match as expected

shopping_list += ["cookies"]
print(shopping_list)      # now has cookies in the list - so we have successfully mutated the list
print(id(shopping_list))  # The ID remains unchanged, because lists are mutable, so Python didn't need to make a new one
                          # The list is simply just added to, rather than a "new thing" created 


"""
So, lists can have multiple names bound to them.
If we look above, another_list is a name bound to the list: shopping_list. Now, even though we then add 'cookies' to 
shopping_list after, if we actually reference another_list again (like the print statement below) it will now 
include cookies. Essentially, the underlying data within Python can be bound to multiple names that will represent
the same object, even when it is being modified.

There might not be a specific Analytics need for this, but good to know nonetheless.
"""

print(another_list)    # will now show 'cookies' added to it

########################################################################################################

# Appending to a List
current_choice = "-"
computer_parts = [] # create an empty list - this will be a list we append items to as they are selected

while current_choice != '0':
    if current_choice in "123456":
        print("Adding {}".format(current_choice))
        if current_choice == '1':
            computer_parts.append("computer")

        elif current_choice == '2':
            computer_parts.append("monitor")

        elif current_choice == '3':
            computer_parts.append("keyboard")

        elif current_choice == '4':
            computer_parts.append("mouse")

        elif current_choice == '5':
            computer_parts.append("mouse mat")

        elif current_choice == '6':
            computer_parts.append("hdmi cable")
    else:
        print("Please add options from the list below:")
        print("1: computer")
        print("2: monitor")
        print("3: keyboard")
        print("4: mouse")
        print("5: mouse mat")
        print("6: hdmi cable")
        print("0: to finish")

    current_choice = input()   # User inputs choice

print(computer_parts)  # prints list we have built out once loop has ended

