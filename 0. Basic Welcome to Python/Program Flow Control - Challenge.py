"""
This script is the end of section 4 - Program Flow Control

The following is code in relation to a challenge set against the learnings from this section
"""

print("Please choose your option from the list below:")
print("1:\tLearn Python")   # \t creates tab space before string is written
print("2:\tLearn R")
print("3:\tLearn SAS")
print("4:\tLearn Tableau")
print("5:\tLearn SQL")
print("0:\tExit")

while True:
    choice = input()

    if choice == "0":
        break  # terminates loop is user select 0 to Exit

    elif choice in "12345":
        print("You chose {}".format(choice))

    else:  # This re-prints list if user does not select  a valid option
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")   # \t creates tab space before string is written
        print("2:\tLearn R")
        print("3:\tLearn SAS")
        print("4:\tLearn Tableau")
        print("5:\tLearn SQL")
        print("0:\tExit")

