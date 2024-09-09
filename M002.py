# Kommentare
# Werden mit einer Raute (#) am Anfang der Zeile definiert
# Alles was nach der # kommt, wird nicht ausgeführt

################################################################

# Variablen
# Behälter für Werte
# Definition: <Name> = <Wert>

x = 5  # Nach Zeile 11 kann der Wert aus x herausgelesen werden
print(x)  # print(...): Gibt den Inhalt innerhalb der Klammern in der Konsole aus

# Typen
# In Python gibt es 5 Typen: int, float, str, bool, complex
# Der Inhalt einer Variable gibt den Typen der Variable vor

# int: Ganze Zahl
# Generell hat ein Int-Datentyp eine fixe Größe (z.B. 1B, 2B, 4B, 8B, ...)
# In Python kann ein Int beliebig groß sein
y = 289568329659710238597123759421943  # Typ: int
print(y)
print(type(y))  # Typ von y

# float: Kommazahl
# Beliebig groß/klein wie int
y = 2.5  # Kommazahlen werden immer mit einem Punkt dargestellt
print(type(y))  # Typ von y

# complex: Komplexe Zahlen
z = 12 + 5j  # j = i
print(type(z))

# str: String, Text
# Kann beliebigen Text enthalten (beliebige Länge + UTF-8)
# Kann mit doppelten oder einzelnen Hochkomma umgeben sein
a = "Hallo"
b = 'Welt'
print(a)
print(b)

# bool: Wahr-/Falschwert
# Kann nur True oder False enthalten
c = True
d = False

################################################################

# Der Punkt Operator
# Greife in die Variable und sag dem Inhalt, das er die folgende Funktion ausführen soll
komma = 83295.3258
print(komma.hex())  # Liebe Kommazahl, stelle dich selbst als Hexadezimalzahl dar

# Stringfunktionen
text = " Das ist ein Text"
text.upper()  # GANZER TEXT GROß
text.lower()  # ganzer text klein
print(text)  # Originaler Text???????????

# Funktionen geben generell eine Kopie zurück
print(text.upper())
print(text.lower())

text.isnumeric()
text.isalpha()
text.isalnum()

print(text.capitalize())  # Erstes Zeichen groß, Rest klein
print(text.title())  # Alle Anfangsbuchstaben groß, Rest klein

print(text.strip(" "))
print(text.lstrip(" "))  # Nur links
print(text.rstrip(" "))  # Nur rechts

print(text.split(" "))  # Teilt den Text in einzelne Elemente anhand des Trennzeichens auf

################################################################

# Index
# Gibt uns die Möglichkeit, von Listen einzelne Elemente zu nehmen
# Strings sind auch Listen (Ein String ist eine Liste von einzelnen Zeichen)
# Index fängt immer bei 0 an
print(text[5])
# i, weil:
#  Das ist ein Text
# 0123456789...

print(text[1])  # D

# Index von der anderen Seite
print(text[-1])  # t

# Bereich auswählen
# WICHTIG: Obergrenze ist nicht inkludiert
print(text[1:4])  # Das

print(text[-4:-1])  # Tex
print(text[-4:0])  # Nichts
print(text[-4:])  # Wenn eine Grenze nicht angegeben wird, wird der Rest genommen  (-4 bis 0)
print(text[:5])  # 0 bis 5

print(text[:])

################################################################

# Arithmetik
# Arithmetik mit Zahlen
z1 = 8
z2 = 3

z1 + z2  # Warning: Statement seems to have no effect
# Bei z1 + z2 wird nur eine Summe berechnet, diese Summe muss weiterverwendet werden
# z.B.: Variable, print(...), ...
summe = z1 + z2

z1 += z2  # Berechne die Summe, und schreibe diese in z1 hinein
# Hier müssen keine weiteren Schritte durchgeführt werden

print(z1 - z2)
print(z1 * z2)
print(z1 / z2)  # 11 / 3 = 3.6666

# In anderen Sprachen kommt bei einer Division mit zwei Integern auch wieder ein Integer heraus
# 11 / 3 = 3
# In Python gibt es dafür einen zusätzlichen Operator: //
print(z1 // z2)  # Hier werden immer die Kommastellen abgeschnitten: 11 / 3 = 3

# Modulo (%)
# Gibt den Rest einer Division zurück
print(z1 % z2)  # 11 % 3 = 2
# 11 / 3 = 3
#  2R.

# 16 % 5
# 16 / 5 = 3
#  1R.

# Potenz
# **
print(3 ** 5)  # 3^5 = 243
print(9 ** 0.5)  # sqrt(9) = 3
print(9 ** -1)  # 1/9 = 0.11111

# Arithmetik mit Strings
h = "Hallo"
w = "Welt"
h += " " + w
print(h)

print(h * 20)  # Hallo WeltHallo WeltHallo WeltHallo WeltHallo WeltHallo WeltHallo WeltHallo WeltHallo WeltHallo WeltHallo WeltHallo WeltHallo WeltHallo WeltHallo WeltHallo WeltHallo WeltHallo WeltHallo WeltHallo Welt

# Länge eines beliebigen Objekten, welches eine Länge hat
print(len(h))  # 10
print(len([1, 2, 3]))  # 3