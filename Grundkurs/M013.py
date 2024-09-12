# Lambda

# Normale Funktion
def halloWelt():
	print("Hello World")

halloWelt()

# Hier wird ein Funktionszeiger angelegt
hw = halloWelt
hw()

# Dieser Funktionszeiger kann ausgeführt werden und/oder als Parameter bei einer anderen Funktion mitgegeben werden
hwa = lambda: print("Hello World")
hwa()

# Funktion mit Funktionszeiger
def runFunc(func):
	func()

runFunc(halloWelt)
runFunc(hw)
runFunc(hwa)

################################################################

# filter und map
# Diese beiden Funktionen benötigen eine Lambda-Expression als das Kriterium

# filter
# Filtert eine Liste nach einem Kriterium
zahlen = list(range(10))

# Aufgabe: Finde alle Zahlen welche durch 2 teilbar

# 1. Schleife
zahlenSchleife = []
for x in zahlen:
	if x % 2 == 0:
		zahlenSchleife.append(x)
print(zahlenSchleife)

# 2. LC
print([x for x in zahlen if x % 2 == 0])

# 3. filter
# Filter macht eine Schleife über die Liste und verwendet den Methodenzeiger mit jedem Element
# Wenn bei diesem Methodenzeiger True zurückkommt, wird das Element zurückgegeben
print(list(filter(lambda y: y % 2 == 0, zahlen)))

def teilbarDurch2(z: int):
	return z % 2 == 0

print(list(filter(teilbarDurch2, zahlen)))  # Filter mit dedizierter Methode statt Lambda

# map
# Wandelt jedes Element einer List in eine neue Form um

# Aufgabe: Liste mit Zahl^Zahl

# 1. Schleife
zahlenHochSelbst = []
for x in zahlen:
	zahlenHochSelbst.append(x ** x)
print(zahlenHochSelbst)

# 2. LC
print([x ** x for x in zahlen])

# 3. map
print(list(map(lambda y: y ** y, zahlen)))