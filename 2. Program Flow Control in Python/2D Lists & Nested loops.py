########################################################
####           2D Lists & Nested Loops              ####
########################################################


number_grid = [
    
    [1, 2, 3],   # each one of these is lists within a list.   aka rows and columns in a grid like structure 
    [4, 5, 6],
    [7, 8, 9],
    [0] 
    
    ]

# print(number_grid[index for row][index for the column])

print(number_grid[2][1]) ;   # this would print 8 - why?

# well remember, indexes start at 0 in Python.
# so, first row (1,2,3) is index 0, likewise first column (1,4,7,0) is index 0 .
# so, the number 8, in the grid, belongs to 3rd row (indexed as 2) and 2nd column (indexed as 1) 

##########################################################################################################

# Nested for loops are basically for loops inside a for loop 

for row in number_grid :
    for col in row:
        
        print(col) ;  # prints all numbers out to the console, across the number grid 
        
        