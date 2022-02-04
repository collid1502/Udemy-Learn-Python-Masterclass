"""
Continued: 'Lists' in Python
"""

# Very simple list example
computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]
print(computer_parts)

# Now, using an index, we can replace one of the items on the list above. Swap trackball for mouse
computer_parts[3] = "trackball"
print(computer_parts)


#---------------------------------------------------------------
# Example 2 - replace a slice of a list
print(computer_parts[3:])   # This prints all items in list from index 3 to end of list (mouse & mouse mat)

# so, imagine we want to replace mouse & mouse mat with, trackball
computer_parts[3:] = ["trackball"]
print(computer_parts)

