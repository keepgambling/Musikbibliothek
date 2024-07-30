class MusicLibrary:
    def __init__(self):
        self.songs = []
        self.favorites = []

    def add_song(self, title, artist, category):
        song = {
            'title': title,
            'artist': artist,
            'category': category
        }
        self.songs.append(song)
        self.sort_songs()
        print(f"Song '{title}' von {artist} in der Kategorie '{category}' hinzugefügt und sortiert.")

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
            print(f"{idx}. {song['title']} - {song['artist']} ({song['category']})")

    def sort_songs(self):
        self.songs.sort(key=lambda x: (x['title'].lower(), x['artist'].lower(), x['category'].lower()))

    def search_song(self, search_term):
        results = [song for song in self.songs if search_term.lower() in song['title'].lower() or search_term.lower() in song['artist'].lower() or search_term.lower() in song['category'].lower()]
        if results:
            print("\nSuchergebnisse:")
            for idx, song in enumerate(results, start=1):
                print(f"{idx}. {song['title']} - {song['artist']} ({song['category']})")
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
            print(f"{idx}. {song['title']} - {song['artist']} ({song['category']})")


def main():
    library = MusicLibrary()
    print("Willkommen zu Ihrer Musikbibliothek")

    while True:
        print("\nHauptmenü")
        print("1. Titel verwalten")
        print("2. Titel anzeigen")
        print("3. Titel suchen")
        print("4. Favoriten verwalten")
        print("5. Programm beenden")

        choice = input("Wähle eine Option: ")

        if choice == '1':
            print("\nTitel verwalten")
            print("1. Titel hinzufügen")
            print("2. Titel löschen")
            manage_choice = input("Wähle eine Option: ")
            if manage_choice == '1':
                title = input("Gib den Titel des Songs ein: ")
                artist = input("Gib den Interpreten des Songs ein: ")
                category = input("Gib die Kategorie des Songs ein: ")
                library.add_song(title, artist, category)
            elif manage_choice == '2':
                title = input("Gib den Titel des zu löschenden Songs ein: ")
                library.delete_song(title)
            else:
                print("Ungültige Option.")
        elif choice == '2':
            library.list_songs()
        elif choice == '3':
            search_term = input("Gib den Suchbegriff ein (Titel, Interpret oder Kategorie): ")
            library.search_song(search_term)
        elif choice == '4':
            print("\nFavoriten verwalten")
            print("1. Favoriten anzeigen")
            print("2. Song zu Favoriten hinzufügen")
            print("3. Song aus Favoriten entfernen")
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
            else:
                print("Ungültige Option.")
        elif choice == '5':
            print("Programm beendet.")
            break
        else:
            print("Ungültige Option. Bitte versuche es erneut.")

if __name__ == "__main__":
    main()


# Playlist erstllen 
# Playlist oder Favoriten "abspielen"
    #abspielen mit iter()
    #vllt zufälliges abspielen
# hinzufügen von Songs durch Datei
# Such algorythmen hinzufügen
    # binär
    # linear
    