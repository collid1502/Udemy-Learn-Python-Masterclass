"""
3. Escape Characters
"""
splitString = ("This string has been\nsplit over\nseveral\nlines")   # places each part onto a new line
print(splitString)

tabbedString = "1\t2\t3\t4\t5"    # creates tabbed between each part
print(tabbedString)

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")

# or
print(""" The pet shop owner said "No, no, 'e's uh,...he's resting". """)   # using triple quotes


# The below results in the strings being typed over several lines to the console
anotherSplitString = """This string has been 
split over 
several 
line"""
print(anotherSplitString)

# But, we could use backslashes to ensure Python adds them all to one line:
anotherSplitString = """This string has been \
split over \
several \
line"""
print(anotherSplitString)

# Example - printing tabs
Number1 = "Number 1\tThe Larch"
Number2 = "Number 2\tThe Horse Chestnut"
print(Number1)
print(Number2)

# or

print("Number 1\tThe Larch")
print("Number 2\tThe Horse Chestnut")

#################################################################

"""
4. More on Escape Characters in Strings
"""

print(""" The pet shop owner said "No, no, \
 'e's uh,...he's resting". """)                   # you still get the string on one whole line

print("C:\Users\timbuchalka\notes.txt")    # The backslashes are causing problems

# The \ before the t in tim, is causing Python to interpret it as a tabbed character
# The \ before the n is causing Python as a line feed character
# The \U is also causing an issue as Python uses this to include accented chars in strings

print("C:\\Users\\timbuchalka\\notes.txt")    # use backslash to escape the second backslash
print(r"C:\Users\timbuchalka\notes.txt")      # print a raw string
