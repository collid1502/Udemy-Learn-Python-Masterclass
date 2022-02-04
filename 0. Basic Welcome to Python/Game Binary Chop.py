"""
Hi_Lo Game - Random Guessing Game using 'Binary Chop'
"""
low = 1
high = 1000
print("please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1
while low != high:
    print("\tGuessing in the range of {} to {}".format(low, high))    # Spits out the range for which the computers next guess will be the midpoint of
    guess = low + (high - low) // 2    # remember, integer division in Python (//) rounds down
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter H or L, or C if my guess was correct"
                     .format(guess)).casefold()

    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess.
        low = guess + 1

    elif high_low == "l":
        # Guess lower. The high end of the range becomes 1 less than the guess.
        high = guess - 1

    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break    # break from loop once user confirms computer guesses correct answer

    else:
        print("Please enter H, L or C")
        
    guesses = guesses + 1   # Adds 1 to create a tally for the number of guesses the computer is making

else:
    print("You thought of the number {}".format(low))
    print("I got it in {}".format(guesses))
