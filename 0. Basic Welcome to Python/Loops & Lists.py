"""
Loops & Lists - use of the 'continue' statement
"""

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

"""
for item in shopping_list:
    if item != "spam":          # This now excludes spam 
        print("Buy " + item)    
"""

for item in shopping_list:
    if item == "spam":
        continue            # 'Continue' causes all remaining code within the block, to be ignored, and roll back to
                            #  start of the code/previous code block
    print("buy " + item)

for item in shopping_list:
    if item == "spam":
        break            # if you use break, the whole loop terminates once the 'break' runs

    print("buy " + item)


# Example: running a search and breaking loop once found
item_to_find = "spam"
found_at = None                # we initialise the variable 'found_at' - so that it exists
                               # 'None' is used a bit like 0 - essentially holds an empty/not found

for index in range(len(shopping_list)):          # using 'len' creates a range(0, 6)
    if shopping_list[index] == item_to_find:     # If the item at index matches spam, then place that index
        found_at = index                         # value into the found_at variable
        break                                    # once found, terminate loop