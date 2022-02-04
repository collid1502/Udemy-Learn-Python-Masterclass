"""
Removing items from a list
"""

# using our computer parts example, we can let the customer remove items they no longer want

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
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # it's already in so remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)

        print("Your list now contains: {}".format(computer_parts))

    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):  # so, 'number' will be the index, 'part' will be the item
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()   # User inputs choice

print(computer_parts)  # prints list we have built out once loop has ended

