import os
import random
import string

# Klasse, die ein Lied mit Titel, Künstler und Album darstellt
class Song:
    """Klasse, die ein Lied mit Titel, Künstler und Album darstellt."""
    
    def __init__(self, title, artist, album):
        # Initialisiert das Song-Objekt mit Titel, Künstler und Album
        self.title = title
        self.artist = artist
        self.album = album

    def __str__(self):
        # Gibt das Lied als String mit Titel, Künstler und Album zurück
        return f"{self.title} von {self.artist} ({self.album})"

    def __lt__(self, other):
        """Vergleiche Lieder basierend auf Titel, Künstler und Album."""
        # Wenn die Titel gleich sind, vergleiche Künstler
        if self.title == other.title:
            if self.artist == other.artist:
                return self.album < other.album
            return self.artist < other.artist
        # Wenn die Titel unterschiedlich sind, vergleiche diese
        return self.title < other.title

    def __eq__(self, other):
        """Überprüfen, ob zwei Lieder gleich sind."""
        # Zwei Lieder sind gleich, wenn Titel, Künstler und Album übereinstimmen
        return self.title == other.title and self.artist == other.artist and self.album == other.album


# Knotenklasse für einen Rot-Schwarz-Baum
class RedBlackNode:
    """Knoten für Rot-Schwarz-Baum, der ein Lied und Zeiger auf Kinder und Eltern speichert."""
    
    def __init__(self, song):
        # Initialisiert den Knoten mit dem Lied und setzt die Knotenfarbe auf Rot
        self.song = song
        self.color = "RED"
        self.left = None
        self.right = None
        self.parent = None


# Klasse für den Rot-Schwarz-Baum
class RedBlackTree:
    """Rot-Schwarz-Baum-Implementierung zur Speicherung von Liedern."""
    
    def __init__(self):
        # NIL-Knoten repräsentiert das Ende eines Zweiges, um Null zu vermeiden
        self.NIL = RedBlackNode(None)
        self.NIL.color = "BLACK"
        self.root = self.NIL

    def insert(self, song):
        """Füge ein neues Lied in den Rot-Schwarz-Baum ein."""
        # Erzeuge einen neuen Knoten mit dem Lied
        new_node = RedBlackNode(song)
        new_node.left = self.NIL
        new_node.right = self.NIL
        parent = None
        current = self.root

        # Falls der Baum leer ist, setze das neue Lied als Wurzel und mache es schwarz
        if self.root == self.NIL:
            self.root = new_node
            new_node.color = "BLACK"
            return

        # Suche die richtige Position für den neuen Knoten
        while current != self.NIL:
            parent = current
            if new_node.song < current.song:
                current = current.left
            else:
                current = current.right

        # Setze den Elter des neuen Knotens
        new_node.parent = parent

        # Bestimme, ob der neue Knoten ein linkes oder rechtes Kind sein soll
        if new_node.song < parent.song:
            parent.left = new_node
        else:
            parent.right = new_node

        # Korrigiere den Baum, falls er die Eigenschaften eines Rot-Schwarz-Baums verletzt
        self.fix_insert(new_node)

    def fix_insert(self, node):
        """Korrigiere den Rot-Schwarz-Baum nach dem Einfügen."""
        # Solange der Knoten nicht die Wurzel ist und der Elternknoten rot ist
        while node != self.root and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "RED":
                    # Fall 1: Onkel ist rot, also färbe um
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # Fall 2: Knoten ist ein rechtes Kind, führe Linksrotation durch
                        node = node.parent
                        self.left_rotate(node)
                    # Fall 3: Knoten ist ein linkes Kind, führe Rechtsrotation durch
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "RED":
                    # Spiegelbildliche Fälle für den rechten Elternteil
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.left_rotate(node.parent.parent)

        # Stelle sicher, dass die Wurzel schwarz ist
        self.root.color = "BLACK"

    def left_rotate(self, x):
        """Führe eine Linksrotation durch."""
        # Rotation nach links um den Knoten x
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        """Führe eine Rechtsrotation durch."""
        # Rotation nach rechts um den Knoten x
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def search(self, song):
        """Suche nach einem Lied im Rot-Schwarz-Baum."""
        # Starte die rekursive Suche nach dem Lied
        result = self._search_recursive(self.root, song)

    def _search_recursive(self, node, song):
        """Hilfsmethode für die rekursive Suche."""
        # Falls der Knoten das Lied enthält oder der NIL-Knoten erreicht wurde, kehre zurück
        if node == self.NIL or node.song == song:
            return node != self.NIL
        # Wenn das gesuchte Lied kleiner ist, gehe nach links, ansonsten nach rechts
        if song < node.song:
            return self._search_recursive(node.left, song)
        return self._search_recursive(node.right, song)

