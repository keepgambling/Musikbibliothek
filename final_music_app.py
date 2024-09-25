import os
import time
import random
import string

class Song:
    """Klasse, die ein Lied mit Titel, Künstler und Album darstellt."""
    def __init__(self, title, artist, album):
        self.title = title
        self.artist = artist
        self.album = album

    def __str__(self):
        return f"{self.title} von {self.artist} ({self.album})"

    def __lt__(self, other):
        """Vergleiche Lieder basierend auf Titel, Künstler und Album."""
        if self.title == other.title:
            if self.artist == other.artist:
                return self.album < other.album
            return self.artist < other.artist
        return self.title < other.title

    def __eq__(self, other):
        """Überprüfen, ob zwei Lieder gleich sind."""
        return self.title == other.title and self.artist == other.artist and self.album == other.album


class RedBlackNode:
    """Knoten für Rot-Schwarz-Baum, der ein Lied und Zeiger auf Kinder und Eltern speichert."""
    def __init__(self, song):
        self.song = song
        self.color = "RED"
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    """Rot-Schwarz-Baum-Implementierung zur Speicherung von Liedern."""
    def __init__(self):
        self.NIL = RedBlackNode(None)
        self.NIL.color = "BLACK"
        self.root = self.NIL

    def insert(self, song):
        """Füge ein neues Lied in den Rot-Schwarz-Baum ein."""
        new_node = RedBlackNode(song)
        new_node.left = self.NIL
        new_node.right = self.NIL
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.song < current.song:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.song < parent.song:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)

    def fix_insert(self, node):
        """Korrigiere den Rot-Schwarz-Baum nach dem Einfügen."""
        while node != self.root and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "RED":
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

        self.root.color = "BLACK"

    def left_rotate(self, x):
        """Führe eine Linksrotation durch."""
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
        result = self._search_recursive(self.root, song)

    def _search_recursive(self, node, song):
        """Hilfsmethode für die rekursive Suche."""
        if node == self.NIL or node.song == song:
            return node != self.NIL
        if song < node.song:
            return self._search_recursive(node.left, song)
        return self._search_recursive(node.right, song)


