########################################################
####               Exponent Function                ####
########################################################


print(2**3) ;  # this is 2 raised to the power of 3  (aka 2 cubed) 


# could create a function to do this 

def raise_to_power(base_num, power_num) :
    
    result = 1 ;
    for index in range(power_num) :     # essentially we will keep multiplying base num by itself as many times as the number in pow_num
        result = result * base_num ;
        
    return result ;

print(raise_to_power(2,3)) ;   # prints 8 as expected 
        

