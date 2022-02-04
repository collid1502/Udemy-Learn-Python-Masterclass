"""
Working with code blocks in Python

when : ends a line, Python needs an indent on the next line, to understand the code inside the block
"""

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))
    print("*" * 80)
