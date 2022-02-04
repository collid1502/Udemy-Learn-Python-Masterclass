########################################################
####          If Statements & Comparisons           ####
########################################################

# Create a function that prints out the max number, out of those we provide

def max_num(num1, num2, num3):

    if num1 >= num2 and num1 >= num3:
        return num1 ;
    elif num2 >= num1 and num2 >= num3:
        return num2 ;
    else:
        return num3 ;

print(max_num(380, 40, 5)) ;  # Prints the max number out, which is 380 in this example

# Google Python basic comparison operators, but most are basically same as SAS - except = is >>> '=='
