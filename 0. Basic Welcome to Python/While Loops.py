"""
While Loops
"""

for i in range(0, 10):
    print("i is now {}".format(i))

# now - same but using while loop
i = 0
while i < 10:
    print("i is now {}".format(i))
    i = i + 1      # Can be written as i += 1

#############################################################################################

# Example - Adventure Game

available_exits = ["north", "south", "east", "west"]

chosen_exit = ""    # initialises variable with empty string

while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")

print("aren't you glad you got out of the room!")

#################################################################
# Breaks in while loops

available_exits = ["north", "south", "east", "west"]

chosen_exit = ""    # initialises variable with empty string

while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":      # makes the string comparison "case less"
        print("Game Over")
        break               # This action thus terminates the loop, allowing the player to "quit" the game
print("aren't you glad you got out of the room!")

