########################################################
####       Building a Basic Calculator              ####
########################################################

num1 = input("Enter a number: ")
num2 = input("Enter a second number: ")

result = num1 + num2
print(result)

# notice, when you type in 5 and 8.3 as your user entered numbers, the outcome is 58.3 which is WRONG!
# but why???
# essentially, Python defaults to string for user input, so we need to change this to a number in order to calculate properly
# so, convert the strings into numbers:
# can use the int() function for whole numbers
# can use float for decimal if needed

num1 = input("Enter a number: ")
num2 = input("Enter a second number: ")

result = float(num1) + float(num2)
print(result)
# now you get the correct 13.3 as the result output 
