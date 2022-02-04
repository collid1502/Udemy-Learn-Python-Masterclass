"""
The str Data Type
"""
# a string is a sequence data type, because the letters are in a sequence
# index>> 0123456789  etc. etc.
parrot = "Norwegian Blue"

print(parrot)     # prints the value of parrot
print(parrot[3])  # prints the letter W. Now, this is actually the 4th letter of parrot. By Python indexing starts at 0, so 3 is actually the 4th index position

"""
CHALLENGE 
add some code so that it prints out 'we win' using the parrot = Norwegian Blue, with each character on a separate line 

so it should look like:
w
e 

w
i
n
"""
print(parrot)     # prints the value of parrot
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])    # And the result is: we win

"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------
"""

"""
Negative Indexing in Strings 
"""
# so, negative numbers start from right to left in indexing, rather than left to right (and note, -0 doesnt make sense, so reverse indexing starts at -1)
# for example, a -1 would do:
print(parrot[-1])  # and return the letter 'e' which is the last letter in the string, Norwegian Blue

print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])    # And the result is: we win  (via negative indexing)

"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------
"""

"""
Slicing   -   basically like pulling a substr in SAS 
"""
# index>> 0123456789  etc. etc.
parrot = "Norwegian Blue"

print(parrot[0:6])  # Norweg -  Here we are telling Python to start at position 0 & go up to BUT NOT including position 6

print(parrot[3:5])  # Outputs 'we'

print(parrot[0:9])  # Outputs - 'Norwegian'

"""
Slicing with Negative Numbers 
"""
print(parrot[-4:-2])   # prints 'Bl'   -  prints from index -4 (B) upto but not including 2nd to last char in string (u)
print(parrot[-4:12])   # prints 'Bl'

print(parrot[-14:-8])  # prints out 'Norweg'

"""
Using steps in slices 
"""
# NOTE - a step defaults to 1

print(parrot[0:6:2])   # Outputs: 'Nre' - this is because we are collecting every SECOND (2) character between index 0 & 6 due to specifying :2 in the statement

print(parrot[0:6:3])   # Outputs: 'Nw' - this is because we are collecting every THIRD (3) character between index 0 & 6 due to specifying :3 in the statement
