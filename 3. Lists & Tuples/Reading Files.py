#####################################################################
####                Reading & Writing to Files                   ####
#####################################################################


# Lets say we want to read in a file, well, first, we have to actually open the file within python 

open("location......\The Office - Dummy Data.txt", "r") # just wants to read info from file

##  r is read 
##  w is write - aka can modify file 
##  a is append - aka add stuff to file
##  r+ is read & write 

# now we might want to read this file into a variable so:

employee_file = open("The Office - Dummy Data.txt", "r") # when file is in same location as Python Script - but not working for me atm??

employee_file.close() ; # best practice is to close file after finished using it 

##########################################################
## So, some examples 

employee_file = open("The Office - Dummy Data.txt", "r")

print(employee_file.readable()) ; # Prints True or False as to whether we can read the file or not 

print(employee_file.read()) ;


# could read first line only, for example
print(employee_file.readline()) ;   # will read first line of file
print(employee_file.readline()) ;   # will then read second line of file 

# we can read ALL lines into an Array 
print(employee_file.readlines()) ;   # reads each lines and places it into an array 

# so, to then get a specific line, could refer to its index from the array , REMEMBER Index starts at 0 in Python 
print(employee_file.readline()[1]) ; # would produce the Dwight - Salesman (second line) of file 


####################################################################################################################
####################################################################################################################
####################################################################################################################

# so, we want to add an employee to the file

employee_file = open("The Office - Dummy Data.txt", "a")  # lets us append to file 

employee_file.write("Toby - HR Rep") ;

employee_file.close() ;

# add another employee to a new line, not in a current line 
employee_file.write("\nToby - HR Rep") ;   # the \n will create a new line before writing the text 

# be carefule with w - it will just overwrite eveything already in the file , should use a (append) for adding stuff 




