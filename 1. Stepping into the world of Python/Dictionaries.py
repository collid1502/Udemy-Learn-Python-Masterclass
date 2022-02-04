########################################################
####                   Dictionaries                 ####
########################################################


# a Dictionary is a special structure in Python, which allows us to store information in "Key Value Pairs".

# So to access a specific piece of info in the Dictionary, can simply just reference its Key


# For example, a dictionary that converst a 3 month code name to the full name
# basically like a SAS proc format.

monthconversions = {
    
    "Jan": "January" ,
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    }

# so now we can access them from the dictionary 

print(monthconversions["Nov"])  # will return full Novemeber entry  

# or can use 

print(monthconversions.get("Dec"))  # To return Full December dictionary value 


# note, not every value might match to they key from the dictionary, so we can pass a default outcome should this happen, for example:
print(monthconversions.get("Lov", "Not a Valid Key"))   # and as its not a valid key, it will spit out that second part to the console


# Also, much like SAS proc format, dictionaries dont need to be strings.
# They can be numbers, for example:

monthconversions2 = {
    
    1: "January" ,
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
    }

print(monthconversions2.get(3, "Not a Valid Key"))     # prints March to console 



