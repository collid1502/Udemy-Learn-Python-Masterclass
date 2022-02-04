"""
Tuples - A simple 'Jukebox' example 
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

# REMEMBER -Indexes start at 0... 
print(albums) # check its loaded right 

# Python norms is to use all uppercase to specify a constant variable 
ALBUM_SONGS = 3  # this is the index position of the song list for each album, in each tuple. Rather than hard coding 3 in our programme, 
                 # we can simply set a more meaningful variable name. like the %LET statement in SAS. 

SONG_TITLE_INDEX = 1 

while True:
    print("Please choose your album (ivalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))
    
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice -1][ALBUM_SONGS]   # This creates the song list from the album chosen (aka choice minus 1, to get correct index position)
    else:
        break 
    
    print("Please choose your song:") 
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index +1, song)) 
        
    song_choice = int(input()) 
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice -1][SONG_TITLE_INDEX]
        print("Playing {}".format(title))
    
    print("=" * 40)    # prints nice format line 

