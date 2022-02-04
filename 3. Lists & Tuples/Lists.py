########################################################
####             Working with Lists                 ####
########################################################

# Create a list, say of friends
friends = ["Mitch", "James", "Conall", "Serge"]

# You can basically put anything inside a list, i.e. strings, numbers, booleans

## accessing individual elements inside our created list by using the index on the list. Remember indexing in Python starts at Index 0
print(friends[1])  # should return James

# can select an index range, so if we wanted conall &n serge we could do from index 2 to OPEN (which defaults as end of list) so 2:
print(friends[2:])

# we could trial a selection such as 1 to 3 aka 1:3
print(friends[1:3])  #This would return James & Conall as it starts at Index 1 and finishes before Index 3

###########################
# say we want to modify one of the elements, say turn Mitch into Connor, we can do that as so:
friends[0] = "Connor"
print(friends) # And now you see Connor output in the list instead of Mitch



