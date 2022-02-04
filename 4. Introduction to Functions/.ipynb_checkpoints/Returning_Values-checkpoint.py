"""
Returning Values
"""

import random

# we create a function to create an integer based on what the user types/inputs 
def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)   # when conditions for return is met, it processes and then leaves loop, rather than running again 
        else:
            print("You have not entered a valid number. Please try again.")

 
highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing.
guess = 0  # initialise to any number that doesn't equal answer
print("Please guess a number between 1 and {}: ".format(highest))
 
while guess != answer:
    guess = get_integer(": ")  # now call function "get_integer" created above & use here 
 
    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:  # guess must be greater than answer
            print("Please guess lower")



# -----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------
"""
Example of a function that sums all of the odd or even numbers, below an entered number, based on user selection 
"""

def sum_eo(n, t):
    """Sum even or odd numbers in range.

    Return the sum of even or odd natural numbers, in the range 1..n-1.

    :param n: The endpoint of the range. The numbers from 1 to n-1 will be summed.
    :param t: 'e' to sum even numbers, 'o' to sum odd numbers.
    :return: The sum of the even or odd numbers in the range.
            Returns -1 if `t` is not 'e' or 'o'.
    """
    if t == "e":
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1

    return sum(range(start, n, 2))


x = sum_eo(11, 'e')
print(x)

# -----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------

"""
Returning None
"""

def multiply(x, y):
    result = x * y 
    return result    # NB. If we do not add the 'return' code here, when we run the function, Python will simply return 'None' to the console


answer = multiply(18, 3) 
print(answer) 

