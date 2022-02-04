"""
Blocks :  Using IF Statements
"""
################################################################################
"""
EXAMPLE: Working with code blocks in Python

when : ends a line, Python needs an indent on the next line, to understand the code inside the block
"""

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))
    print("*" * 80)

################################################################################

name = input("Please Enter Your Name: ")
age = int(input("How old are you, {0}? ".format(name)))   # Turns into number format
print(age)

if age >= 18:
    print("Old enough to vote")
    print("Please put an X in the box")
else:
    print("please come back in {0} years".format(18 - age))

# or other way around
if age < 18:
    print("please come back in {0} years".format(18 - age))
else:
    print("Old enough to vote")
    print("Please put an X in the box")

"""
----------------------------------------------------------------------------------------------------
"""
"""
Working with ELSE IF (elif - in Python) 
"""
if age < 18:
    print("please come back in {0} years".format(18 - age))    # The format calc is replacing the {0} within the string
elif age == 900:
    print("Sorry Master Yoda, you die in Return of the Jedi")
else:
    print("Old enough to vote")
    print("Please put an X in the box")



