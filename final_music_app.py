import os
import time
import random
import string

class Song:
    """Class to represent a song with title, artist, and album."""
    def __init__(self, title, artist, album):
        self.title = title
        self.artist = artist
        self.album = album

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.album})"

    def __lt__(self, other):
        """Compare songs based on title, artist, and album."""
        if self.title == other.title:
            if self.artist == other.artist:
                return self.album < other.album
            return self.artist < other.artist
        return self.title < other.title

    def __eq__(self, other):
        """Check if two songs are equal."""
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
    """Red-Black Tree implementation to store songs."""
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
        """Fix the Red-Black Tree after an insertion."""
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
        """Perform a left rotation."""
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
        """Perform a right rotation."""
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
        """Helper method for recursive search."""
        if node == self.NIL or node.song == song:
            return node != self.NIL
        if song < node.song:
            return self._search_recursive(node.left, song)
        return self._search_recursive(node.right, song)


class MusicLibrary:
    """Music library for managing songs."""
    FILENAME = "songs.csv"

    def __init__(self):
        self.songs = []
        self.rbt = RedBlackTree()
        self.load_songs()

    def load_songs(self):
        """Load songs from the file."""
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
            print("No songs found. Starting with an empty library.")

    def save_songs(self):
        """Save songs to a file."""
        with open(self.FILENAME, 'w') as file:
            for song in self.songs:
                file.write(f"{song.title},{song.artist},{song.album}\n")
        print(f"{len(self.songs)} songs saved to {self.FILENAME}.")

    def add_song(self, title, artist, album):
        """Add a new song to the library."""
        song = Song(title, artist, album)
        self.songs.append(song)
        self.rbt.insert(song)
        self.save_songs()
        print(f"'{song}' added to your music library.")

    def delete_song(self, title):
        """Delete a song by title."""
        song_to_delete = next((s for s in self.songs if s.title == title), None)
        if song_to_delete:
            self.songs.remove(song_to_delete)
            self.save_songs()
            print(f"'{song_to_delete}' removed from your music library.")
        else:
            print(f"'{title}' not found.")

    def display_songs(self):
        """Display all songs in the library."""
        if self.songs:
            print("Your music library:")
            for i, song in enumerate(self.songs, 1):
                print(f"{i}. {song}")
        else:
            print("Your music library is empty.")

    def linear_search(self, title):
        """Perform a linear search by title."""
        for index, song in enumerate(self.songs):
            if song.title == title:
                return index
        return -1

    def binary_search(self, title):
        """Perform a binary search using the Red-Black Tree."""
        song_to_search = Song(title, "", "")
        return self.rbt.search(song_to_search)

    def sort_songs(self):
        """Display sorting options and execute sorting."""
        while True:
            print("Choose sorting algorithm:")
            print("1. Bubble Sort")
            print("2. Insertion Sort")
            print("3. Merge Sort")
            print("4. Quick Sort")
            print("5. Back")
            choice = input("Enter your choice: ").strip()

            if choice == '1':
                self._measure_sort_time(self.bubble_sort)
            elif choice == '2':
                self._measure_sort_time(self.insertion_sort)
            elif choice == '3':
                self._measure_sort_time(lambda: self.merge_sort(self.songs))
            elif choice == '4':
                self._measure_sort_time(lambda: self.quick_sort(0, len(self.songs) - 1))
            elif choice == '5':
                return
            else:
                print("Invalid choice. Please try again.")

    def _measure_sort_time(self, sort_function):
        """Measure and display the time taken by a sorting algorithm."""
        start_time = time.time()
        sort_function()
        print(f"Time taken: {time.time() - start_time:.6f} seconds.")
        self.save_songs()

    def bubble_sort(self):
        """Bubble sort algorithm."""
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
        """Insertion sort algorithm."""
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
        return self._merge(left_half, right_half)

    def _merge(self, left, right):
        """Helper method to merge two arrays."""
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

    def quick_sort(self, low, high):
        """Quick sort algorithm."""
        if low < high:
            pi = self._partition(low, high)
            self.quick_sort(low, pi - 1)
            self.quick_sort(pi + 1, high)

    def _partition(self, low, high):
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
        """Create random songs."""
        for _ in range(count):
            title = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5, 10)))
            artist = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5, 10)))
            album = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5, 10)))
            self.add_song(title, artist, album)


# Functions for menu management

def manage_songs(library):
    """Manage songs in the library."""
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


def search_songs(library):
    """Search for songs in the library."""
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
                print(f"'{library.songs[result]}' found at position {result + 1}.")
            else:
                print(f"'{title}' not found.")
        elif choice == '2':
            title = input("Enter the song title: ")
            found = library.binary_search(title)
            if found:
                print(f"'{title}' found in your music library.")
            else:
                print(f"'{title}' not found.")
        elif choice == '3':
            break
        else:
            print("Invalid option.")


# Main function

def main():
    """Main program to run the music library."""
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
