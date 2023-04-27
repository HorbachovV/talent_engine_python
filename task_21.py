# DJ helper tool

# Create get_song() helper function that takes two parameters - dictionary with songs (see below) and integer argument which is a maximum length of a song in seconds.

# songs is an array of objects which are formatted as follows:
# {
#  'artist': 'Artist', 
#  'title': 'Title String', 
#  'playback': '04:30' 
# }
# You can expect playback value to be formatted exactly like above.

# Result should be a title of the longest song from the database that matches the criteria of not being longer than specified time. If there's no songs matching criteria in the database, return False.

songs_db = [ {
 'artist': 'Led Zeppelin', 
 'title': 'Stairways to heaven', 
 'playback': '09:20' 
}, {
 'artist': 'Metallica', 
 'title': 'Master of puppets', 
 'playback': '04:30' 
}, {
 'artist': 'Nirvana', 
 'title': 'The Man who sold the world', 
 'playback': '03:10' 
}, {
 'artist': 'Stepan Galyabarda', 
 'title': 'Lyst do mamy', 
 'playback': '02:20' 
}]

def get_song(db, len_seconds):
    # ...
    filtered_db = [song for song in db if (int(song['playback'][:2]) * 60 + int(song['playback'][3:]) <= len_seconds)]
    if filtered_db:
        longest_song = max(filtered_db, key=lambda x: int(x['playback'][:2]) * 60 + int(x['playback'][3:]))
        return "Best possible song: {}/{}".format(longest_song['artist'], longest_song['title'])
    else:
        return False

print(get_song(songs_db, 145))