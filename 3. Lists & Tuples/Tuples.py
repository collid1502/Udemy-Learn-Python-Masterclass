########################################################
####               Tuples                           ####
########################################################

# a Tuple is a type of data structure
# It is very similar to a list

# Creating a Tuple:
## To create a Tuple in Pythin, we place between parenthases
coordinates = (4, 5)

# Tuple are Immutable (aka they are unchangeable)
print(coordinates[0])   #Tuples are indexed starting at 0. So 4 (in the example above) is index 0
print(coordinates[1])    #Prints 5

#So, if you tried to change the Tuple, for example:
coordinates[1] = 10  #Trying to change the 5 to a 10, Python will throw an error message at you

## Difference between Tuples () & Lists []
# Generally people use Lists for stuff that needs to change
# Where as people use Tuples for stuff not designed to change, aka the Cooridnates example, as coordinates probably wont change
