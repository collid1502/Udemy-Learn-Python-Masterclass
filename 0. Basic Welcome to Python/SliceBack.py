"""
Slicing Backwards
"""
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]   # Prints the string from right to left, omitting letter A because we used stop value 0 (remember - upto NOT including)
print(backwards)

# So, to include the letter 'a'
# we omit the 'stop' value. Python is clever enough to work out that if we place no stop value, read to the end of the string

# so:
backwards = letters[25::-1]
print(backwards)      # will now print all 26 letters backwards   (remember - 25 is the index position of 'Z' because indexing starts at 0 in Python


"""
Challenge
1) create a slice that produces the characters 'qpo' 
2) slice the string to produce 'edcba' 
3) slice the string to produce the last 8 characters, in reverse order 
"""
# Answer 1
answer1 = letters[16:13:-1]
print(answer1)   # prints 'qpo'

# Answer 2
answer2 = letters[4::-1]
print(answer2)   # prints 'edcba'

# Answer 3
answer3 = letters[25:17:-1]   # or could have used - letters[:-9:-1] to get same answer
print(answer3)   # prints 'zyxwvuts'


"""
Common Python Idioms for Back Slicing 

get the  last <n> characters from a string :  print(<string>[-<n>:])  - produces final <n> chars from string 
get the first <n> characters from a string :  print(<string>[:<n>])   - produces the first <n> chars from string 
"""

"""
Note - Python 3 has Five sequence types built in:
1 - The String Type 
2 - List
3 - Tuple
4 - Range 
5 - Bytes & Bytearray
"""
