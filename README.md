# Musikbibliothek - Dokumentation

Dieses Projekt implementiert eine **Musikbibliothek**, die eine effiziente Verwaltung, Suche und Sortierung von Liedern ermöglicht. Der Kern des Systems basiert auf einem **Rot-Schwarz-Baum**, um Lieder schnell und speicheroptimiert zu speichern und abzurufen. Außerdem stehen dem Benutzer mehrere Sortier- und Suchalgorithmen zur Verfügung, um verschiedene Anwendungsfälle zu unterstützen.

## Inhaltsverzeichnis

- [Projektbeschreibung](#projektbeschreibung)
- [Klassen](#klassen)
  - [Song](#song)
  - [RedBlackTree](#redblacktree)
  - [MusicLibrary](#musiclibrary)
- [Menü-Funktionen](#funktionen)
  - [manage_songs](#manage_songs)
  - [sort_songs](#sort_songs)
  - [search_songs](#search_songs)
  - [main](#main)
- [Vorgehen](#vorgehen)
- [Komplexität (Big-O-Notation)](#komplexität-big-o-notation)
- [Herausforderungen](#herausforderungen)
- [Zukünftige Erweiterungen](#zukünftige-erweiterungen)

---

## Projektbeschreibung

Die **Musikbibliothek** ermöglicht es, eine Sammlung von Liedern in einer Datei zu speichern und diese mithilfe eines Rot-Schwarz-Baums effizient zu verwalten. Lieder können hinzugefügt, gelöscht, durchsucht und sortiert werden. Darüber hinaus bietet die Anwendung Favoriten-Management und die Möglichkeit, zufällige Lieder zu erstellen. Der Benutzer hat die Wahl zwischen mehreren Sortieralgorithmen (z. B. Bubble Sort, Merge Sort) und Suchalgorithmen (z. B. Lineare Suche, Binäre Suche).

---

## Klassen

### Song

Die `Song`-Klasse repräsentiert ein Lied mit den Attributen Titel, Künstler und Album. Diese Klasse wird verwendet, um Lieder in der Bibliothek darzustellen und zu vergleichen.

#### Attribute:
- `title`: Titel des Liedes
- `artist`: Künstler des Liedes
- `album`: Album, in dem das Lied enthalten ist

#### Methoden:

- `__init__(self, title, artist, album)`: Initialisiert ein neues `Song`-Objekt.
- `__str__(self)`: Gibt eine formatierte Zeichenkette zurück, die den Song beschreibt (z. B. "Titel von Künstler (Album)").
- `__lt__(self, other)`: Vergleicht zwei Songs anhand des Titels, Künstlers und Albums.
- `__eq__(self, other)`: Überprüft die Gleichheit zweier Songs durch Vergleich von Titel, Künstler und Album.

### RedBlackTree

Der `RedBlackTree` ist die Implementierung eines Rot-Schwarz-Baums. Diese Datenstruktur sorgt für eine balancierte und effiziente Speicherung der Songs.

#### Attribute:
- `root`: Der Wurzelknoten des Baums.
- `NIL`: Ein Sentinel-Knoten, der als Platzhalter für `None`-Knoten verwendet wird.

#### Methoden:

- `insert(self, song)`: Fügt einen Song in den Baum ein.
- `fix_insert(self, node)`: Korrigiert den Baum nach dem Einfügen eines Knotens, um die Rot-Schwarz-Eigenschaften zu erhalten.
- `search(self, song)`: Sucht nach einem Song im Baum.
- `left_rotate(self, x)`, `right_rotate(self, x)`: Rotationsoperationen zur Strukturänderung des Baums.

### MusicLibrary

Die `MusicLibrary` verwaltet die gesamte Sammlung von Songs und verwendet einen Rot-Schwarz-Baum für die Speicherung. Zudem bietet sie Funktionen zur Suche, Sortierung und Verwaltung von Favoriten.

#### Attribute:
- `songs`: Liste der Songs in der Bibliothek.
- `favorites`: Liste der Favoriten-Songs.
- `rbt`: Instanz des `RedBlackTree`, um Songs effizient zu verwalten.

#### Methoden:

- `load_songs(self)`: Lädt Songs aus einer CSV-Datei.
- `save_songs(self)`: Speichert die aktuelle Liste der Songs in einer Datei.
- `add_song(self, title, artist, album)`: Fügt einen Song der Bibliothek hinzu.
- `delete_song(self, title)`: Entfernt einen Song aus der Bibliothek.
- `display_songs(self)`: Zeigt alle Songs in der Bibliothek an.
- `create_random_songs(self, count)`: Erstellt eine definierte Anzahl zufälliger Songs.
- `linear_search(self, title)`: Führt eine lineare Suche nach einem Song durch.
- `binary_search(self, title)`: Führt eine binäre Suche auf dem Rot-Schwarz-Baum durch.
- `interpolation_search(self, title)`: Implementiert den Interpolations-Suchalgorithmus für eine sortierte Liste.
- `exponential_search(self, title)`: Führt eine exponentielle Suche durch.
- `bubble_sort(self)`, `insertion_sort(self)`, `merge_sort(self)`, `heap_sort(self)`: Verschiedene Sortieralgorithmen.
- `add_favorite(self, title)`, `remove_favorite(self, title)`: Verwaltung von Favoriten.
- `display_favorites(self)`: Zeigt alle Favoriten an.

---

## Menü-Funktionen

### manage_songs

Diese Funktion ermöglicht das Verwalten der Songs in der Bibliothek, darunter das Hinzufügen, Erstellen zufälliger Songs und das Löschen.

### sort_songs

Ermöglicht dem Benutzer, verschiedene Sortieralgorithmen auf die Songs anzuwenden.

### search_songs

Bietet mehrere Suchalgorithmen an, um Songs in der Bibliothek zu finden.

### main

Der Einstiegspunkt des Programms. Das Hauptmenü wird angezeigt, um dem Benutzer die Verwaltung der Musikbibliothek zu ermöglichen.

---

## Vorgehen

Beim Programmieren dieses Projekts wurden mehrere Schritte durchgeführt, um die verschiedenen Such- und Sortieralgorithmen zu implementieren, zu testen und die Musikbibliothek zu optimieren. Der folgende Ablauf beschreibt den Prozess im Detail:

### 1. Implementierung der Sortier- und Suchalgorithmen
Zunächst lag der Fokus auf der Implementierung verschiedener Sortier- und Suchalgorithmen. Die folgenden Sortieralgorithmen wurden in die Musikbibliothek eingebaut:
- **Bubble Sort**
- **Insertion Sort**
- **Merge Sort**
- **Heap Sort**

Zusätzlich wurden Suchalgorithmen hinzugefügt, um effizient nach Songs in der Bibliothek zu suchen:
- **Lineare Suche**
- **Binäre Suche**
- **Interpolationssuche**
- **Exponentialsuche**

### 2. Testen der Algorithmen mit verschiedenen Datensätzen
Nach der Implementierung der Algorithmen wurden sie getestet, um ihre Leistung in Bezug auf Geschwindigkeit und Effizienz zu messen. Dabei wurden zwei Datensätze verwendet:
- **10.000 Einträge**: Zunächst wurde die Musikbibliothek mit 10.000 zufälligen Songs befüllt. Jeder Algorithmus wurde mehrfach auf diese Daten angewendet, um seine Effizienz zu messen.
- **50.000 Einträge**: Nach dem Testen auf dem kleineren Datensatz wurde die Anzahl der Songs auf 50.000 erhöht, um die Skalierbarkeit der Algorithmen zu prüfen. Hier wurden die Ausführungszeiten erneut erfasst, um zu sehen, wie sich die Algorithmen bei wachsender Datenmenge verhalten.

### 3. Entfernung der Laufzeitmessungsfunktionen
Nach den Leistungstests und der Analyse der Algorithmen wurde der Code bereinigt. Die Funktionen zur **Laufzeitmessung** wurden entfernt, da sie nur während der Testphase erforderlich waren. Diese Änderungen machten den Code leichter lesbar und wartbar. Trotz der Entfernung der Laufzeitmessung blieben alle Algorithmen in der endgültigen Version des Projekts enthalten, um dem Benutzer Flexibilität in der Sortierung und Suche zu bieten.

### 4. Sortierung der Algorithmen nach Effizienz für den Benutzer
Basierend auf den Leistungstests wurde festgestellt, welche Algorithmen für große Datensätze am effizientesten sind. Die Algorithmen wurden daher in den Menüs so angeordnet, dass die schnelleren Algorithmen zuerst zur Auswahl stehen, um den Benutzern eine bessere Benutzererfahrung zu bieten. Beispielsweise wurden **Merge Sort** und **Heap Sort** an prominenter Stelle platziert, da sie sich als effizienter als **Bubble Sort** und **Insertion Sort** erwiesen.

### 5. Verbesserung der Menüfunktionen
Nachdem die Algorithmen getestet und optimiert waren, wurde das Menü der Anwendung verbessert. Diese Verbesserungen umfassten:
- **Benutzerfreundliche Menüs**: Die Menüführung wurde vereinfacht, um dem Benutzer eine intuitive Navigation durch die verschiedenen Funktionen der Musikbibliothek zu ermöglichen. Es wurden klare Anweisungen und Optionen angeboten, um Verwirrung zu vermeiden.
- **Menü für Favoritenverwaltung**: Zusätzlich wurde die Möglichkeit hinzugefügt, **Favoriten** zu speichern und zu verwalten. Benutzer können jetzt Songs als Favoriten markieren und diese in einer separaten Liste speichern. Diese Funktionalität wurde durch das Hinzufügen von Speicher- und Ladefunktionen für Favoriten realisiert.

---

## Komplexität (Big-O-Notation)

Im Folgenden werden die gemessenen Laufzeiten der getesteten Algorithmen gegenübergestellt, die zur Sortierung der Algorithmen im Skript geführt haben. Anschließend wird die
Big-O-Notation der Algorithmen erläutert.

## Sortieren von 50.000 Elementen

### Insertion Sort
![Insertion Sort 50000](path/to/Screenshot Insertion Sort 50000.png)
- **Big-O-Notation:** O(n²)

### Merge Sort
![Merge Sort 50000](path/to/Screenshot Merge Sort 50000.png)
- **Big-O-Notation:** O(n log n)

### Heap Sort
![Heap Sort 50000](path/to/Screenshot Heap sort 50000.png)
- **Big-O-Notation:** O(n log n)

### Bubble Sort
![Bubble Sort 50000](path/to/Screenshot Bubble Sort 50000.png)
- **Big-O-Notation:** O(n²)

## Sortieren von 10.000 Elementen

### Insertion Sort
![Insertion Sort 10000](path/to/Screenshot Insertion Sort.png)
- **Big-O-Notation:** O(n²)

### Merge Sort
![Merge Sort 10000](path/to/Screenshot Merge sort.png)
- **Big-O-Notation:** O(n log n)

### Heap Sort
![Heap Sort 10000](path/to/Screenshot Heap sort.png)
- **Big-O-Notation:** O(n log n)

### Bubble Sort
![Bubble Sort 10000](path/to/Screenshot Bubble_sort.png)
- **Big-O-Notation:** O(n²)

Big-O-Notationen der angegebenen Suchalgorithmen:

- **Exponential Search**: O(log n) für den binären Suchteil (nachdem der Bereich eingegrenzt wurde)
  - Wird verwendet, um effizient in einem exponentiell wachsenden Bereich zu suchen, und nutzt binäre Suche, sobald ein Bereich gefunden wurde.

- **Binäre Suche (Binary Search)**: O(log n)
  - Funktioniert nur auf sortierten Daten. Teilt das Suchfeld bei jedem Schritt in der Mitte und sucht in einer der Hälften weiter.

- **Interpolation Search**: O(log log n) im besten Fall, O(n) im schlechtesten Fall
  - Eine optimierte Suche für gleichmäßig verteilte Daten, die die Position der mittleren Zahl schätzt und basierend auf dieser Schätzung sucht.

- **Lineare Suche (Linear Search)**: O(n)
  - Durchsucht das Array elementweise von Anfang bis Ende, bis der gesuchte Wert gefunden wird.


---

## Herausforderungen

Während der Entwicklung des Projekts traten mehrere Herausforderungen auf, die den Prozess verlangsamt und zusätzliche Aufmerksamkeit erfordert haben. Hier sind die wichtigsten Schwierigkeiten, die während der Programmierung gemeistert werden mussten:

1. **Verständnis der verschiedenen Algorithmen**
   - Eine der größten Herausforderungen war das **Verständnis der Such- und Sortieralgorithmen**. Insbesondere die tiefergehenden Konzepte hinter komplexeren Algorithmen wie **Merge Sort**, **Heap Sort**, und den Suchalgorithmen wie der **Interpolationssuche** und **Exponentialsuche** waren anspruchsvoll. Diese Algorithmen erfordern ein gutes Verständnis von Datenstrukturen und Rekursion, was Zeit und Einarbeitung in die jeweilige Funktionsweise erforderte.
   - Die Komplexität der Algorithmen selbst, wie zum Beispiel das richtige Setzen von Bedingungen in rekursiven Suchfunktionen oder das Vermeiden von Endlosschleifen bei der Sortierung, führte oft zu Fehlern, die erst durch intensives Debugging gefunden wurden.

2. **Korrekte Implementierung der Algorithmen**
   - Auch nach dem Verständnis der Algorithmen war die **korrekte Implementierung** eine Herausforderung. Selbst kleine Fehler, wie die falsche Handhabung von Indizes oder unsachgemäße Vergleiche von Objekten (Songs), konnten dazu führen, dass die Algorithmen nicht wie erwartet funktionierten.
   - Besonders schwierig war es, sicherzustellen, dass die Algorithmen auch für größere Datensätze wie 50.000 Einträge stabil und effizient liefen. Hier traten oft unerwartete Probleme wie zu hohe Speicheranforderungen oder längere Laufzeiten auf, die durch weitere Optimierungen gelöst werden mussten.

3. **Probleme bei der Laufzeitmessung**
   - Die Implementierung der **Laufzeitmessung** brachte ebenfalls Probleme mit sich. Einerseits war es notwendig, die Zeit für die Ausführung der Algorithmen genau zu messen, um ihre Effizienz zu vergleichen. Andererseits durfte die Laufzeitmessung die eigentlichen Abläufe nicht beeinflussen.
   - Bei der Messung der Laufzeit für Algorithmen wie Merge Sort oder Interpolation Search führte die zusätzliche Zeit, die für die Initialisierung von Listen oder Arrays benötigt wurde, zu ungenauen Ergebnissen. Auch das richtige Platzieren der Messpunkte (vor und nach den Algorithmen) war wichtig, um realistische Messungen zu erhalten.

4. **Umfang des Codes**
   - Ein weiteres Problem war der **umfangreiche Code**, der sich durch die Vielzahl von Algorithmen und Funktionen angesammelt hat. Das Projekt wuchs schnell, da jeder Algorithmus seine eigene Implementierung und oft auch Hilfsfunktionen benötigte. Dies führte zu einem **komplexen Code**, der schwer zu überblicken und zu warten war.
   - Bei so vielen Algorithmen und Funktionen war es zudem schwierig, **duplizierten Code** zu vermeiden und dennoch eine klare Struktur zu bewahren. Es war notwendig, wiederkehrende Funktionalitäten auszulagern und in Hilfsfunktionen zu kapseln, um den Code sauber und übersichtlich zu halten.

5. **Menülogik und Benutzerführung**
   - Eine weitere Herausforderung lag darin, eine **einfache und intuitive Menüführung** zu entwickeln. Da das Programm viele Funktionen und Optionen bietet, war es eine Herausforderung, die Benutzeroberfläche klar und verständlich zu gestalten, ohne den Benutzer zu überfordern.
   - Insbesondere die Verwaltung von Favoriten und die Einbindung der verschiedenen Algorithmen in die Menüs musste gut durchdacht werden, um die Navigation durch die verschiedenen Funktionen für den Endbenutzer so einfach wie möglich zu gestalten.

---
