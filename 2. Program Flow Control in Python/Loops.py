"""
For Loops & While Loops
"""
import char as char

parrot = "Norwegian Blue"

for character in parrot:
    print(character)


# another loop example
number = input("Please enter a series of numbers using any separators you like: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char
print(separators)

"""
---------------------------------------------------------------------------------------------
"""
# Iterating over a 'RANGE'

for i in range(1, 20):         # up to, but not including 20 - remember that
    print("i is now {}".format(i))

# if trying to do a stepped loop, like a BY in SAS, we can do:

for i in range(1,20, 2):
    print("i is now {}".format(i))

"""
---------------------------------------------------------------------------------------------
"""

"""
Nested For Loops 
"""
# A simple example, multiplication tables
for i in range (1, 13):
    for j in range(1, 13):
        print("{0} times {1} is {2}".format(j, i, i * j))
    print("------------")




