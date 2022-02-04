# -*- coding: utf-8 -*-
"""
The Reversed Function
"""

data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]

min_valid = 100
max_valid = 200 

for index, value in enumerate(reversed(data)):
    print(index, value)
    
print(data) 

# so the 108 is index 0 = because we are starting from the end of the list now

#---------------------------------------------------------------------------------------------------

# To get the actual indexes (but still reverse order of data), we could do:
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    print(top_index - index, value)

print(data)

# Notice now that 108 still gets printed first, but it's index is shown as 12, rather than 0 now.

#--------------------------------------------------------------------------------------------------

# So now we want to run a loop to get rid of values outside the min & max valid set above 
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]

print(data)

# So, notice that, as we are working backwards, the value 306 [at index 9] is dropped first.
# Then we drop the value 5 [at index 6] and so on ...
# Finally a new list is printed, with outlier values removed
