# -*- coding: utf-8 -*-
"""
Tuples - Intro & Working With
"""
#------------------------------------------------
"""
A tuple is a mathematical name for an ordered set of data.
Remember, being 'ordered' is a requirement for a Python sequence.

Tuples differ from lists because they are 'immutable'. This means that they can't be 
changed after they are created, just like strings.
"""

t = "a", "b", "c"
print(t)    # Note, that the printed output looks like a list, except it uses curly brackets rather than square brackets.
            # This is a way of knowing we are working with a Tuple.

#-----------------------------------------------
# Tuples are immutable 
welcome = "welcomes to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightening", "Metallica", 1984

print(metallica)   # prints the tuple, containing album, artist & release year 

print(metallica[0]) # Prints the index 0 value in the tuple - aka the album name 
print(metallica[1]) # Prints the index 1 value in the tuple - aka artist name 
print(metallica[2]) # Prints the release year from the tuple 


metallica[0] = "Master of Puppets"   # note - if you try to run this, you get an error 
"""
TypeError: 'tuple' object does not support item assignment
"""
# This is because tuples are immuatble!

"""
Note, because tuples dont have the overhead of the methods needed to change them, tuples use less memory than lists.
If using bigger data, this may be one reason why you would rather use a tuple.

Another reason they are useful is that the integrity of your data is protected. If immutable, the underlying data cannot be changed by accident/error!
"""

# We can create a list from our Tuples:
print(list(metallica))   # and you will see a list [] printed containing the arguments. Notice, the release year is left as an integer, because lists can hold multiple types

# And now that you have a list, you can change the album title.
metallica2 = list(metallica) 
metallica2[0] = "Master of Puppets"
print(metallica2)   # change album name, no error occurs now

#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
"""
Unpacking a Tuple
"""
# binding variables 
a=b=c=d=e=f=12 ;
print(c)  # so all values are bound to the value 12 

x,y=1,2 
print(x)  # x is bound to value 1
print(y)  # y is bound to value 2

# The above, is called unpacking a tuple. 
# You can also unpack a List [x,y,z] in the same way, but code can crash if list is longer/shorter than unpcking statement.

"""
practical use for unpacking a tuple 
"""
for index, character in enumerate("abcdefgh"):
    print(index, character)   # prints out 0a, 1b, 2c etc etc
    
    
for t in enumerate("abcdefgh"):
    print(t)    # This builds 8 tuples. Each index position, and each char at that index 
    

"""
more unpacking 
"""
welcome = "welcomes to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightening", "Metallica", 1984

title, artist, year = metallica 
print(title)
print(artist)
print(year) 

#---------------------

# example of calculating area of coffee table from unpacking tuple
table = ("coffee table", 200, 100, 75, 34.50)
print(table[1] * table[2]) 

# a cleaner method for the above would be to do:
table = ("coffee table", 200, 100, 75, 34.50)
name, length, width, height, price = table 
area = length * width 
print(area)    # and we get the answer 20,000 printed to the console 


#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
"""
Nested Tuples & Lists 
"""
albums = [
        "welcomes to my Nightmare", "Alice Cooper", 1975,
        "Bad Company", "Bad Company", 1974,
        "Nightflight", "Budgie", 1981,
        "More Mayhem", "Emilda May", 2011,
        "Ride the Lightening", "Metallica", 1984,
        ]
# now, the above are not yet tuples, it is just one long list. We can check this by doing:
print(len(albums))  # which outputs 15, rather than the desired 5 

# so, using () to create the tuples 
albums = [
        ("welcomes to my Nightmare", "Alice Cooper", 1975),
        ("Bad Company", "Bad Company", 1974),
        ("Nightflight", "Budgie", 1981),
        ("More Mayhem", "Emilda May", 2011),
        ("Ride the Lightening", "Metallica", 1984),
        ]
print(len(albums))  # which outputs 5, which we wanted 

for album in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(album[0], album[1], album[2]))

# a tidier way to do this would be to unpack the tuples, rather than referencing specific indexes
albums = [
        ("welcomes to my Nightmare", "Alice Cooper", 1975),
        ("Bad Company", "Bad Company", 1974),
        ("Nightflight", "Budgie", 1981),
        ("More Mayhem", "Emilda May", 2011),
        ("Ride the Lightening", "Metallica", 1984),
        ]
for (name, artist, year) in albums:              # inside the brackets, unpacks the tuple in indexed order. i.e. name=0, artist=1, year=2 
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

# *************************************************
"""
Nesting Further - adding a list of songs to our Albums data example
"""
albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]
for (name, artist, year,songs) in albums:
    print("Album: {}, Artist: {}, Year: {}, songs: {}"
          .format(name, artist, year, songs))

# can index into the list of songs to get any one particular song 
album = albums[2]   
print(album)       # This collects the 3rd album from above list :  "Nightflight" 

# collect the list of songs from that album 
songs = album[3] 
print(songs)   # This prints the 4th item aka songlist (index=3) of the 3rd album from the album list 

# collect an individual song 
song = songs[1] 
print(song)    # collects the 2nd song, from the list of songs, from the 3rd album of the albums list 


"""
Nested Indexing 
"""
# or, put another way, you could just do 'nested indexing': 
print(albums[2][3][1])

# ******************************************************************
# Exercise 
print(albums[1][3][5][1])  # Prints 'The way I Choose' 
print(albums[2][2])        # Prints the year album 'Nightflight' was realased 
print(albums[3][3][3][0])  # Prints track number of 'Kentish Town Waltz' from 'More Mayhem' album 
print(albums[2][3][1])     # Prints the tuple (2, "Keeping a Rendezvous")

