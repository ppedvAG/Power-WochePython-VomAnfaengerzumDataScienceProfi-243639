# Funktion
# Code abspeichern und wiederverwenden

# Erstellen einer Funktion mittels def
# Syntax: def <Name>(<Parameter>): <Body>

def halloWelt():
	print("Hallo")
	print("Welt")
	print("!")

# Der Code aus halloWelt() kann jetzt beliebig oft verwendet werden
halloWelt()
halloWelt()
halloWelt()

# Parameter
# Daten bei einer Funktion mitgeben
# Beispiel: print
print("Was soll ausgegeben werden?")

def hallo(name):
	print(f"Hallo {name}!")

hallo("Lukas")
hallo("Maren")

# Rückgabewerte
# Funktionen können ein Ergebnis haben, dieses kann im weiteren Verlauf verwendet werden (z.B. durch eine Variable)
# z.B. isupper(), islower(), split(...), ...
text = "Hallo Welt"
text.isupper()  # Rückgabewert bool (ist Uppercase, ist nicht Uppercase)
text.split(" ")  # Rückgabewert list[str] (String Liste, jedes Element ist ein Wort)

def quadriere(zahl):
	return zahl ** 2  # Mittels return kann ein Wert als Ergebnis zurückgegeben werden
	print()  # return beendet die Funktion; This code is unreachable

q = quadriere(20)
print(f"x^2={q}")

# Typen vorgeben bei Parametern und bei Rückgabewerten
# Generell kann in Python jeder beliebige bei Parametern angegeben werden
# Es können Empfehlungen gemacht werden, welche Typen in den entsprechenden Parameter hineingehören
def addiere(x, y):  # Empfehlungen hier sinnvoll
	print(f"{x} + {y} = {x + y}")

addiere("Hallo", "Welt")  # Sollte nicht möglich sein

def addiere2(x: int, y: int):
	print(f"{x} + {y} = {x + y}")

addiere2("Hallo", "Welt")  # Expected type 'int', got 'str' instead, funktioniert trotzdem

# Fehlerhafte Werte verhindern
def addiere3(x: int, y: int):
	if type(x) != int or type(y) != int:
		print("x oder y sind nicht numerisch")
		# raise ValueError  # Skript abstürzen lassen
		return
	print(f"{x} + {y} = {x + y}")

addiere3("X", "Y")

# Mehrere Empfehlungen angeben
def addiere4(x: int | float, y: int | float):
	print(f"{x} + {y} = {x + y}")

# Rückgabetyp angeben
# mit -> <Typ> nach der Klammer den Typen angeben
# Wird teilweise automatisch erkannt
def dividiere(x: int | float, y: int | float) -> float:
	return x / y

d = dividiere(3, 5)

################################################################

# Optionale Parameter
# -> Funktionen konfigurierbar machen
# Jeder Parameter kann einen Standardwert haben, dieser kann geändert werden
def subtrahiere(x, y, z=0):
	return x - y - z

subtrahiere(3, 4)  # z = 0 (Standardwert)
subtrahiere(3, 4, 8)  # z = 8 (Neuer Wert)

# Beispiel: pandas.read_csv
# Über die optionalen Parameter wird die Funktion konfiguriert
# pandas.read_csv(filepath_or_buffer, *, sep=_NoDefault.no_default, delimiter=None,
# header='infer', names=_NoDefault.no_default, index_col=None, usecols=None, dtype=None, engine=None,
# converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0,
# nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=_NoDefault.no_default,
# skip_blank_lines=True, parse_dates=None, infer_datetime_format=_NoDefault.no_default, keep_date_col=_NoDefault.no_default,
# date_parser=_NoDefault.no_default, date_format=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None,
# compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None,
# comment=None, encoding=None, encoding_errors='strict', dialect=None, on_bad_lines='error', delim_whitespace=_NoDefault.no_default,
# low_memory=True, memory_map=False, float_precision=None, storage_options=None, dtype_backend=_NoDefault.no_default)

# Optionale Parameter können über ihren Namen angesprochen werden
def printPerson(vorname = "", nachname = "", alter = -1, adresse = ""):
	print()

# Hier können bestimmte Parameter ausgelassen werden
printPerson(alter=20, adresse="Zuhause")
printPerson(vorname="Max", adresse="Zuhause")

################################################################

# Arbitrary Arguments
# Parameter, welcher beliebig viele Werte empfangen kann
# Wird mit *<Name> definiert
# Kann nur einmal pro Funktion existieren
# Wird intern als *args bezeichnet
def addieren(*zahlen: int | float):
	for x in zahlen:  # Innerhalb der Funktion ist der Parameter ein Tupel
		print(x)
	print(sum(zahlen))

# Beliebig viele Parameter möglich
addieren(1, 2, 3, 4, 5, 6)
addieren(3, 4, 5)
addieren(3)
addieren()

# Arbitrary Keyword Arguments
# Parameter, welcher beliebig viele BENANNTE Werte empfangen kann
# Wird mit **<Name> definiert
# Kann nur einmal pro Funktion existieren
# Wird intern als **kwargs bezeichnet
def printPersonen(**p):
	for key, value in p.items():  # Innerhalb der Funktion ist der Parameter ein Dictionary
		print(f"{key} heißt {value}")

printPersonen(P1="Max", P2="Tim", P3="Udo")

# Einzelschritte
# Parameter in ein Dictionary zusammenfügen
p = {
	"P1": "Max",
	"P2": "Tim",
	"P3": "Udo"
}

print(p.items())

for t in p.items():  # Zerlegung eines Tupels mittels Index
	print(t[0], t[1])

for k, v in p.items():  # Zerlegung eines Tupels mittels Unpacking
	print(k, v)

################################################################

# Problem: Liste bei *args einfügen
zahlen = [4, 12, 9, 7, 2]
# addieren(zahlen)  # addieren benötigt mehrere Zahlen als Parameter, hier ist eine Liste gegeben

# Lösung: Unpacking Operator
addieren(*zahlen)  # Explizit in Einzelteile zerlegen

# Unpacking mit Dictionary
# printPersonen(p)  # printPersonen benötigt mehrere BENANNTE Parameter, hier ist ein Dictionary gegeben
printPersonen(**p)