# Klasse für die Musikbibliothek
class MusicLibrary:
    """Musikbibliothek zur Verwaltung von Liedern."""
    
    # Standard-Dateinamen für Lieder und Favoriten
    FILENAME = "songs.csv"
    FAVORITES_FILENAME = "favoriten.csv"

    def __init__(self):
        # Initialisiert die Bibliothek mit einer Liste von Liedern und Favoriten
        self.songs = []
        self.favorites = []
        self.rbt = RedBlackTree()
        self.load_songs()  # Läd die Lieder aus der Datei
        self.load_favorites()  # Läd die Favoriten aus der Datei

    def load_songs(self):
        """Lade Lieder aus der Datei."""
        try:
            # Prüfe, ob die Datei existiert, und lade die Lieder
            if os.path.exists(self.FILENAME):
                with open(self.FILENAME, 'r') as file:
                    for line in file:
                        if line.strip():
                            title, artist, album = line.strip().split(',')
                            song = Song(title, artist, album)
                            self.songs.append(song)
                            self.rbt.insert(song)
                print(f"{len(self.songs)} Lieder aus {self.FILENAME} geladen.")
            else:
                print("Keine Lieder gefunden. Beginne mit einer leeren Bibliothek.")
        except Exception as e:
            print(f"Fehler beim Laden der Songs: {e}")

    def save_songs(self):
        """Speichere Lieder in eine Datei."""
        # Schreibe die Lieder in die Datei
        with open(self.FILENAME, 'w') as file:
            for song in self.songs:
                file.write(f"{song.title},{song.artist},{song.album}\n")
        print(f"{len(self.songs)} Lieder in {self.FILENAME} gespeichert.")

    def add_song(self, title, artist, album):
        """Füge ein neues Lied zur Bibliothek hinzu."""
        # Erstelle ein neues Song-Objekt und füge es der Bibliothek hinzu
        song = Song(title, artist, album)
        self.songs.append(song)
        self.rbt.insert(song)
        self.save_songs()
        print(f"'{song}' wurde deiner Musikbibliothek hinzugefügt.")

    def delete_song(self, title):
        """Lösche ein Lied nach Titel."""
        # Suche das Lied mit dem angegebenen Titel in der Bibliothek
        song_to_delete = next((s for s in self.songs if s.title == title), None)
        
        if song_to_delete:
            # Wenn das Lied gefunden wurde, entferne es aus der Bibliothek
            self.songs.remove(song_to_delete)
            # Speichere die aktualisierte Liste der Lieder
            self.save_songs()
            print(f"'{song_to_delete}' wurde aus deiner Musikbibliothek entfernt.")
        else:
            # Wenn das Lied nicht gefunden wurde, gib eine entsprechende Nachricht aus
            print(f"'{title}' wurde in deiner Musikbibliothek nicht gefunden.")

    def display_songs(self):
        """Zeige alle Lieder in der Bibliothek an."""
        if self.songs:
            # Wenn Lieder vorhanden sind, zeige sie mit ihrer Position in der Liste an
            print("Deine Musikbibliothek:")
            for i, song in enumerate(self.songs, 1):
                print(f"{i}. {song}")
        else:
            # Wenn keine Lieder vorhanden sind, zeige eine Nachricht an
            print("Deine Musikbibliothek ist leer.")

    def linear_search(self, title):
        """Lineare Suche nach einem Titel mit Laufzeitmessung."""
        # Durchsuche die Bibliothek linear (sequentiell), um ein Lied mit dem angegebenen Titel zu finden
        for index, song in enumerate(self.songs):
            if song.title == title:
                # Gib den Index des gefundenen Liedes zurück
                return index
        # Wenn das Lied nicht gefunden wurde, gib -1 zurück
        return -1

    def binary_search(self, title):
        """Binäre Suche mit dem Rot-Schwarz-Baum."""
        # Erstelle ein temporäres Song-Objekt mit dem gesuchten Titel
        song_to_search = Song(title, "", "")
        # Suche das Lied im Rot-Schwarz-Baum
        found = self.rbt.search(song_to_search)
        # Gib das Ergebnis der Suche zurück (True oder False)
        return found

    def interpolation_search(self, title):
        """Interpolation Search Algorithmus für eine sortierte Liste mit Zeitmessung."""
        low = 0
        high = len(self.songs) - 1

        while low <= high and title >= self.songs[low].title and title <= self.songs[high].title:
            # Vermeide Division durch Null, falls der Anfangs- und Endtitel gleich sind
            if self.songs[high].title == self.songs[low].title:
                if self.songs[low].title == title:
                    # Gib die Position des gefundenen Liedes zurück
                    return low
                else:
                    break

            # Berechne die Position anhand der Interpolationsformel
            pos = low + ((ord(title[0]) - ord(self.songs[low].title[0])) * (high - low) // 
                        (ord(self.songs[high].title[0]) - ord(self.songs[low].title[0])))

            # Überprüfe, ob das Lied an der berechneten Position gefunden wurde
            if self.songs[pos].title == title:
                return pos

            # Passen den Suchbereich basierend auf dem verglichenen Titel an
            if self.songs[pos].title < title:
                low = pos + 1
            else:
                high = pos - 1

        # Wenn das Lied nicht gefunden wurde, gib -1 zurück
        return -1

    def exponential_search(self, title):
        """Exponential Search Algorithmus für eine sortierte Liste mit Zeitmessung."""
        if len(self.songs) == 0:
            return -1

        # Prüfe, ob das erste Lied in der Liste das gesuchte ist
        if self.songs[0].title == title:
            return 0

        # Finde den Bereich, in dem sich das gesuchte Lied befinden könnte
        i = 1
        while i < len(self.songs) and self.songs[i].title <= title:
            i = i * 2

        # Führe eine binäre Suche im gefundenen Bereich durch
        return self._binary_search_in_range(title, i // 2, min(i, len(self.songs) - 1))

    def _binary_search_in_range(self, title, low, high):
        """Binäre Suche in einem spezifischen Bereich."""
        while low <= high:
            mid = low + (high - low) // 2

            if self.songs[mid].title == title:
                # Wenn das Lied gefunden wurde, gib die Position zurück
                return mid
            elif self.songs[mid].title < title:
                low = mid + 1
            else:
                high = mid - 1

        # Wenn das Lied nicht gefunden wurde, gib -1 zurück
        return -1

    def bubble_sort(self):
        """Bubble Sort Algorithmus mit Laufzeitmessung."""
        # Anzahl der Lieder in der Bibliothek
        n = len(self.songs)
        for i in range(n):
            swapped = False
            # Vergleiche und tausche benachbarte Lieder, wenn nötig
            for j in range(0, n - i - 1):
                if self.songs[j] > self.songs[j + 1]:
                    self.songs[j], self.songs[j + 1] = self.songs[j + 1], self.songs[j]
                    swapped = True
            # Wenn keine Vertauschungen vorgenommen wurden, ist die Liste sortiert
            if not swapped:
                break
        # Speichere die sortierten Lieder
        self.save_songs()

    def insertion_sort(self):
        """Insertion Sort Algorithmus mit Laufzeitmessung."""
        # Iteriere über die Lieder und füge sie sortiert in die Liste ein
        for i in range(1, len(self.songs)):
            key_song = self.songs[i]
            j = i - 1
            # Verschiebe Lieder, die größer als das aktuelle Lied sind, um einen Platz nach rechts
            while j >= 0 and key_song < self.songs[j]:
                self.songs[j + 1] = self.songs[j]
                j -= 1
            # Setze das aktuelle Lied an die richtige Position
            self.songs[j + 1] = key_song
        # Speichere die sortierten Lieder
        self.save_songs()

    def merge_sort(self, array=None):
        """Merge Sort Algorithmus mit Laufzeitmessung."""
        # Initialisiere das Array mit der Bibliothek, wenn keines übergeben wird
        if array is None:
            array = self.songs

        # Wenn das Array nur ein Element enthält, ist es bereits sortiert
        if len(array) <= 1:
            return array

        # Teile das Array in zwei Hälften und sortiere diese rekursiv
        mid = len(array) // 2
        left_half = self.merge_sort(array[:mid])
        right_half = self.merge_sort(array[mid:])
        # Mische die beiden sortierten Hälften zusammen
        return self._merge(left_half, right_half)

    def _merge(self, left, right):
        """Hilfsmethode zum Mischen von zwei Arrays."""
        result = []
        i, j = 0, 0

        # Füge Elemente der beiden Hälften sortiert in das Ergebnisarray ein
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Füge verbleibende Elemente hinzu
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort_with_merge_sort(self):
        """Führt Merge Sort durch und misst die Zeit."""
        # Sortiere die Bibliothek mit Merge Sort
        self.songs = self.merge_sort()
        # Speichere die sortierten Lieder
        self.save_songs()

    def heap_sort(self):
        """Heap Sort Algorithmus mit Laufzeitmessung."""
        n = len(self.songs)

        # Erzeuge den Heap (Umstrukturierung der Liste)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(n, i)

        # Extrahiere die Elemente aus dem Heap und sortiere sie
        for i in range(n - 1, 0, -1):
            self.songs[i], self.songs[0] = self.songs[0], self.songs[i]
            self._heapify(i, 0)
        # Speichere die sortierten Lieder
        self.save_songs()

    def _heapify(self, n, i):
        """Hilfsmethode zur Umstrukturierung eines Heaps."""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Finde das größte Element unter dem Knoten und seinen Kindern
        if left < n and self.songs[left] > self.songs[largest]:
            largest = left

        if right < n and self.songs[right] > self.songs[largest]:
            largest = right

        # Wenn das größte Element nicht der aktuelle Knoten ist, tausche es und strukturiere weiter um
        if largest != i:
            self.songs[i], self.songs[largest] = self.songs[largest], self.songs[i]
            self._heapify(n, largest)

    def create_random_songs(self, count):
        """Erstelle zufällige Lieder."""
        # Erstelle eine bestimmte Anzahl von zufälligen Liedern
        for _ in range(count):
            # Generiere einen zufälligen Titel, Künstler und Albumname aus Großbuchstaben
            title = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5, 10)))
            artist = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5, 10)))
            album = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5, 10)))
            # Füge das zufällig generierte Lied der Bibliothek hinzu
            self.add_song(title, artist, album)

    def load_favorites(self):
        """Lade Favoriten aus der Datei."""
        # Prüfe, ob die Favoriten-Datei existiert
        if os.path.exists(self.FAVORITES_FILENAME):
            # Öffne die Datei und lade die Lieder in die Favoritenliste
            with open(self.FAVORITES_FILENAME, 'r') as file:
                for line in file:
                    if line.strip():
                        # Zerlege jede Zeile in Titel, Künstler und Album
                        title, artist, album = line.strip().split(',')
                        # Erstelle ein neues Song-Objekt und füge es den Favoriten hinzu
                        song = Song(title, artist, album)
                        self.favorites.append(song)
            # Gib die Anzahl der geladenen Favoriten aus
            print(f"{len(self.favorites)} Favoriten aus {self.FAVORITES_FILENAME} geladen.")

    def save_favorites(self):
        """Speichere Favoriten in eine Datei."""
        # Öffne die Datei im Schreibmodus
        with open(self.FAVORITES_FILENAME, 'w') as file:
            # Schreibe jedes Lieblingslied in die Datei
            for song in self.favorites:
                file.write(f"{song.title},{song.artist},{song.album}\n")
        # Gib die Anzahl der gespeicherten Favoriten aus
        print(f"{len(self.favorites)} Favoriten in {self.FAVORITES_FILENAME} gespeichert.")

    def add_favorite(self, title):
        """Füge ein Lied zu den Favoriten hinzu, wenn es in der Bibliothek vorhanden ist."""
        try:
            # Suche nach einem Lied mit dem angegebenen Titel in der Bibliothek
            song_to_add = next((s for s in self.songs if s.title == title), None)
            # Wenn das Lied gefunden wird und nicht bereits in den Favoriten ist
            if song_to_add and song_to_add not in self.favorites:
                # Füge das Lied zu den Favoriten hinzu
                self.favorites.append(song_to_add)
                # Speichere die aktualisierten Favoriten
                self.save_favorites()
                print(f"'{song_to_add}' wurde zu deinen Favoriten hinzugefügt.")
            elif song_to_add in self.favorites:
                # Falls das Lied bereits in den Favoriten ist
                print(f"'{title}' ist bereits in den Favoriten.")
            else:
                # Falls das Lied nicht in der Bibliothek gefunden wurde
                print(f"'{title}' wurde nicht in deiner Musikbibliothek gefunden.")
        except Exception as e:
            # Gib eine Fehlermeldung aus, falls beim Hinzufügen ein Fehler auftritt
            print(f"Fehler beim Hinzufügen zu Favoriten: {e}")

    def remove_favorite(self, title):
        """Entferne ein Lied aus den Favoriten."""
        # Suche nach einem Lied mit dem angegebenen Titel in der Favoritenliste
        song_to_remove = next((s for s in self.favorites if s.title == title), None)
        if song_to_remove:
            # Entferne das Lied, wenn es in den Favoriten gefunden wurde
            self.favorites.remove(song_to_remove)
            # Speichere die aktualisierte Favoritenliste
            self.save_favorites()
            print(f"'{song_to_remove}' wurde aus deinen Favoriten entfernt.")
        else:
            # Falls das Lied nicht in den Favoriten gefunden wurde
            print(f"'{title}' wurde in deinen Favoriten nicht gefunden.")

    def display_favorites(self):
        """Zeige alle Favoriten an."""
        # Prüfe, ob es Favoriten gibt
        if self.favorites:
            print("Deine Favoriten:")
            # Zeige die Favoriten mit ihrer Position in der Liste an
            for i, song in enumerate(self.favorites, 1):
                print(f"{i}. {song}")
        else:
            # Falls keine Favoriten vorhanden sind, gib eine entsprechende Nachricht aus
            print("Du hast keine Favoriten.")


