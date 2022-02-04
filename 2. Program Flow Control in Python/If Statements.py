########################################################
####                  If Statements                 ####
########################################################

# Using if statements to help the program make decisions on when to execute code based on certain elements etc.

is_male = True ;  # Boolean variable, set equal to true

if is_male:
    print("You are a Male") ;  # So because is_male is True, this will run & print. If it was false, then it would print blank.

else:
    print("You are not a Male") ;  # Prints the else statement reflecting the other side of the rule

################################################################################################

## More Complex versions
is_male = True
is_tall = True

if is_male or is_tall:    # aka - if the person is male and/or is tall ... then do something  - much like SAS conditional statements, can use a variety of And/Or and so on
    print("You are a male or you are tall") ;
else:
    print("You are neither male nor tall") ;

#########################################

# Now lets change this to include an "else if" statement

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male") ;
elif is_male and not(is_tall):
    print("You are male, but not tall");
elif not(is_male) and is_tall:
    print("You are not male, but you are tall");
else:
    print("You are neither male or tall");

