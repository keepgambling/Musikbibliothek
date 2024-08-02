import Songs

class MusicLibrary:
    def __init__(self):
        # Erstellen von Listen für Songs und Favoriten
        self.songs = Songs.songs
        self.favorites = []

    # Funktion zum Hinzufügen von Songs
    def add_song(self, title, artist, genre):
        song = {
            'title': title,
            'artist': artist,
            'genre': genre
        }
        self.songs.append(song)
        self.sort_songs()
        print(f"Song '{title}' von {artist} im Genre '{genre}' hinzugefügt und sortiert.")

    # Funktion um Songs aus der Bibilithek zu löschen
    def delete_song(self, title):
        song = next((song for song in self.songs if song['title'].lower() == title.lower()), None)
        if song:
            self.songs.remove(song)
            self.sort_songs()
            print(f"Song '{title}' gelöscht und Liste sortiert.")
        else:
            print(f"Song '{title}' nicht gefunden.")

    # Funktion welche alle Songs der Bibiliothek aufgibt
    def list_songs(self):
        print("\nListe der Songs:")
        for idx, song in enumerate(self.songs, start=1):
            print(f"{idx}. {song['title']} - {song['artist']} ({song['genre']})")

    # Funktion welche Songs sortiert 
    def sort_songs(self):
        self.songs.sort(key=lambda x: (x['title'].lower(), x['artist'].lower(), x['genre'].lower()))

    def search_song(self, search_term):
        results = [song for song in self.songs if search_term.lower() in song['title'].lower() or search_term.lower() in song['artist'].lower() or search_term.lower() in song['genre'].lower()]
        if results:
            print("\nSuchergebnisse:")
            for idx, song in enumerate(results, start=1):
                print(f"{idx}. {song['title']} - {song['artist']} ({song['genre']})")
        else:
            print("Keine Songs gefunden.")

    # Funktion um Song zu den Favoriten hinzuzufügen
    def add_favorite(self, title):
        song = next((song for song in self.songs if song['title'].lower() == title.lower()), None)
        if song and song not in self.favorites:
            self.favorites.append(song)
            print(f"Song '{title}' zu Favoriten hinzugefügt.")
        else:
            print("Song ist entweder nicht in der Bibliothek oder bereits in den Favoriten.")

    # Funktion um Song aus den Favoriten zu entfernen
    def remove_favorite(self, index):
        if 0 <= index < len(self.favorites):
            removed_song = self.favorites.pop(index)
            print(f"Song '{removed_song['title']}' aus den Favoriten entfernt.")
        else:
            print("Ungültige Nummer.")

    # Funktion welche die Titel der Favoriten ausgibt
    def list_favorites(self):
        print("\nListe der Favoriten:")
        for idx, song in enumerate(self.favorites, start=1):
            print(f"{idx}. {song['title']} - {song['artist']} ({song['genre']})")

# Function to manage songs
def manage_songs(library):
    while True:
        print("\nTitel verwalten")
        print("1. Titel anzeigen")
        print("2. Titel hinzufügen")
        print("3. Titel löschen")
        print("4. Zurück")
        title_choice = input("Wähle eine Option: ")
        if title_choice == '1':
            library.list_songs()
        elif title_choice == '2':
            title = input("Gib den Titel des Songs ein: ")
            artist = input("Gib den Interpreten des Songs ein: ")
            genre = input("Gib das Genre des Songs ein: ")
            library.add_song(title, artist, genre)
        elif title_choice == '3':
            title = input("Gib den Titel des zu löschenden Songs ein: ")
            library.delete_song(title)
        elif title_choice == "4":
            break
        else:
            print("Ungültige Option.")

# Function to search for songs
def search_songs(library):
    while True:
        print("\nTitel suchen")
        print("1. SUCHALGORiTHMUS 1")
        print("2. SUCHALGORITHMUS 2")
        print("3. SUCHALGORiTHMUS 3")
        print("4. Zurück")
        search_choice = input("Wähle eine Option: ")
        if search_choice == '1':
            print("SUCHALGORiTHMUS 1")
        elif search_choice == '2':
            print("SUCHALGORiTHMUS 2")
        elif search_choice == '3':
            search_term = input("Gib den Suchbegriff ein (Titel, Interpret oder Genre): ")
            library.search_song(search_term)
        elif search_choice == '4':
            break
        else:
            print("Ungültige Option.")

# Function to manage favorites
def manage_favorites(library):
    while True:
        print("\nFavoriten verwalten")
        print("1. Favoriten anzeigen")
        print("2. Song zu Favoriten hinzufügen")
        print("3. Song aus Favoriten entfernen")
        print("4. Zurück")
        fav_choice = input("Wähle eine Option: ")
        if fav_choice == '1':
            library.list_favorites()
        elif fav_choice == '2':
            title = input("Gib den Titel des Songs ein: ")
            library.add_favorite(title)
        elif fav_choice == '3':
            library.list_favorites()
            index = int(input("Gib die Nummer des zu entfernenden Songs ein: ")) - 1
            library.remove_favorite(index)
        elif fav_choice == '4':
            break
        else:
            print("Ungültige Option.")