# Menüfunktionen

def print_menu(title, options):
    """Hilfsfunktion zur Anzeige eines Menüs."""
    # Druckt eine Überschrift mit einer Trennlinie aus Gleichheitszeichen
    print(f"\n{'=' * 30}")
    print(f"{title:^30}")  # Zentriert den Titel innerhalb der 30 Zeichen
    print(f"{'=' * 30}")
    # Iteriert über die Optionen und zeigt sie nummeriert an
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    print(f"{'=' * 30}")  # Schließt das Menü mit einer weiteren Trennlinie ab

def manage_songs(library=MusicLibrary):
    """Verwalte Lieder in der Bibliothek."""
    while True:
        # Zeigt das Menü für das Verwalten von Liedern an
        print_menu("Verwalte Lieder", [
            "Zeige Lieder",
            "Lied hinzufügen",
            "Zufällige Lieder erstellen",
            "Lied löschen",
            "Zurück"
        ])
        choice = input("Wähle eine Option: ")  # Fragt den Benutzer nach einer Auswahl

        # Überprüft die Auswahl des Benutzers und führt die entsprechende Aktion aus
        if choice == '1':
            library.display_songs()  # Zeigt alle Lieder in der Bibliothek an
        elif choice == '2':
            # Nimmt die Details des neuen Liedes auf
            title = input("Gib den Titel des Liedes ein: ")
            artist = input("Gib den Künstler ein: ")
            album = input("Gib das Album ein: ")
            library.add_song(title, artist, album)  # Fügt das neue Lied hinzu
        elif choice == '3':
            # Fragt nach der Anzahl der zufällig zu erstellenden Lieder
            count = int(input("Gib die Anzahl der zu erstellenden zufälligen Lieder ein: "))
            library.create_random_songs(count)  # Erstellt die zufälligen Lieder
        elif choice == '4':
            # Fragt nach dem Titel des zu löschenden Liedes
            title = input("Gib den Titel des zu löschenden Liedes ein: ")
            library.delete_song(title)  # Löscht das angegebene Lied
        elif choice == '5':
            break  # Beendet das Menü
        else:
            print("Ungültige Option.")  # Warnung bei ungültiger Eingabe

