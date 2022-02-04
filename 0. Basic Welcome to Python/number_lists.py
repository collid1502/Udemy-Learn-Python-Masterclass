#
# Common sequence operations
#

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

print(min(even))
print(max(even))

print(min(odd))
print(max(odd))

print()  # blank line print
print(len(even))  # result = 4 prints the number of objects in the list rather than the 'length' of a char/variable
print(len(odd))   # result = 5

print()
print("mississippi".count("s"))   # result = 4 's' exist in the string

#-------------------------------------------------------------------------------------------

# Creating Lists

empty_list = []
even_ = [2, 4, 6, 8]
odd_ = [1, 3, 5, 7, 9]

numbers_ = even_ + odd_
print(numbers_)

sorted_numbers_ = sorted(numbers_)  # All numbers within list now in order, but in a "new" list
print(sorted_numbers_)
print(numbers_)

digits = sorted("432985617")   # creates a list of strings, sorted in order
print(digits)

# an efficient method for creating a 'copy' of a list would be to do:
more_numbers_ = numbers_.copy()

