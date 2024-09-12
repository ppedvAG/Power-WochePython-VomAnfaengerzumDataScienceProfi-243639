# Listentypen
# Variablen die nicht nur einen Wert halten können, sondern mehrere Werte

# List
# Wird mit [ ] definiert
# Hat einen Index
# Ist unsortiert
# Kann Duplikate enthalten
# Kann verschiedene Typen enthalten

a = [1, 2, 3, 4, 5]  # [Element1, Element2, ...]
print(a)  # Gibt die gesamte Liste in der Konsole aus

print(a[0])  # Index möglich

print(len(a))  # Anzahl Elemente: 5

# Listenfunktionen

# list.append(Element)
# Fügt ein Element hinzu
a.append("Hallo Welt")
print(a)

# list.pop(Index)
# Entfernt ein Element am gegebenen Index
a.pop(3)
print(a)

# list.sort()
# Sortiert die Liste
a.pop(4)
a.sort()  # Liste kann nicht sortiert werden, wenn gemischte Typen enthalten sind
print(a)

# sort kann auch eine Richtung bekommen
a.sort(reverse=True)  # Funktion konfigurieren mittels benannten Parametern
print(a)

# Zwei Listen zusammenhängen
b = ["a", "b", "c"]
a.append(b)
print(a)

# Nicht möglich mit append, stattdessen extend oder += benutzen
a.remove(b)  # remove: Sucht nach dem gegebenen Element und entfernt das erste Vorkommnis
a.extend(b)
print(a)

a += b
print(a)

################################################################

# Tupel
# Funktioniert wie List, ist aber nicht veränderbar
# Wird vorallem für Daten verwendet, welche final sind
# z.B. Messdaten, Informationen aus dem Internet, ...
c = (1, 2, 3)  # Normale Klammern statt eckigen Klammern
print(type(a))  # <class 'list'>
print(type(c))  # <class 'tuple'>

# Unpacking
# Inhalte einer Liste in einzelne Variablen zerlegen
# z.B. List, Tuple, String, ...
x, y, z = c
print(x)
print(y)
print(z)

# Tupel über Umwege verändern über Konvertierung
l = list(c)
l.append(4)
c = tuple(l)
print(c)

################################################################

# range
# Bereich von X bis Y
r = range(10)  # Nur ein Generator für die Zahlen
print(r)

print(list(r))  # Generator ausführen mittels list(r)
print(tuple(r))

# range von X bis Y
print(list(range(50, 100)))

# range von X bis Y mit Schrittgröße
print(list(range(50, 101, 5)))  # Obergrenze nicht inkludiert -> 101

################################################################

# Set
# Liste von Elemente welche alle eindeutig sein müssen
s = {1, 2, 3}  # Wird mit { } dargestellt

s.add(3)  # Fügt ein Element hinzu, wenn dieses noch nicht existiert
print(s)

# Anwendungsfall: Duplikate filtern
d = [1, 2, 2, 3, 3, 3, 3, 4]
d = set(d)
d = list(d)
print(d)

################################################################

# Dictionary
# Funktioniert wie ein Set, aber jeder Wert hat einen Namen (Schlüssel)
# Jeder Inhalt eines Sets muss eindeutig sein, hier muss jeder Schlüssel eindeutig sein
h = {
	"Wert1": "Hallo",
	"Wert2": "Welt",
	"Wert3": "!"
}

print(h["Wert1"])  # Dictionary angreifen mittels [String]
# Generell sollten alle Schlüssel Strings sein

print({ False: 0, True: 1 })  # False und True als Schlüssel (nicht sinnvoll)
print({ 0: False, 1: True })  # 0 und 1 als Schlüssel (nicht sinnvoll)

# Praktisches Beispiel: Person
person = {
	"Vorname": "Max",
	"Nachname": "Mustermann",
	"Alter": 33
}
print(person)

# Neuen Wert hinzufügen
person["Hoehe"] = 180
print(person)

# person.update({"Gewicht": 80})
person.setdefault("Gewicht", 80)
print(person)

# Wert entfernen
person.pop("Hoehe")
print(person)

# Einzelteile des Dictionaries entnehmen
print(person.keys())  # Liste mit Keys
print(person.values())  # Liste mit Values
print(person.items())  # Liste mit Tupeln von allen Keys + Valuse

################################################################

# Konvertierungen
# Typen von Variablen verändern

# z.B. Kommastellen von Kommazahlen abschneiden
z = 21948.9483
i = int(z)
print(i)

# Listen zu anderen Listen
x = [1, 2, 3, 4]
print(tuple(x))
print(set(x))
print(list("Hallo"))

# int -> bool
print(bool(5))  # 5 zu True oder False konvertieren
print(bool(0))  # Alles was nicht 0 ist ist True
print(bool("Hallo"))  # True
print(bool(None))  # None ist auch False

# int -> str
z1 = 10
z2 = 20
print(z1 + z2)
# print(str(z1) + z2)
print(str(z1) + str(z2))