def sort_songs(library=MusicLibrary):
    """Zeige Sortieroptionen und führe die gewählte Sortierung durch."""
    while True:
        # Zeigt ein Menü zur Auswahl eines Sortieralgorithmus
        print_menu("Wähle einen Sortieralgorithmus", [
            "Insertion Sort",
            "Merge Sort",
            "Heap Sort",
            "Bubble Sort",
            "Zurück"
        ])
        choice = input("Gib deine Wahl ein: ").strip()  # Fragt nach der Wahl des Sortierverfahrens

        # Überprüft die Auswahl und führt die entsprechende Sortierung durch
        if choice == '1':
            library.insertion_sort()  # Führt den Insertion Sort durch
        elif choice == '2':
            library.sort_with_merge_sort()  # Führt den Merge Sort durch
        elif choice == '3':
            library.heap_sort()  # Führt den Heap Sort durch
        elif choice == '4':
            library.bubble_sort()  # Führt den Bubble Sort durch
        elif choice == '5':
            return  # Verlasse das Menü
        else:
            print("Ungültige Wahl. Bitte versuche es erneut.")  # Warnung bei ungültiger Eingabe

def search_songs(library=MusicLibrary):
    """Suche nach Liedern in der Bibliothek, geordnet nach Geschwindigkeit."""
    while True:
        # Zeigt ein Menü zur Auswahl einer Suchmethode
        print_menu("Suche nach Liedern", [
            "Exponential Search",
            "Binäre Suche",
            "Interpolation Search",
            "Lineare Suche",
            "Zurück"
        ])
        choice = input("Wähle eine Option: ")  # Fragt nach der Wahl der Suchmethode

        # Überprüft die Auswahl und führt die entsprechende Suchmethode durch
        if choice == '1':
            title = input("Gib den Titel des Liedes ein: ")
            result = library.exponential_search(title)  # Führt die Exponentialsuche durch
            if result != -1:
                print(f"'{library.songs[result]}' an Position {result + 1} gefunden.")
            else:
                print(f"'{title}' wurde nicht gefunden.")
        elif choice == '2':
            title = input("Gib den Titel des Liedes ein: ")
            found = library.binary_search(title)  # Führt die Binärsuche durch
            if found:
                print(f"'{title}' in deiner Musikbibliothek gefunden.")
            else:
                print(f"'{title}' wurde nicht gefunden.")
        elif choice == '3':
            title = input("Gib den Titel des Liedes ein: ")
            result = library.interpolation_search(title)  # Führt die Interpolationssuche durch
            if result != -1:
                print(f"'{library.songs[result]}' an Position {result + 1} gefunden.")
            else:
                print(f"'{title}' wurde nicht gefunden.")
        elif choice == '4':
            title = input("Gib den Titel des Liedes ein: ")
            result = library.linear_search(title)  # Führt die Linearsuche durch
            if result != -1:
                print(f"'{library.songs[result]}' an Position {result + 1} gefunden.")
            else:
                print(f"'{title}' wurde nicht gefunden.")
        elif choice == '5':
            break  # Verlasse das Menü
        else:
            print("Ungültige Option.")  # Warnung bei ungültiger Eingabe

