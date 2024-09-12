# List Comprehension
# Anhand von einer Schleife eine Liste erzeugen
# Kann mit Bedingungen und Wertanpassungen versehen werden

# Aufgabenstellung: Zahlen von 1 bis 20

# Schleife
zahlen = []
for i in range(1, 21):
	zahlen.append(i)
print(zahlen)

# Mit LC
zahlenLC = [i for i in range(1, 21)]  # Schleife in die Klammer, Cursor an den Anfang setzen, i hinzufügen
print(zahlenLC)

# if-Anweisungen
# Aufgabenstellung: Liste mit Zahlen die durch 3 oder 5 teilbar sind

# Schleife
zahlen3oder5 = []
for i in range(1, 100):
	if i % 3 == 0 or i % 5 == 0:
		zahlen3oder5.append(i)
print(zahlen3oder5)

# Mit LC
zahlen3oder5LC = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(zahlen3oder5LC)

# Wert verändern vor dem Hinzufügen
# Aufgabenstellung: Alle Zahlen hoch 2 hinzufügen

# Schleife
zahlenHoch2 = []
for i in range(1, 100):
	zahlenHoch2.append(i ** 2)
print(zahlenHoch2)

# Mit LC
zahlenHoch2LC = [i ** 2 for i in range(1, 100)]
print(zahlenHoch2LC)

# Zahlen hoch 2 aus M005
for i in range(1, 11):
	print(f"Die Zahl ist: {i}")
	print(f"Die Zahl ist hoch 2: {i ** 2}")
	print(f"{i}^2={i ** 2}")

print([(f"Die Zahl ist: {i}", f"Die Zahl ist hoch 2: {i ** 2}", f"{i}^2={i ** 2}") for i in range(1, 11)])

# Verschachtelte Schleifen
# Aufgabenstellung: 1x1

# Schleife
for x in range(1, 11):
	for y in range(1, 11):
		print(f"{x} x {y} = {x * y}")

# Mit LC
einMalEins = [f"{x} x {y} = {x * y}" for x in range(1, 11) for y in range(1, 11)]
print(einMalEins)

# Ternary Operator
# Aufgabenstellung: FizzBuzz

# Mit Schleife
for i in range(1, 101):
	if i % 3 == 0 and i % 5 == 0:
		print("FizzBuzz")
	elif i % 3 == 0:
		print("Fizz")
	elif i % 5 == 0:
		print("Buzz")
	else:
		print(i)

# Mit LC
fizzBuzz = ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(1, 101)]
print(fizzBuzz)