class MusicLibrary:
    """Musikbibliothek zur Verwaltung von Liedern."""
    FILENAME = "songs.csv"

    def __init__(self):
        self.songs = []
        self.rbt = RedBlackTree()
        self.load_songs()

    def load_songs(self):
        """Lade Lieder aus der Datei."""
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

    def save_songs(self):
        """Speichere Lieder in eine Datei."""
        with open(self.FILENAME, 'w') as file:
            for song in self.songs:
                file.write(f"{song.title},{song.artist},{song.album}\n")
        print(f"{len(self.songs)} Lieder in {self.FILENAME} gespeichert.")

    def add_song(self, title, artist, album):
        """Füge ein neues Lied zur Bibliothek hinzu."""
        song = Song(title, artist, album)
        self.songs.append(song)
        self.rbt.insert(song)
        self.save_songs()
        print(f"'{song}' wurde deiner Musikbibliothek hinzugefügt.")

    def delete_song(self, title):
        """Lösche ein Lied nach Titel."""
        song_to_delete = next((s for s in self.songs if s.title == title), None)
        if song_to_delete:
            self.songs.remove(song_to_delete)
            self.save_songs()
            print(f"'{song_to_delete}' wurde aus deiner Musikbibliothek entfernt.")
        else:
            print(f"'{title}' wurde in deiner Musikbibliothek nicht gefunden.")

    def display_songs(self):
        """Zeige alle Lieder in der Bibliothek an."""
        if self.songs:
            print("Deine Musikbibliothek:")
            for i, song in enumerate(self.songs, 1):
                print(f"{i}. {song}")
        else:
            print("Deine Musikbibliothek ist leer.")

    def linear_search(self, title):
        """Lineare Suche nach einem Titel mit Laufzeitmessung."""
        start_time = time.time()  
        for index, song in enumerate(self.songs):
            if song.title == title:
                print(f"Zeit für lineare Suche: {time.time() - start_time:.6f} Sekunden.")
                return index
        print(f"Zeit für lineare Suche: {time.time() - start_time:.6f} Sekunden.")
        return -1

    def binary_search(self, title):
        """Binäre Suche mit dem Rot-Schwarz-Baum."""
        start_time = time.time()  
        song_to_search = Song(title, "", "")
        found = self.rbt.search(song_to_search)
        print(f"Zeit für binäre Suche: {time.time() - start_time:.6f} Sekunden.")
        return found

    def interpolation_search(self, title):
        """Interpolation Search Algorithmus für eine sortierte Liste mit Zeitmessung."""
        start_time = time.time()
        low = 0
        high = len(self.songs) - 1
        while low <= high and title >= self.songs[low].title and title <= self.songs[high].title:
            if low == high:
                if self.songs[low].title == title:
                    print(f"Zeit für Interpolation Search: {time.time() - start_time:.6f} Sekunden.")
                    return low
                return -1

            pos = low + ((high - low) // (ord(self.songs[high].title[0]) - ord(self.songs[low].title[0])) *
                         (ord(title[0]) - ord(self.songs[low].title[0])))

            if self.songs[pos].title == title:
                print(f"Zeit für Interpolation Search: {time.time() - start_time:.6f} Sekunden.")
                return pos
            if self.songs[pos].title < title:
                low = pos + 1
            else:
                high = pos - 1

        print(f"Zeit für Interpolation Search: {time.time() - start_time:.6f} Sekunden.")
        return -1

    def exponential_search(self, title):
        """Exponential Search Algorithmus für eine sortierte Liste mit Zeitmessung."""
        start_time = time.time()
        if len(self.songs) == 0:
            print(f"Zeit für Exponential Search: {time.time() - start_time:.6f} Sekunden.")
            return -1

        if self.songs[0].title == title:
            print(f"Zeit für Exponential Search: {time.time() - start_time:.6f} Sekunden.")
            return 0

        i = 1
        while i < len(self.songs) and self.songs[i].title <= title:
            i = i * 2

        result = self._binary_search_in_range(title, i // 2, min(i, len(self.songs)))
        print(f"Zeit für Exponential Search: {time.time() - start_time:.6f} Sekunden.")
        return result

    def _binary_search_in_range(self, title, low, high):
        """Binäre Suche in einem spezifischen Bereich."""
        while low <= high:
            mid = low + (high - low) // 2

            if self.songs[mid].title == title:
                return mid
            elif self.songs[mid].title < title:
                low = mid + 1
            else:
                high = mid - 1

        return -1

    def _measure_sort_time(self, sort_function):
        """Messe und zeige die Zeit an, die für das Sortieren benötigt wird."""
        start_time = time.time()
        sort_function()
        print(f"Zeit benötigt: {time.time() - start_time:.6f} Sekunden.")
        self.save_songs()

    def bubble_sort(self):
        """Bubble Sort Algorithmus mit Laufzeitmessung."""
        start_time = time.time()
        n = len(self.songs)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if self.songs[j] > self.songs[j + 1]:
                    self.songs[j], self.songs[j + 1] = self.songs[j + 1], self.songs[j]
                    swapped = True
            if not swapped:
                break
        print(f"Zeit für Bubble Sort: {time.time() - start_time:.6f} Sekunden.")

    def insertion_sort(self):
        """Insertion Sort Algorithmus mit Laufzeitmessung."""
        start_time = time.time()
        for i in range(1, len(self.songs)):
            key_song = self.songs[i]
            j = i - 1
            while j >= 0 and key_song < self.songs[j]:
                self.songs[j + 1] = self.songs[j]
                j -= 1
            self.songs[j + 1] = key_song
        print(f"Zeit für Insertion Sort: {time.time() - start_time:.6f} Sekunden.")

    def merge_sort(self, array=None):
        """Merge Sort Algorithmus mit Laufzeitmessung."""
        if array is None:
            array = self.songs

        if len(array) <= 1:
            return array

        mid = len(array) // 2
        left_half = self.merge_sort(array[:mid])
        right_half = self.merge_sort(array[mid:])
        return self._merge(left_half, right_half)

    def _merge(self, left, right):
        """Hilfsmethode zum Mischen von zwei Arrays."""
        result = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort_with_merge_sort(self):
        """Führt Merge Sort durch und misst die Zeit."""
        start_time = time.time()
        self.songs = self.merge_sort()
        print(f"Zeit für Merge Sort: {time.time() - start_time:.6f} Sekunden.")
        self.save_songs()


    def heap_sort(self):
        """Heap Sort Algorithmus mit Laufzeitmessung."""
        start_time = time.time()
        n = len(self.songs)

        # Erstelle einen Max-Heap
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(n, i)

        # Einzeln Elemente vom Heap entfernen
        for i in range(n - 1, 0, -1):
            self.songs[i], self.songs[0] = self.songs[0], self.songs[i]  # Tausche
            self._heapify(i, 0)

        print(f"Zeit für Heap Sort: {time.time() - start_time:.6f} Sekunden.")

    def _heapify(self, n, i):
        """Hilfsmethode zur Umstrukturierung eines Heaps."""
        largest = i
        left = 2 * i + 1  # Linkes Kind
        right = 2 * i + 2  # Rechtes Kind

        # Wenn das linke Kind größer ist als der größte bisherige Wert
        if left < n and self.songs[left] > self.songs[largest]:
            largest = left

        # Wenn das rechte Kind größer ist als der größte bisherige Wert
        if right < n and self.songs[right] > self.songs[largest]:
            largest = right

        # Wenn der größte Wert nicht die Wurzel ist
        if largest != i:
            self.songs[i], self.songs[largest] = self.songs[largest], self.songs[i]  # Tausche
            self._heapify(n, largest)

    def create_random_songs(self, count):
        """Erstelle zufällige Lieder."""
        for _ in range(count):
            title = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5, 10)))
            artist = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5, 10)))
            album = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5, 10)))
            self.add_song(title, artist, album)