def manage_favorites(library=MusicLibrary):
    """Verwalte Favoriten in der Bibliothek."""
    while True:
        # Zeigt ein Menü zur Verwaltung der Favoriten
        print_menu("Verwalte Favoriten", [
            "Zeige Favoriten",
            "Lied zu Favoriten hinzufügen",
            "Lied aus Favoriten entfernen",
            "Zurück"
        ])
        choice = input("Wähle eine Option: ")  # Fragt nach der Wahl

        # Überprüft die Auswahl und führt die entsprechende Aktion aus
        if choice == '1':
            library.display_favorites()  # Zeigt die Favoriten an
        elif choice == '2':
            # Fragt nach dem Titel des hinzuzufügenden Liedes
            title = input("Gib den Titel des Liedes ein, das du zu den Favoriten hinzufügen möchtest: ")
            library.add_favorite(title)  # Fügt das Lied den Favoriten hinzu
        elif choice == '3':
            # Fragt nach dem Titel des zu entfernenden Liedes
            title = input("Gib den Titel des Liedes ein, das du aus den Favoriten entfernen möchtest: ")
            library.remove_favorite(title)  # Entfernt das Lied aus den Favoriten
        elif choice == '4':
            break  # Verlasse das Menü
        else:
            print("Ungültige Option.")  # Warnung bei ungültiger Eingabe

