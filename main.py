import lyricsgenius as lg # https://github.com/johnwmillr/LyricsGenius
import musicbrainzngs, json, music_functions
from config import genius_key

file = open("lyrics_1.txt", "w")  # File to write lyrics to
genius = lg.Genius(genius_key,  # Client access token from Genius Client API page
                             skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                             remove_section_headers=True)
musicbrainzngs.set_useragent("Lyric Counter App", "0.1", "https://github.com/xtenanetx")


if __name__ == "__main__":
    song_list = []
    song_input = ''
    artist = input("Enter artist name: ")

    while(1):
        song_input = input("Enter song by " + artist + " or !q to start searching: ")
        if(song_input == ""): break
        
        song_list.append(song_input)

    if(song_list != []):
        music_functions.count_words(artist, song_list, genius)
    else:
        print("No songs entered.")