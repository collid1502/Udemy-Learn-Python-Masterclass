"""
Iterating over a List
"""

# available_parts = ["computer",
#                    "monitor",
#                    "keyboard",
#                    "mouse",
#                    "mouse mat",
#                    "hdmi cable"
#                    ]
#
# # Appending to a List
# current_choice = "-"
# computer_parts = [] # create an empty list - this will be a list we append items to as they are selected
#
# while current_choice != '0':
#     if current_choice in "123456":
#         print("Adding {}".format(current_choice))
#         if current_choice == '1':
#             computer_parts.append("computer")
#
#         elif current_choice == '2':
#             computer_parts.append("monitor")
#
#         elif current_choice == '3':
#             computer_parts.append("keyboard")
#
#         elif current_choice == '4':
#             computer_parts.append("mouse")
#
#         elif current_choice == '5':
#             computer_parts.append("mouse mat")
#
#         elif current_choice == '6':
#             computer_parts.append("hdmi cable")
#     else:
#         print("Please add options from the list below:")
#         for part in available_parts:   # now uses the list defined above at start and iterates over it
#             print("{0}: {1}".format(available_parts.index(part) + 1, part))
#
#     current_choice = input()   # User inputs choice
#
# print(computer_parts)  # prints list we have built out once loop has ended

"""
What is this bit:
        for part in available_parts:   # now uses the list defined above at start and iterates over it 
            print("{0}: {1}".format(available_parts.index(part) + 1, part)) 
doing?

essentially, it allows us to iterate ver a predefined list above, rather than type out multiple statements (as seen in list_intro code)
and then uses the index plus 1 (remember index starts at 0) & the part name to create the list format >> 1: computer etc etc.

There is actually a more efficient way to do this - enumerate function - covered below 

enumerate returns each item, with it's index position, for a list
"""

# EXAMPLE - Using enumerate function rather than searching for each index

"""
valid_choices = [str(i) for i in range(1, len(available_parts) +1)]
print(valid_choices)    # This creates the valid choices as a list, 1: computer, 2: monitor etc etc

we will cover the above method in more detail at a later section 
"""

available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi cable"
                   ]

valid_choices = []   # empty list created
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))

current_choice = "-"
computer_parts = [] # create an empty list - this will be a list we append items to as they are selected

while current_choice != '0':
    if current_choice in valid_choices:
        print("Adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)

    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):  # so, 'number' will be the index, 'part' will be the item
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()   # User inputs choice

print(computer_parts)  # prints list we have built out once loop has ended

