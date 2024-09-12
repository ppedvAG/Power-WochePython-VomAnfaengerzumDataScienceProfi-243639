# Vererbung
# Oberklassen definieren, welche ihre Funktionen/Felder nach unten weitergeben
# Ermöglicht, Generalisierung von Eigenschaften

# Beispiel: Object
# - Ist die Oberklasse von allen Klassen
# - Gibt verschiedene Funktionen an alle Klassen weiter (u.a. __init__, __str__, ...)

# Beispiel: Lebewesen
# Feld: Alter
# Funktion: Bewegen
class Lebewesen:
	def __init__(self, alter: int):
		self.alter = alter

	def bewegen(self, distanz: int):
		# type(self): Der Typ den das Objekt eigentlich hat (nicht Lebewesen)
		print(f"{type(self).__name__} bewegt sich um {distanz}m")

# Unterklasse Mensch, Vererbung durch Oberklasse in Klammer erzeugen
# Mensch ist eine Spezifizierung, hat zusätzliche Eigenschaften ggü. Lebewesen
# z.B.: Name, Sprechen
class Mensch(Lebewesen):
	def __init__(self, alter: int, name: str):
		# super(): Rufe Code aus der Oberklasse auf
		# Wird hier verwendet, um eine Verkettung zw. den beiden __init__ Methoden herzustellen
		# Stellt Redundanz her, wenn eine Veränderung auftritt, wird diese von den Unterklassen "automatisch" übernommen
		super().__init__(alter)
		self.name = name

	def sprechen(self, text: str):
		print(f"{self.name} sagt: {text}")
		
		
class Katze(Lebewesen):
	pass

# Mensch hat Alter, Bewegen vererbt bekommen
m = Mensch(30, "Max")
m.bewegen(20)
m.sprechen("Hallo")

k = Katze(3)
k.bewegen(10)

# Typvergleiche
# Herausfinden, welchen Typ ein Objekt hat
if type(m) == Mensch:
	print("m ist ein Mensch")

if m is Mensch:
	print("m ist ein Mensch")