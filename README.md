# Musikbibliothek - Dokumentation

## Inhaltsverzeichnis

- [Klassen](#klassen)
  - [Song](#song)
  - [RedBlackNode](#redblacknode)
  - [RedBlackTree](#redblacktree)
  - [MusicLibrary](#musiclibrary)
- [Funktionen](#funktionen)
  - [manage_songs](#manage_songs)
  - [sort_songs](#sort_songs)
  - [search_songs](#search_songs)
  - [main](#main)

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

### RedBlackNode

Repräsentiert einen Knoten in einem Rot-Schwarz-Baum, der ein Lied speichert und Verweise auf Eltern-, Kinderknoten sowie die Farbe des Knotens enthält.

#### Methoden:

- `__init__(self, song)`
  - Initialisiert einen neuen Knoten mit einem Lied. Standardmäßig ist die Farbe des Knotens "RED". Ein spezieller NIL-Knoten hat die Farbe "BLACK".

### RedBlackTree

Implementiert einen Rot-Schwarz-Baum zur effizienten Verwaltung und Suche von Liedern.

#### Methoden:

- `__init__(self)`
  - Initialisiert einen leeren Rot-Schwarz-Baum mit einem NIL-Knoten.
  
- `insert(self, song)`
  - Fügt ein neues Lied in den Baum ein und stellt die Baumstruktur sicher.
  
- `fix_insert(self, node)`
  - Korrigiert den Baum nach der Einfügeoperation, um die Rot-Schwarz-Eigenschaften zu gewährleisten.
  
- `left_rotate(self, x)`
  - Führt eine Linksrotation durch.
  
- `right_rotate(self, x)`
  - Führt eine Rechtsrotation durch.
  
- `search(self, song)`
  - Sucht nach einem Lied im Baum und misst die Laufzeit.
  
- `_search_recursive(self, node, song)`
  - Rekursive Hilfsfunktion für die Suche im Baum.

### MusicLibrary

Eine Klasse, die die Musikbibliothek verwaltet. Sie enthält Lieder und verwendet einen Rot-Schwarz-Baum für die effiziente Suche.

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
  
- `merge_sort(self, array)`
  - Implementiert den Merge-Sort-Algorithmus.
  
- `_merge(self, left, right)`
  - Hilfsmethode zum Mischen zweier Arrays während des Merge-Sort-Vorgangs.
  
- `quick_sort(self, low, high)`
  - Implementiert den Quick-Sort-Algorithmus.
  
- `_partition(self, low, high)`
  - Partitioniert die Liste für den Quick-Sort-Algorithmus.
  
- `create_random_songs(self, count)`
  - Erstellt eine definierte Anzahl zufälliger Lieder.

## Funktionen

### manage_songs


## Vorgehen

## Big O notation

## Herausforderungen
