# Musikbibliothek - Dokumentation

Dieses Projekt implementiert eine **Musikbibliothek**, die es ermöglicht, Lieder hinzuzufügen, zu verwalten, zu durchsuchen und zu sortieren. Dabei kommt ein **Rot-Schwarz-Baum** zur effizienten Verwaltung der Lieder zum Einsatz.

## Inhaltsverzeichnis

- [Klassen](#klassen)
  - [Song](#song)
  - [MusicLibrary](#musiclibrary)
- [Funktionen](#funktionen)
  - [manage_songs](#manage_songs)
  - [sort_songs](#sort_songs)
  - [search_songs](#search_songs)
  - [main](#main)
- [Vorgehen](#vorgehen)
- [Komplexität (Big-O-Notation)](#komplexität-big-o-notation)
- [Herausforderungen](#herausforderungen)





## Klassen

### Song

Repräsentiert ein Lied mit den Attributen Titel, Künstler und Album.

#### Methoden:

- `__init__(self, title, artist, album)`
  - Initialisiert ein neues `Song`-Objekt mit Titel, Künstler und Album.
  
- `__str__(self)`
  - Gibt eine formatierte Zeichenkette zurück, die das Lied beschreibt.
  
- `__lt__(self, other)`
  - Ermöglicht den Vergleich zweier Lieder auf Basis von Titel, Künstler und Album.
  
- `__eq__(self, other)`
  - Überprüft, ob zwei Lieder gleich sind, indem Titel, Künstler und Album verglichen werden.


### MusicLibrary

Eine Klasse, die die Musikbibliothek verwaltet. Sie enthält Lieder und verwendet einen Rot-Schwarz-Baum für die effiziente Suche und Sortierung.

#### Methoden:

- `__init__(self)`
  - Initialisiert die Bibliothek, lädt Lieder aus einer Datei und fügt sie dem Rot-Schwarz-Baum hinzu.
  
- `load_songs(self)`
  - Lädt Lieder aus einer Datei.
  
- `save_songs(self)`
  - Speichert Lieder in eine Datei.
  
- `add_song(self, title, artist, album)`
  - Fügt ein neues Lied zur Bibliothek hinzu und speichert die Änderungen.
  
- `delete_song(self, title)`
  - Löscht ein Lied aus der Bibliothek und speichert die Änderungen.
  
- `display_songs(self)`
  - Zeigt alle Lieder in der Bibliothek an.
  
- `linear_search(self, title)`
  - Sucht linear nach einem Lied in der Bibliothek und misst die Laufzeit.
  
- `binary_search(self, title)`
  - Führt eine binäre Suche im Rot-Schwarz-Baum durch.
  
- `interpolation_search(self, title)`
  - Implementiert den Interpolations-Suchalgorithmus für eine sortierte Liste.
  
- `exponential_search(self, title)`
  - Führt die exponentielle Suche für eine sortierte Liste durch.
  
- `bubble_sort(self)`
  - Sortiert die Lieder mit dem Bubble-Sort-Algorithmus und misst die Laufzeit.
  
- `insertion_sort(self)`
  - Sortiert die Lieder mit dem Insertion-Sort-Algorithmus und misst die Laufzeit.
  
- `merge_sort(self, array=None)`
  - Implementiert den Merge-Sort-Algorithmus.
  
- `_merge(self, left, right)`
  - Hilfsmethode zum Mischen zweier Arrays während des Merge-Sort-Vorgangs.
  
- `heap_sort(self)`
  - Implementiert den Heap-Sort-Algorithmus.

- `create_random_songs(self, count)`
  - Erstellt eine definierte Anzahl zufälliger Lieder.

## Funktionen

### manage_songs

Ermöglicht das Verwalten der Lieder in der Musikbibliothek. Hier können Lieder hinzugefügt, gelöscht oder angezeigt werden.

### sort_songs

Bietet eine Auswahl von Sortieralgorithmen, darunter **Bubble Sort**, **Insertion Sort**, **Merge Sort** und **Heap Sort**, die auf die Musikbibliothek angewendet werden können.

### search_songs

Bietet mehrere Suchalgorithmen an, um Lieder in der Musikbibliothek zu finden, darunter **Lineare Suche**, **Binäre Suche**, **Interpolation Search** und **Exponential Search**.

### main

Startet das Hauptprogramm und zeigt das Hauptmenü der Musikbibliothek.

## Vorgehen

1. Der Benutzer kann Lieder hinzufügen oder löschen und die gesamte Liste der Lieder anzeigen.
2. Verschiedene Suchalgorithmen (linear, binär, etc.) können zur Suche verwendet werden.
3. Die Lieder können nach verschiedenen Kriterien sortiert werden, um die Performance der Algorithmen zu vergleichen.

## Komplexität (Big-O-Notation)

- **Lineare Suche**: O(n)
- **Binäre Suche**: O(log n) (unter der Voraussetzung, dass die Liste sortiert ist)
- **Bubble Sort**: O(n²)
- **Insertion Sort**: O(n²)
- **Merge Sort**: O(n log n)
- **Heap Sort**: O(n log n)
- **Rot-Schwarz-Baum Einfügen/Suchen**: O(log n)

## Herausforderungen