# Function to create a playlist
def create_playlist(library):
    playlist_name = input("Gib den Namen der neuen Playlist ein: ")
    library.create_playlist(playlist_name)
    while True:
        print("\nPlaylist erstellen")
        print("1. Titel Auswählen") # Titel einzeln auswählen mit Suchalgorithmus -> als Liste NAME DER PLAYLIST EINZIGARTIG
        print("2. zufällige Titel einer Genre")
        print("3. zufällige Titel eines Künstlers")
        print("4. Zurück")
        create_play_choice = input("Wähle eine Option: ")
        if create_play_choice == '1':
            song_title = input("Gib den Titel des Songs ein: ")
            library.add_song_to_playlist(playlist_name, song_title)
        elif create_play_choice == '2':
            genre = input("Gib das Genre ein: ")
            num_songs = int(input("Anzahl der hinzuzufügenden Songs: "))
            library.add_random_songs_by_genre(playlist_name, genre, num_songs)
        elif create_play_choice == '3':
            artist = input("Gib den Namen des Künstlers ein: ")
            library.add_songs_by_artist(playlist_name, artist)
        elif create_play_choice == '4':
            break
        else:
            print("Ungültige Option.")

# Function to adjust a playlist
def adjust_playlist(library):
    playlist_name = input("Gib den Namen der Playlist ein: ")
    if playlist_name not in library.playlists:
        print("Playlist existiert nicht.")
        return

    while True:
        print("\nPlaylist anpassen")
        print("1. Titel hinzufügen") # Zuerst Playlist auswählen und dann Titel angeben
        print("2. Titel entfernen") # Zuerst Playlist auswählen und dann Titel angeben
        print("3. Zurück")
        adjust_play_choice = input("Wähle eine Option: ")
        if adjust_play_choice == '1':
            song_title = input("Gib den Titel des Songs ein: ")
            library.add_song_to_playlist(playlist_name, song_title)
        elif adjust_play_choice == '2':
            song_title = input("Gib den Titel des zu entfernenden Songs ein: ")
            playlist_songs = library.playlists.get(playlist_name, [])
            song = next((song for song in playlist_songs if song['title'].lower() == song_title.lower()), None)
            if song:
                library.playlists[playlist_name].remove(song)
                print(f"Song '{song_title}' aus Playlist '{playlist_name}' entfernt.")
            else:
                print(f"Song '{song_title}' nicht in Playlist '{playlist_name}' gefunden.")
        elif adjust_play_choice == '3':
            break
        else:
            print("Ungültige Option.")

# Function to manage playlists
def manage_playlists(library):
    while True:
        print("\nPlaylist verwalten")
        print("1. Playlist erstellen")
        print("2. Playlist anpassen")
        print("3. Playlist löschen")
        print("4. Zurück")
        play_choice = input("Wähle eine Option: ")
        if play_choice == '1':
            create_playlist(library)
        elif play_choice == '2':
            adjust_playlist(library)
        elif play_choice == '3':
            playlist_name = input("Gib den Namen der zu löschenden Playlist ein: ")
            library.delete_playlist(playlist_name)
        elif play_choice == '4':
            break
        else:
            print("Ungültige Option.")

# Main function to manage the entire library
def main():
    library = MusicLibrary()
    print("Willkommen zu Ihrer Musikbibliothek")

    while True:
        print("\nHauptmenü")
        print("1. Titel verwalten")
        print("2. Titel suchen")
        print("3. Favoriten verwalten")
        print("4. Playlist verwalten")
        print("5. Programm beenden")

        main_choice = input("Wähle eine Option: ")

        if main_choice == '1':
            manage_songs(library)
        elif main_choice == '2':
            search_songs(library)
        elif main_choice == '3':
            manage_favorites(library)
        elif main_choice == '4':
            manage_playlists(library)
        elif main_choice == '5':
            print("Programm beendet.")
            break
        else:
            print("Ungültige Option. Bitte versuche es erneut.")

if __name__ == "__main__":
    main()


# Playlist erstllen NAME DER PLAYLIST EINZIGARTIG!
    # Mithilfe von Filtern Songs Auswählen
    # Song suche
# Playlist oder Favoriten "abspielen" ITERATOR
    # abspielen mit iter()
    # vllt zufälliges abspielen
# hinzufügen von Songs durch Datei vllt Zugrunde Ligende Datei
# Such algorythmen hinzufügen AKTUELLE SUCHFUNKTION ÄNDERN!!!!
    # binär
    # linear
# Begrenzung bei Genre (vorgegbene Genres)

# Speichern von Songs, Playlist und Fvoriten in Dateien