import lyricsgenius as lg # https://github.com/johnwmillr/LyricsGenius
import musicbrainzngs, json
from config import genius_key

file = open("lyrics_1.txt", "w")  # File to write lyrics to
genius = lg.Genius(genius_key,  # Client access token from Genius Client API page
                             skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                             remove_section_headers=True)
musicbrainzngs.set_useragent("Lyric Counter App", "0.1", "https://github.com/xtenanetx")

def count_words(artist_name, song_titles):
    total_word_list = []
    total_word_count = 0
    total_song_length = 0
    for x in song_titles:
        songs = [genius.search_song(x, artist_name)]
        if songs[0] is None: continue
        mb_metadata = musicbrainzngs.search_recordings(query=x, artist=artist_name, limit=1)
        song_length = int(mb_metadata["recording-list"][0]["length"])
        word_list = []
        word_count = 0
        s = [song.lyrics for song in songs]
        for song in s:
            start_found = False
            for word in song.split():
                if not start_found:
                    if word != "Lyrics": continue
                    start_found = True
                    continue
                word = word.replace('"', "")
                word = word.strip(",.…!?")
                word_count += 1
                if word not in word_list:
                    word_list.append(word)

                if word not in total_word_list:
                    total_word_list.append(word)

        final_word = word_list.pop()
        if(final_word.endswith("Embed")):
            final_word = final_word.removesuffix("Embed")
            while(final_word[len(final_word)-1].isnumeric()):
                final_word = final_word[:-1]
        final_word = final_word.strip(",.…!?")
        if final_word not in word_list:
            word_list.append(final_word)

        if(word_list[len(word_list)-3 : len(word_list)] == ["might", "also", "like"]):
            word_list = word_list[:-3]
            final_word = word_list.pop()
            final_word = final_word[:-3]
            final_word = final_word.strip(",.…!?")
            if final_word not in word_list:
                word_list.append(final_word)


        total_word_count += word_count
        total_song_length += song_length
        print("Unique Words: " + str(len(word_list)))
        print("Total Words: " + str(word_count))
        print("Unique %: " + str(round(len(word_list) / word_count * 100, 2)))
        print("WPM: " + str(word_count / (song_length / 60000)))
        print("----------------------------------------------------")
    if(len(song_titles) > 1):
        print("Total Unique Words: " + str(len(total_word_list)))
        print("Overall Word Count: " + str(total_word_count))
        print("Unique %: " + str(round(len(total_word_list) / total_word_count * 100, 2)))
        print("Total WPM: " + str(total_word_count / (total_song_length / 60000)))

song_list = ["Tequila"]
count_words("The Champs", song_list)