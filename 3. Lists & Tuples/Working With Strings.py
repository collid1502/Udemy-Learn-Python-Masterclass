########################################################
####        Working with Strings in Python          ####
########################################################

print("Dan\nCollins")   # The \n creates a New Line in the output between the two words

# If we want to print a quotation mark, we need to use the backslash to tell Python to disregard the quotation mark as the actual string end
# For example:
print("Dan Collins said \"No Way Mate\"")

# Create string variable
Phrase = "Dan Collins"
print(Phrase)

# Concatanation
print(Phrase + " is 27 years old")

##################################################################################
##
# A Function is a specific block of code that will perform an operation for us
##
print(Phrase.upper())  # Turns the phrase/string to Upper Case

# We can also check if a string is all upper or all lowercase etc.
print(Phrase.isupper())    # Should say False back

# So, we could convert the string to Upper case first, then run a check to collect a True Value to indicate the string is all upper case
print(Phrase.upper().isupper())


# Can find the length of the string
print(len(Pharse))

# Collect individual characters from a string, say the 1st character  { like a SAS substr(<variable>,1,1) }
Print(Phrase[0])   # This is essentially an Index on the string, and in Python the index starts at 0 (not 1 like in SAS)

# Index function (like SAS) tells us where a specific character/string is located
print(Phrase.index("C"))  # So will return the position where first capital C appears


# Replace function
print(Pharse.replace("Dan", "Daniel"))   # So we are replacing 'Dan' with 'Daniel' inside our String
