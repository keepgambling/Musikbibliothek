class MusicLibrary:
    def __init__(self):
        self.songs = []
        self.favorites = []

    def add_song(self, title, artist, genre):
        song = {
            'title': title,
            'artist': artist,
            'genre': genre
        }
        self.songs.append(song)
        self.sort_songs()
        print(f"Song '{title}' von {artist} im Genre '{genre}' hinzugefügt und sortiert.")

    def delete_song(self, title):
        song = next((song for song in self.songs if song['title'].lower() == title.lower()), None)
        if song:
            self.songs.remove(song)
            self.sort_songs()
            print(f"Song '{title}' gelöscht und Liste sortiert.")
        else:
            print(f"Song '{title}' nicht gefunden.")

    def list_songs(self):
        print("\nListe der Songs:")
        for idx, song in enumerate(self.songs, start=1):
            print(f"{idx}. {song['title']} - {song['artist']} ({song['genre']})")

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

    def add_favorite(self, title):
        song = next((song for song in self.songs if song['title'].lower() == title.lower()), None)
        if song and song not in self.favorites:
            self.favorites.append(song)
            print(f"Song '{title}' zu Favoriten hinzugefügt.")
        else:
            print("Song ist entweder nicht in der Bibliothek oder bereits in den Favoriten.")

    def remove_favorite(self, index):
        if 0 <= index < len(self.favorites):
            removed_song = self.favorites.pop(index)
            print(f"Song '{removed_song['title']}' aus den Favoriten entfernt.")
        else:
            print("Ungültige Nummer.")

    def list_favorites(self):
        print("\nListe der Favoriten:")
        for idx, song in enumerate(self.favorites, start=1):
            print(f"{idx}. {song['title']} - {song['artist']} ({song['genre']})")


def main():
    library = MusicLibrary()
    print("Willkommen zu Ihrer Musikbibliothek")

    while True:
        print("\nHauptmenü")
        print("1. Titel verwalten")
        print("2. Titel anzeigen")
        print("3. Titel suchen")
        print("4. Favoriten verwalten")
        print("5. Playlist verwalten")
        print("6. Programm beenden")

        main_choice = input("Wähle eine Option: ")

        if main_choice == '1':
            while True:
                print("\nTitel verwalten")
                print("1. Titel hinzufügen")
                print("2. Titel löschen")
                print("3. Zurück")
                title_choice = input("Wähle eine Option: ")
                if title_choice == '1':
                    title = input("Gib den Titel des Songs ein: ")
                    artist = input("Gib den Interpreten des Songs ein: ")
                    genre = input("Gib das Genre des Songs ein: ")
                    library.add_song(title, artist, genre)
                elif title_choice == '2':
                    title = input("Gib den Titel des zu löschenden Songs ein: ")
                    library.delete_song(title)
                elif title_choice == "3":
                    break
                else:
                    print("Ungültige Option.")
        elif main_choice == '2':
            library.list_songs()
        elif main_choice == '3':
            search_term = input("Gib den Suchbegriff ein (Titel, Interpret oder Genre): ")
            library.search_song(search_term)
        elif main_choice == '4':
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
        elif main_choice == '5':
            while True:
                print("\nPlaylist verwalten")
                print("1. Playlist erstellen")
                print("2. Playlist anpassen")
                print("3. Playlist löschen")
                print("4. Zurück")
                play_choice = input("Wähle eine Option: ")
                if play_choice == '1':
                    while True:
                        print("\nPlaylist erstellen")
                        print("1. Titel Auswählen") # Titel einzeln auswählen mit Suchalgorithmus -> als Liste NAME DER PLAYLIST EINZIGARTIG
                        print("2. zufällige Titel einer Genre")
                        print("3. zufällige Titel eines Künstlers")
                        print("4. Zurück")
                        create_play_choice = input("Wähle eine Option: ")
                        if create_play_choice == '1':
                            print("asap")
                        elif create_play_choice == '2':
                            print("asap")
                        elif create_play_choice == '3':
                            print("asap")
                        elif create_play_choice == '4':
                            break
                        else:
                            print("Ungültige Option.")
                elif play_choice == '2':
                    while True:
                        print("\nPlaylist anpassen")
                        print("1. Titel hinzufügen") # Zuerst Playlist auswählen und dann Titel angeben
                        print("2. Titel entfernen") # Zuerst Playlist auswählen und dann Titel angeben
                        print("3. Zurück")
                        adjust_play_choice = input("Wähle eine Option: ")
                        if adjust_play_choice == '1':
                            print("asap")
                        elif adjust_play_choice == '2':
                            print("asap")
                        elif adjust_play_choice == '3':
                            break
                        else:
                            print("Ungültige Option.")
                elif play_choice == '3':
                    print("asap") #Eingabe des Playlist namen dann nochmal bestätigen mit Y/N
                elif play_choice == '4':
                    break
                else:
                    print("Ungültige Option.")
        elif main_choice == '6':
            print("Programm beendet.")
            break
        else:
            print("Ungültige Option. Bitte versuche es erneut.")

if __name__ == "__main__":
    main()


# Playlist erstllen NAME DER PLAYLIST EINZIGARTIG!
    # Mithilfe von Filtern Songs Auswählen
    # Song suche
# Playlist oder Favoriten "abspielen"
    # abspielen mit iter()
    # vllt zufälliges abspielen
# hinzufügen von Songs durch Datei
# Such algorythmen hinzufügen
    # binär
    # linear
