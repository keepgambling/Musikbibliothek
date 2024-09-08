import os

class Song:
    """Class to represent a song with title, artist, and album."""
    def __init__(self, title, artist, album):
        self.title = title
        self.artist = artist
        self.album = album

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.album})"

    def __lt__(self, other):
        if self.title == other.title:
            if self.artist == other.artist:
                return self.album < other.album
            return self.artist < other.artist
        return self.title < other.title

    def __eq__(self, other):
        return self.title == other.title and self.artist == other.artist and self.album == other.album

class RedBlackNode:
    """Node for Red-Black Tree, storing a song and pointers to children and parent."""
    def __init__(self, song):
        self.song = song
        self.color = "RED"
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    """Implementation of Red-Black Tree for storing songs."""
    def __init__(self):
        self.NIL = RedBlackNode(None)
        self.NIL.color = "BLACK"
        self.root = self.NIL

    def insert(self, song):
        """Insert a new song into the Red-Black Tree."""
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
        """Fix the Red-Black Tree after an insertion to maintain balance."""
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
        """Perform a left rotation in the Red-Black Tree."""
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
        """Perform a right rotation in the Red-Black Tree."""
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
        """Search for a song in the Red-Black Tree."""
        return self._search_recursive(self.root, song)

    def _search_recursive(self, node, song):
        """Helper method to recursively search the tree."""
        if node == self.NIL or node.song == song:
            return node != self.NIL
        if song < node.song:
            return self._search_recursive(node.left, song)
        return self._search_recursive(node.right, song)

class MusicLibrary:
    """Music library that stores songs and manages operations like adding, deleting, searching."""
    FILENAME = "songs.csv"

    def __init__(self):
        self.songs = []
        self.rbt = RedBlackTree()
        self.load_songs()

    def load_songs(self):
        """Load songs from a file into the music library."""
        if os.path.exists(self.FILENAME):
            with open(self.FILENAME, 'r') as file:
                for line in file:
                    if line.strip():
                        title, artist, album = line.strip().split(',')
                        song = Song(title, artist, album)
                        self.songs.append(song)
                        self.rbt.insert(song)
            print(f"{len(self.songs)} songs loaded from {self.FILENAME}.")
        else:
            print("No songs found. Starting with an empty music library.")

    def save_songs(self):
        """Save all songs to a file."""
        with open(self.FILENAME, 'w') as file:
            for song in self.songs:
                file.write(f"{song.title},{song.artist},{song.album}\n")
        print(f"{len(self.songs)} songs saved to {self.FILENAME}.")

    def add_song(self, title, artist, album):
        """Add a song to the library and save to file."""
        song = Song(title, artist, album)
        self.songs.append(song)
        self.rbt.insert(song)
        self.save_songs()
        print(f"'{song}' added to your music library.")

    def delete_song(self, title):
        """Delete a song from the library and save changes to file."""
        song_to_delete = next((s for s in self.songs if s.title == title), None)
        if song_to_delete:
            self.songs.remove(song_to_delete)
            self.save_songs()
            print(f"'{song_to_delete}' removed from your music library.")
        else:
            print(f"'{title}' not found in your music library.")

    def display_songs(self):
        """Display all songs in the library."""
        if self.songs:
            print("Your music library:")
            for i, song in enumerate(self.songs, 1):
                print(f"{i}. {song}")
        else:
            print("Your music library is empty.")

    def linear_search(self, title):
        """Perform a linear search for a song by title."""
        for index, song in enumerate(self.songs):
            if song.title == title:
                return index
        return -1

    def binary_search(self, title):
        """Perform a binary search using the Red-Black Tree."""
        song_to_search = Song(title, "", "")
        return self.rbt.search(song_to_search)

    def sort_songs(self):
        """Choose and execute a sorting algorithm."""
        while True:
            print("Choose sorting algorithm:")
            print("1. Bubble Sort")
            print("2. Insertion Sort")
            print("3. Merge Sort")
            print("4. Quick Sort")
            print("5. Back")

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                import time
                start_time = time.time()
                self.bubble_sort()
                print(f"Time taken: {time.time() - start_time:.6f} seconds.")
                self.save_songs()
            elif choice == '2':
                import time
                start_time = time.time()
                self.insertion_sort()
                print(f"Time taken: {time.time() - start_time:.6f} seconds.")
                self.save_songs()
            elif choice == '3':
                import time
                start_time = time.time()
                self.songs = self.merge_sort(self.songs)
                print(f"Time taken: {time.time() - start_time:.6f} seconds.")
                self.save_songs()
            elif choice == '4':
                import time
                start_time = time.time()
                self.quick_sort(0, len(self.songs) - 1)
                print(f"Time taken: {time.time() - start_time:.6f} seconds.")
                self.save_songs()
            elif choice == '5':
                # Go back to the main menu
                return
            else:
                print("Invalid choice. Please try again.")

    def bubble_sort(self):
        """Bubble sort algorithm to sort the songs."""
        n = len(self.songs)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if self.songs[j] > self.songs[j + 1]:
                    self.songs[j], self.songs[j + 1] = self.songs[j + 1], self.songs[j]
                    swapped = True
            if not swapped:
                break
        print("Sorted using Bubble Sort.")

    def insertion_sort(self):
        """Insertion sort algorithm to sort the songs."""
        for i in range(1, len(self.songs)):
            key_song = self.songs[i]
            j = i - 1
            while j >= 0 and key_song < self.songs[j]:
                self.songs[j + 1] = self.songs[j]
                j -= 1
            self.songs[j + 1] = key_song
        print("Sorted using Insertion Sort.")

    def merge_sort(self, array):
        """Merge sort algorithm."""
        if len(array) <= 1:
            return array

        mid = len(array) // 2
        left_half = self.merge_sort(array[:mid])
        right_half = self.merge_sort(array[mid:])

        return self.merge(left_half, right_half)

    def merge(self, left, right):
        """Helper function to merge two halves in merge sort."""
        result = []
        i = j = 0

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

    def quick_sort(self, low, high):
        """Quick sort algorithm."""
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi - 1)
            self.quick_sort(pi + 1, high)

    def partition(self, low, high):
        """Partition function for quick sort."""
        pivot = self.songs[high]
        i = low - 1

        for j in range(low, high):
            if self.songs[j] < pivot:
                i += 1
                self.songs[i], self.songs[j] = self.songs[j], self.songs[i]

        self.songs[i + 1], self.songs[high] = self.songs[high], self.songs[i + 1]
        return i + 1

    def create_random_songs(self, count):
        """Create a given number of random songs."""
        import random
        import string

        for _ in range(count):
            title = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5, 10)))
            artist = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5, 10)))
            album = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5, 10)))
            self.add_song(title, artist, album)


