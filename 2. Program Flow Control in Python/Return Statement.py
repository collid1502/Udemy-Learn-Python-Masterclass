########################################################
####                  Return Statement              ####
########################################################

# A return statement can be used in a Python Function
# This can be when we want to get information BACK from a function, i.e. give me info back after executing the task

# Create function to cube a number & return value

def cube(num):
    return num*num*num  ;

result = cube(3) ;
print(result) ;  #Prints the result from the function above - also, you cant run code after the line of the return statement. Python breaks out of the function after the Return code line
