"""
Guessing Game  - If, Else If & Else
"""

answer = 5
print("please guess number between 1 and 10: ")
guess = int(input())   # converts to integer

if guess < answer:
    print("Please guess higher")
elif guess > answer:
    print("Please guess lower")
else:
    print("You got it first time!")

##############################################

# Adding a second guess, if you get the first wrong
if guess < answer:
    print("Please guess higher")
    guess = int(input())
    if guess == answer:                        # to test for equality - need to use two = signs >>> ==
        print("Well done, you guessed it")
    else:
        print("Sorry, wrong again")
elif guess > answer:
    print("Please guess lower")
    guess = int(input())
    if guess == answer:                        # to test for equality - need to use two = signs >>> ==
        print("Well done, you guessed it")
    else:
        print("Sorry, wrong again")
else:
    print("You got it first time!")

"""
-------------------------------------------------------------------------------------------------------------
"""
"""
Conditional Operators in Python 

Less Than              ||   < 
Less Than or Equal To  ||   <= 
Greater Than           ||   >
Greater Than or Eq to  ||   >=
Equal To               ||   ==
Not Equal To           ||   != 
"""

answer = 5
print("please guess number between 1 and 10: ")
guess = int(input())   # converts to integer

if guess != answer:                          # where guess is not equal to answer
    if guess < answer:                       # where guess was less than answer value
        print("Please guess higher")
    else:                                    # where guess was higher than answer value
        print("Please guess lower")
    guess = int(input())                     # opportunity for second guess
    if guess == answer:                      # checks if second guess now matches answer
        print("well done, guessed it in two")
    else:                                    # if second guess does not match answer, print wrong again statement
        print("sorry, you got it wrong again")
else:                                        # this is where first guess equals answer, so prints right first time
    print("You got it first time!")

