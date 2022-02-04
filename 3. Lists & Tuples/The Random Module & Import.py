"""
Random Number module
"""
import random

highest = 10
answer = random.randint(1, highest)   # selects a random number between 1 & 10

print("please guess number between 1 and {0}: ".format(highest))
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