# Function to manage songs
def manage_songs(library):
    """Menu to manage songs in the music library."""
    while True:
        print("\nManage Songs")
        print("1. Display Songs")
        print("2. Add Song")
        print("3. Create Random Songs")
        print("4. Delete Song")
        print("5. Back")
        choice = input("Choose an option: ")
        if choice == '1':
            library.display_songs()
        elif choice == '2':
            title = input("Enter the song title: ")
            artist = input("Enter the artist: ")
            album = input("Enter the album: ")
            library.add_song(title, artist, album)
        elif choice == '3':
            count = int(input("Enter number of random songs to create: "))
            library.create_random_songs(count)
        elif choice == '4':
            title = input("Enter the title of the song to delete: ")
            library.delete_song(title)
        elif choice == '5':
            break
        else:
            print("Invalid option.")

# Function to search for songs
def search_songs(library):
    """Menu to search for songs in the music library."""
    while True:
        print("\nSearch Songs")
        print("1. Linear Search")
        print("2. Binary Search")
        print("3. Back")
        choice = input("Choose an option: ")
        if choice == '1':
            title = input("Enter the song title: ")
            result = library.linear_search(title)
            if result != -1:
                print(f"'{library.songs[result]}' found in your music library at position {result + 1}.")
            else:
                print(f"'{title}' not found in your music library.")
        elif choice == '2':
            title = input("Enter the song title: ")
            found = library.binary_search(title)
            if found:
                print(f"'{title}' found in your music library.")
            else:
                print(f"'{title}' not found in your music library.")
        elif choice == '3':
            break
        else:
            print("Invalid option.")


# Main function to manage the entire library
def main():
    """Main function to run the music library application."""
    library = MusicLibrary()
    print("Welcome to your Music Library")

    while True:
        print("\nMain Menu")
        print("1. Manage Songs")
        print("2. Search Songs")
        print("3. Sort Songs")
        print("4. Exit")

        main_choice = input("Choose an option: ")

        if main_choice == '1':
            manage_songs(library)
        elif main_choice == '2':
            search_songs(library)
        elif main_choice == '3':
            library.sort_songs()
        elif main_choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
