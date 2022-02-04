########################################################
####                Try Except                      ####
########################################################


# Being able to catch erros/exceptions in Python
# So we can handle errors and do things when they occur


# Example - get user to enter a number 

number = int(input("Enter a Number: ")) ;
print(number) ;


'''
But let's say someone enters text, like the letter a - well Python throws an error. Looking like:
    
Traceback (most recent call last):

  File "<ipython-input-2-96c88bb8b72f>", line 1, in <module>
    number = int(input("Enter a Number: ")) ;

ValueError: invalid literal for int() with base 10: 'a'  

So, how can we handle this error?

A try except block 
'''

try: 
    score = 77/100    # now this will throw an error, so to catch it with a correct except, we can do:
    number = int(input("Enter a number: ")) 
    print(number) 
    
except ZeroDivisionError:
    print("Divided by Zero") 
    
except ValueError:
    print("Invalid Input") 



