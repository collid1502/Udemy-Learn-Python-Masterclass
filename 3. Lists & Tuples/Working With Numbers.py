########################################################
####        Working with Numbers in Python          ####
########################################################

print(2.097)  # really basic, just prints the number 2 to the console
print(-3.876)

print(3 + 2)  # Simple addition
print(5 - 2)  # Simple subtraction
print(3 * 4)  # Simple multiplication
print(12 / 3) # Simple Division

# can use brackets (much like SAS) to dictate order of operations
print(3 * (2+2))

# We can use the % sign as a modifier to spit out the remainder of an equation, for example
# If we did 10/3 that leaves a remainder of 1, seeing as 3 goes into 10 3 times with 1 left over
# We can indentify and print this 1 as follows
print(10 % 3)

# we can convert a number into a string
my_num = 5
print(str(my_num))

# This comes in handy when we want to print out numbers next to string, for example
print(str(my_num) + " is my fave number")

# Common functions related to Numbers #

## ABS - absolute value of number
print(abs(-5))

## POW allows us to provide a number, then comma, then the number we want to raise the number to i.e. 3 squared
print(pow(3,2))

## MAX/MIN - like SAS, returns the larger/smallest of the numbers we return in to it
print(max(5,10))

## ROUND function - allows us to round our numbers to standard rounding rules
print(round(3.7))    # spits out 4 #

####################################################################################
## In order to get some Maths functions, we need to import into Python ##
## So this is importing external code into our files ##

# This is known as a "Math Module" - which allows us to use a variety of Maths Functions in our code 
from math import *   # This will collect extra maths functions we can use

#Like SAS, can use a floor or Ceil function
print(floor(3.7))  #Prints 3 out
print(ceil(3.7))   #Prints 4 out

#Like SAS, also use Sq Route function
print(sqrt(9))  # Prints 3 out


