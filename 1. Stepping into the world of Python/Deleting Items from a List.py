
data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

del data[0:2]
print(data)     # we can see that the first 2 entries, index 0 & 1 have been removed

#-----------------------------------------------------------------------------------------

data_ = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

min_valid = 100
max_valid = 200

for index, value in enumerate(data_):
    if (value < min_valid) or (value > max_valid):
        del data_[index]
print(data_)
"""
The above would error  -why???

We can see that neither 5 nor 360 were deleted, why?
Well, as we loop through each Index of the data set, if a data point is removed, the index re-sets. So, at index 0, 
we assess '4' & remove it. The code now goes to assess index 1 from the data list, but value '5' is no longer at 
position index 1, it's now at position index 0, and thus, the code does not process it under the looped search for 
MIN / MAX conditions.

Same happens with 360.
350 gets processed, removed, then all remaining data points move down 1 index space. Seeing as 360 was next, it's not 
actually processed, because it's new index position has just been processed in order to get rid of the 350.
"""

# So, how to safely remove those values in the example above:

data_2 = [4, 5, 104, 105, 110, 120, 130, 130, 150,
         160, 170, 183, 185, 187, 188, 191, 350, 360]

min_valid = 100
max_valid = 200

# process low values in the list
stop = 0
for index, value in enumerate(data_2):
    if value >= min_valid:
        stop = index
        break

print(stop)  # for debugging
del data_2[0:stop]
print(data_2)

"""
So, what did this do?

The for loop searched for the first data point where the value was greater than or equal to the condition.
It then passed the index of that data point into the 'stop' value (prev. set to 0).
Thus, we know we know that, if our list is sorted!!! then we can remove all min values safely, by finding the first 
index position where a value passes the min condition.
Then, we run a delete statement from index 0 up to the newly created stop value.
This provides our list with low values removed.
"""

# What about processing the High values in the list?
# We don't want to have to read through the whole list (could be billions of data points) to find the first value to
# initiate the High condition at. So, we can start backwards:

start = 0
for index in range(len(data) - 1, -1, -1):  # this iterates backwards by 1
    if data[index] <= max_valid:
        # we have the index of the last item to keep
        # so we want to set 'start' position of the first item AFTER last item to keep 
        start = index + 1   # places start value of index position where all values should get removed by max condition
        break
print(start) # for debugging

del data_2[start:]   # deletes all data points on list from index position 'start' till end of the list
print(data_2)

