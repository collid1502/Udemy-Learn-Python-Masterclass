########################################################
####                     For Loops                  ####
########################################################


# A for loop is a special type of loop in python that lets you loop over different collections, such as letters in a string, 
# or an array etc.


# state for & specify a variable - which will be used on each iteration of the for loop 

for letter in "Giraffe Academy": 
    print(letter) ;
    
# this basically pints out each letter in the string, Giraffe Academy 


friends = ["Jim","Karen","Kevin"] ;

for name_ in friends :       # name_ - cane be called whatever you want 
    print(name_) ;
    

for index in range(10):
        print(index) ;   # notice, this prints every number from 0 to 9 into the console, so up to 10, but NOT including!


for index in range(3, 10):
    print(index) ;           # prints all values from 3 up to but not including 10 


# so, we have 3 friends in our list. 
# How could we print the index numbers for each number from 0, up to the number of friends in our list?
    
friends = ["Jim","Karen","Kevin"] ;

for index in range(len(friends)) : 
    print(index) ;                  # will print out the 0, 1 & 2  as expected
    
    
# or, we could actually loop through and print out each of the names in the friends array 
    
for index in range(len(friends)) :
    print(friends[index]) ;    # this essentially prints the friend name, which is indexed to the same value of 'Index' during the loop
    
    
######################################################################################
    
# we can actually use iterations of the loops to do certain things as well, like print certain messages, for example:
    
for element in range(5) :
    if element == 0 :
        print("This is the first Loop Iteration") ;
        
    else:
        print("This is Not the First Loop Iteration") ;
        

    