# Hauptprogramm

def main():
    """Hauptprogramm zur Ausführung der Musikbibliothek."""
    library = MusicLibrary()  # Erstellt ein neues Musikbibliotheksobjekt
    print("Willkommen in deiner Musikbibliothek")  # Begrüßung des Benutzers

    while True:
        # Zeigt das Hauptmenü an
        print_menu("Hauptmenü", [
            "Lieder verwalten",
            "Nach Liedern suchen",
            "Lieder sortieren",
            "Favoriten verwalten",
            "Beenden"
        ])
        main_choice = input("Wähle eine Option: ")  # Fragt nach der Wahl im Hauptmenü

        # Überprüft die Auswahl und leitet den Benutzer zu den entsprechenden Untermenüs
        if main_choice == '1':
            manage_songs(library)  # Öffnet das Menü zur Verwaltung der Lieder
        elif main_choice == '2':
            search_songs(library)  # Öffnet das Suchmenü
        elif main_choice == '3':
            sort_songs(library)  # Öffnet das Sortiermenü
        elif main_choice == '4':
            manage_favorites(library)  # Öffnet das Favoritenmenü
        elif main_choice == '5':
            print("Programm wird beendet.")  # Beendet das Programm
            break
        else:
            print("Ungültige Option. Bitte versuche es erneut.")  # Warnung bei ungültiger Eingabe

if __name__ == "__main__":
    main()