# Menüfunktionen

def manage_songs(library = MusicLibrary):
    """Verwalte Lieder in der Bibliothek."""
    while True:
        print("\nVerwalte Lieder")
        print("1. Zeige Lieder")
        print("2. Lied hinzufügen")
        print("3. Zufällige Lieder erstellen")
        print("4. Lied löschen")
        print("5. Zurück")
        choice = input("Wähle eine Option: ")

        if choice == '1':
            library.display_songs()
        elif choice == '2':
            title = input("Gib den Titel des Liedes ein: ")
            artist = input("Gib den Künstler ein: ")
            album = input("Gib das Album ein: ")
            library.add_song(title, artist, album)
        elif choice == '3':
            count = int(input("Gib die Anzahl der zu erstellenden zufälligen Lieder ein: "))
            library.create_random_songs(count)
        elif choice == '4':
            title = input("Gib den Titel des zu löschenden Liedes ein: ")
            library.delete_song(title)
        elif choice == '5':
            break
        else:
            print("Ungültige Option.")

def sort_songs(library=MusicLibrary):
    """Zeige Sortieroptionen und führe die gewählte Sortierung durch."""
    while True:
        print("Wähle einen Sortieralgorithmus:")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Merge Sort")
        print("4. Heap Sort")
        print("5. Zurück")
        choice = input("Gib deine Wahl ein: ").strip()

        if choice == '1':
            library._measure_sort_time(library.bubble_sort)
        elif choice == '2':
            library._measure_sort_time(library.insertion_sort)
        elif choice == '3':
            library.sort_with_merge_sort()
        elif choice == '4':
            library._measure_sort_time(library.heap_sort)
        elif choice == '5':
            return
        else:
            print("Ungültige Wahl. Bitte versuche es erneut.")

def search_songs(library = MusicLibrary):
    """Suche nach Liedern in der Bibliothek."""
    while True:
        print("\nSuche nach Liedern")
        print("1. Lineare Suche")
        print("2. Binäre Suche")
        print("3. Interpolation Search")
        print("4. Exponential Search")
        print("5. Zurück")
        choice = input("Wähle eine Option: ")

        if choice == '1':
            title = input("Gib den Titel des Liedes ein: ")
            result = library.linear_search(title)
            if result != -1:
                print(f"'{library.songs[result]}' an Position {result + 1} gefunden.")
            else:
                print(f"'{title}' wurde nicht gefunden.")
        elif choice == '2':
            title = input("Gib den Titel des Liedes ein: ")
            found = library.binary_search(title)
            if found:
                print(f"'{title}' in deiner Musikbibliothek gefunden.")
            else:
                print(f"'{title}' wurde nicht gefunden.")
        elif choice == '3':
            title = input("Gib den Titel des Liedes ein: ")
            result = library.interpolation_search(title)
            if result != -1:
                print(f"'{library.songs[result]}' an Position {result + 1} gefunden.")
            else:
                print(f"'{title}' wurde nicht gefunden.")
        elif choice == '4':
            title = input("Gib den Titel des Liedes ein: ")
            result = library.exponential_search(title)
            if result != -1:
                print(f"'{library.songs[result]}' an Position {result + 1} gefunden.")
            else:
                print(f"'{title}' wurde nicht gefunden.")
        elif choice == '5':
            break
        else:
            print("Ungültige Option.")

# Hauptprogramm

def main():
    """Hauptprogramm zur Ausführung der Musikbibliothek."""
    library = MusicLibrary()
    print("Willkommen in deiner Musikbibliothek")

    while True:
        print("\nHauptmenü")
        print("1. Lieder verwalten")
        print("2. Nach Liedern suchen")
        print("3. Lieder sortieren")
        print("4. Beenden")
        main_choice = input("Wähle eine Option: ")

        if main_choice == '1':
            manage_songs(library)
        elif main_choice == '2':
            search_songs(library)
        elif main_choice == '3':
            sort_songs(library)
        elif main_choice == '4':
            print("Programm wird beendet.")
            break
        else:
            print("Ungültige Option. Bitte versuche es erneut.")

if __name__ == "__main__":
    main()
