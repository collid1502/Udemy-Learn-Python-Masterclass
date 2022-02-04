########################################################
####             List Functions                     ####
########################################################

# List Data Setup
lucky_number = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(lucky_number)
print(friends)

############################################################
# common & popular functions on Lists #

# Extend function - allows you to append one list to another
friends.extend(lucky_number)
print(friends)

# You can add individual elements to a list, so for example:
friends.append("Creed")
print(friends)

# Now say you want to add an item into the middle of a list, rather than add on at the end. You can use the Insert function
friends.insert(1, "Kelly")  #So adds Kelly in at Index position 1 in the list
print(friends)

# say we want to remove an element? such as Jim
friends.remove("Jim")
print(friends)  # And now Jim is gone

# remove last element/item from the list   - so Creed goes
friends.pop()
print(friends)

# Clear the whole list
friends.clear()
print(friends)

#####################################################
# List Data Setup
lucky_number = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

# lets say we want to check if an element / item is in our list, so say we want to search and see if Jim is in there
print(friends.index("Jim"))  # retunrs the value 2 - Jim's Index position in the list

print(friends.count("Jim"))  # returns 2 as Jim appears twice

friends.sort() # sorts the list in ascending order
lucky_number.reverse() # sorts in descendng order

friends2 = friends.copy
print(friends2)   #Basically we have created a copy of the Friends List 
