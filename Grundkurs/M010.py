# Klassen
# Werden verwendet, um komplexe Datentypen darzustellen
# Beispiel:
# - int: Ganze Zahl
# - float: Kommazahl
# - string: Text
# - Person: ?

# Die Klasse stellt eines Bauplan dar, hier werden keine konkreten Werte festgelegt
# Konkrete werden erst im Objekt festgelegt

# Objekt
# Instanz einer Klasse, hat konkrete Werte
# Beispiel:
# Klasse Person: vorname: str, nachname: str, alter: int, ...
# Objekt Person: vorname: Max, nachname: Mustermann, alter: 33

# Verwendung: komplexe Daten, int, str, float, ... reichen oftmals nicht aus, um bestimmte Zustände darstellen zu können

# Person
# - Felder: vorname, nachname, alter
# - Funktionen: sprechen, bewegen
class Person:
	"""
	docstring
	
	Ermöglicht, Klassen und Funktion zu dokumentieren
	
	Wird immer unter der Klasse/Funktion geschrieben und mit \""" [Text] \""" definiert
	"""

	# __init__
	# Hier werden die Felder des Objekts definiert
	# Generell hat jede Klasse __init__
	# Wenn ein Objekt erstellt wird, wird __init__ ausgeführt
	def __init__(self, vorname: str, nachname: str, alter: int):
		# self: Das Objekt selbst
		# Wenn das Objekt erstellt wird, kann mit self auf dieses konkrete zugegriffen werden
		self.vorname = vorname
		self.nachname = nachname
		self.alter = alter

	def sprechen(self, text: str):
		# self.vorname ist der Vorname des konkreten Objekts
		print(f"{self.vorname} sagt: {text}")

	def bewegen(self, distanz: int):
		"""
		Funktion, welche der Person ermöglicht, sich zu bewegen

		:param distanz: Die Distanz in Meter
		:return: Nichts
		"""
		print(f"{self.vorname} bewegt sich um {distanz}m")

################################################################

# Objekte erstellen
# p1 = Person()
# p1.vorname = "Max"
# p1.nachname = "Mustermann"
# p1.alter = 22
# print(f"{p1.vorname} {p1.nachname} ist {p1.alter} Jahre alt")
# p1.sprechen("Hallo")
# p1.bewegen(10)

# Nach __init__ Verbesserung
p2 = Person("Max", "Nachname", 33)
print(f"{p2.vorname} {p2.nachname} ist {p2.alter} Jahre alt")
p2.sprechen("Hallo")
p2.bewegen(10)

################################################################

# Die __ Methoden
# Besondere Methoden, welche ungewöhnliches Verhalten implementieren
class Test:
	def __init__(self):
		self.x = 5

	# Equals (==)
	def __eq__(self, other):
		# if self.x == other.x:
		# 	return True
		# else:
		# 	return False
		return self.x == other.x

	# Greater Than (>)
	def __gt__(self, other):
		return self.x > other.x

	# Stringrepräsentation des Objekts
	def __str__(self):
		return f"Test object x = {self.x}"


t1 = Test()
t2 = Test()
print(t1 == t2)  # False, weil hier Speicheradressen verglichen werden und nicht die Inhalte

print(t1)  # <__main__.Test object at 0x00000289013E9D30>
print(t2)  # <__main__.Test object at 0x00000289013E9E80>

print(t1 > t2)

# Liste kann ausgegeben werden dank __str__
print([1, 2, 3])

print(t1)  # Test object x = 5

################################################################

# Neues Attribut hinzufügen/wegnehmen
# In Python können Objekte beliebig verändert werden (neue Felder/Funktion hinzugefügt/weggenommen werden)
t3 = Test()
t3.test = "Hallo"
print(t3.test)

del t3.test