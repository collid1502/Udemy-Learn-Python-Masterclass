"""
Sorting Lists
"""

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
print(even)  # the list now contains all values (but not in order)

even.sort()
# even.sort(reverse=True)  - would sort in reverse order
print(even)  # now the list is sorted

####################################################################

"""
Sorting Strings 
"""

pangram = "The quick brown fox jumps over the lazy dog"   # contains all letters of alphabet

letters = sorted(pangram)
print(letters)   # note, upper case letters sort before lower case letters & blanks sort first

"""
Creating a NEW sorted List 
"""
numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)     # NB - 'sort' & 'sorted' work differently >> 'sort' would be >> numbers.sort() / print(numbers)  which isn't creating a new variable/list
print(sorted_numbers)


"""
Case Insensitive Sorting Example
"""
missing_letter = sorted("The quick brown fox jumps over the lazy dog",
                        key=str.casefold)   # This argument creates a sort where cases does not matter

# Example 2
names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]
names.sort(key=str.casefold) # case insensitive sorting function
print(names)
