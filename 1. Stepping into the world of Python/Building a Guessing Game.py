########################################################
####           Building a Guessing game             ####
########################################################

# Here we will use a lot of the tips already learned in order to build a game

# This game will be where a user can guess the secret word 


secret_word = "giraffe" ;  # stored secret word 

guess = "" ;   # empty place for user to enter secret word 



while guess != secret_word :    # keep looping till correct word guessed  - note != is same as not equals <>/^= 
    guess = input("Enter guess: ") 

print("You win!") ;



##########################################
## now, lets say we want a limit on how many times they can guess the word
## if they di it within 3 guesses they win, if not, they lose 

secret_word = "giraffe" ;  # stored secret word 

guess = "" ;   # empty place for user to enter secret word 

guess_count = 0  ;  # rolling the count of guesses by the user 

guess_limit = 3 ;   # max 3 guesses before losing 

out_of_guesses = False ;  # a boolean on whether or not the user is out of guesses 


while guess != secret_word and not(out_of_guesses):    # keep looping till correct word guessed or out of guesses  
    
    if guess_count < guess_limit :   # if true, keep letting them guess 
        guess = input("Enter guess: ") 
        guess_count = guess_count + 1 ;   # after each loop/guess add a count to the rolling value 
        
    else:
        out_of_guesses = True ;

# so, now we need to print the relevant "You Win" or "You Lose" etc messages based on what has happened above 
        
if out_of_guesses :
    print("Out of guesses, you Lose!") ;
else:
    print("You win!") ;
    


