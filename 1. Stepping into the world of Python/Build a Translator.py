########################################################
####          Build a Translator                    ####
########################################################


# Build a basic translator in Python 

# Made up language - called Giraffe #
#
# so, in this language, any vowel gets translated to a g #
# vowels = g ;

# so
# dog -> dgg
# cat -> cgt    etc. 

###########################################################################

def translate(phrase):
    
    translation = "" 
    # so we now want to loop through phrase, then add each letter to translation, 1 by 1 after checking if its a vowel or not 
    
    for letter in phrase:
        if letter in "AEIOUaeiou":
                translation = translation + "g" 
            
        else:
            translation = translation + letter 
            
    return translation ;

print(translate(input("Enter a Phrase:"))) ;

# now - when you enter a phrase, any vowel gets switched to a g 

#########################################################################

# however, we face an issue. If the entered phrase starts with an uppercase vowel, it's switched to lowercase g, rather than UC G, 
# so lets fix it

def translate(phrase):
    
    translation = "" 
 
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G" 
            else:
                translation = translation + "g" 
            
        else:
            translation = translation + letter 
            
    return translation ;

print(translate(input("Enter a Phrase:"))) ;

# end #