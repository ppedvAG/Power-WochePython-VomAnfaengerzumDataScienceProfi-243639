# Schleifen
# Code mehrmals ausführen

# while-Schleife
# Führt den Code innerhalb solange aus, wie die Bedingung True ist

z1 = 0
z2 = 10
while z1 < z2:  # Führe den Code solange aus, bis z1 auf 10 ist
	print(z1)
	z1 += 1
# Springe zum Kopf zurück

# Wenn der Schleifenkopf aus False evaluiert wird, geht der Code nach der Schleife weiter
print("while fertig")

# Else bei Schleifen
# Wird ausgeführt, wenn die Schleife erfolgreich beendet wird (ohne break)
a = 0
while a < 10:
	print(a)
	a += 1
else:
	print("while a fertig")

# break und continue
# break: Beendet die Schleife an dieser Stelle
# continue: Überspringe den Rest der Schleife und springe zum Schleifenkopf zurück
b = 0
while b < 100:
	print(b)
	b += 1
	if b > 10:
		break  # Beende ab 10 die Schleife

c = 0
while c < 100:
	c += 1
	if c % 2 == 0:
		continue  # Wenn c durch 2 teilbar ist, überspringe den Rest (Ausgabe)
	print(c)  # 1, 3, 5, 7, 9, 11, ... (alle ungeraden Zahlen)

################################################################

# for-Schleife
# Geht eine Liste durch
# Benötigt eine Liste (list, tuple, set, dict, string, ...)
# Bei jedem Schleifendurchgang haben wir Zugriff aus das derzeitige Element
h = ["Hallo", "Welt", "!"]

for x in h:  # x ist das derzeitige Element
	print(x)  # "Hallo", "Welt", "!"
# Zeiger wird auf das nächste Element bewegt

zahlen = [8, 3, 5, 1, 2]
for z in zahlen:  # z ist die derzeitige Zahl
	print(z * 2)

# Beispiel Übung 4
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7, 8, 9]
alleListen = [list1, list2, list3]

# Größte Länge ermitteln
maxLen = 0
for liste in alleListen:
	laenge = len(liste)  # Die Länge der jetztigen Liste
	if laenge > maxLen:  # Ist die Länge der jetztigen Liste größer als die bisherige längste Liste?
		maxLen = laenge  # Wenn ja, speichere die größte in der Zwischenspeichervariable

# Ausgabe der längsten Liste (Information)
for liste in alleListen:
	if len(liste) == maxLen:
		print(str(liste) + " ist eine der längsten Listen")

# for-Schleife auf einen String
text = "Hallo Welt!"
for z in text:  # z ist das derzeitige Zeichen
	print(z)

# for-Schleife mit Range
for z in range(10):
	print(z)

for z in range(100):
	if z % 2 == 0:
		print(z)

################################################################

# Verschachtelte Schleifen
for x in range(5):  # Die äußere Schleife wird 5 mal ausgeführt
	for y in range(5):  # Die innere Schleife wird auch 5 mal ausgeführt
		print(str(x) + " " + str(y))  # Alle Kombinationen von 0, 0 bis 4, 4 (25 Outputs)
# -> Insgesamt außen * innen Ausführungen (5 * 5 = 25)

################################################################

# fstring
# Formatted String
# Ermöglicht, Code in einen String einzubetten
# Wird mit f vor dem String definiert
# Code wird { } eingebaut
f = 24
# print("Die Zahl ist " + f)  # Nicht möglich, da string und int nicht addiert werden dürfen
print("Die Zahl ist " + str(f))
print(f"Die Zahl ist {f}")

print("Die Zahl ist " + str(f) + ", die Zahl hoch 2 ist " + str(f ** 2))
print(f"Die Zahl ist {f}, die Zahl hoch 2 ist {f ** 2}")

# Schleife mit fstring
for i in range(1, 11):
	print("Die Zahl ist: " + str(i))
	print("Die Zahl ist hoch 2: " + str(i ** 2))
	print(str(i) + "^2=" + str(i ** 2))

for i in range(1, 11):
	print(f"Die Zahl ist: {i}")
	print(f"Die Zahl ist hoch 2: {i ** 2}")
	print(f"{i}^2={i ** 2}")