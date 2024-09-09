# If-Abfragen
# Prüfen, ob eine bestimmte Bedingung zur Ausführung der Codezeile gültig ist

z1 = 5
z2 = 3

if z1 > z2:  # Wenn z1 größer als z2 ist...
	print("z1 ist größer als z2")  # ... führe dieses Statement aus

# WICHTIG: Einrückungen beachten
if z1 > z2:
	print("z1 ist größer als z2")
	print("In der if")  # Eine Einrückung
print("Nach der if")  # Keine Einrückung


# Else-Statement
if z1 > z2:  # Wenn z1 größer als z2 ist...
	print("z1 ist größer als z2")  # ... führe dieses Statement aus
else:  # ... ansonsten ...
	print("z1 ist kleiner oder gleich z2")  # ... führe dieses Statement aus


# Elif-Statement
# Else mit Bedingung
if z1 > z2:  # Wenn z1 größer als z2 ist...
	print("z1 ist größer als z2")  # ... führe dieses Statement aus
elif z1 < z2:
	print("z1 ist kleiner als z2")
else:  # ... ansonsten ...
	print("z1 ist gleich z2")  # ... führe dieses Statement aus

################################################################

# Vergleichsoperatoren
# ==, != oder <>
# <, >=
# >, <=

# Logische Operatoren
# and, or -> Bedingungen verknüpfen
# not -> Bedingung invertieren
# is, in
# is: Typprüfung
# in: Prüft, ob ein Wert in einer Liste enthalten ist

# and, or benötigen immer zwei Bedingungen
# and: Gibt True zurück, wenn beide Teile True sind
if z1 > z2 and z1 > 5:
	print("Beide gültig")

# or: Gibt True zurück, wenn mindestens eine oder beide Bedingungen True zurückgeben
if z1 > z2 or z1 > 5:
	print("z1 größer z2 und/oder z1 größer 5")

# not: Bedingungen umkehren
# Macht aus True False, und aus False True
if not (z1 > z2 or z1 > 5):  # Prüfe die Klammer -> invertiere die Klammer
	print("z1 größer z2 und/oder z1 größer 5")

# in: Prüft, ob ein Wert in einer Liste enthalten ist
if z1 in [1, 2, 3, 4, 5]:  # Ist z1 zw. 1 und 5?
	print("z1 ist 1 bis 5")

if z1 in range(10):
	print("z1 ist in einem Bereich von 0 bis 9")

if "e" in "Hallo Welt":  # Hat Hallo Welt ein e?
	print("Hallo Welt hat ein e")

if z1 not in range(10):  # Ist z1 nicht zw. 0 und 9?
	print("z1 kleiner als 0 oder größer als 9")

################################################################

# Ternary-Operator
# Ermöglicht, If/Elif/Else Bäume als Einzeiler darzustellen

if z1 > z2:
	print("z1 ist größer als z2")
elif z1 < z2:
	print("z1 ist kleiner als z2")
else:
	print("z1 ist gleich z2")

# Möglichkeit 1:
print("z1 ist größer als z2") if z1 > z2 \
else \
print("z1 ist kleiner als z2") if z1 < z2 \
else \
print("z1 ist gleich z2")

# Möglichkeit 2:
print("z1 ist größer als z2" if z1 > z2 else "z1 ist kleiner als z2" if z1 < z2 else "z1 ist gleich z2")

test = 3.1
print("test ist " + ("" if test % 1 != 0 else "k") + "eine Kommazahl")

if test % 1 != 0:
	print("test ist eine Kommazahl")
else:
	print("test ist keine Kommazahl")