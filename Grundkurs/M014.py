# Decorator
# Code an eine beliebige Funktion anhängen (davor/danach), ohne die Funktion selbst zu verändern
import time

def halloWelt():
	print("Hallo Welt")

halloWelt()

# Eigener Decorator
# Aufgabe: Zeitmesser
def measureTime(func):  # func ist die Funktion, an dem der Decorator später angehängt wird
	def wrapper():
		# Beginn der Zeitmessung
		start = time.time()

		# Dekorierte Funktion ausführen
		func()

		# Ende der Zeitmessung
		ende = time.time()
		print(f"Zeit: {(ende - start)}s")
	return wrapper

# Decorator anhängen mit @<DecoratorName>
@measureTime
def longFunc():
	list(range(50_000))

longFunc()

#################################

# Decorator mit Parameter
def measureTimeParam(func):  # func ist die Funktion, an dem der Decorator später angehängt wird
	def wrapper(*args, **kwargs):
		# Beginn der Zeitmessung
		start = time.time()

		# Dekorierte Funktion ausführen
		func(*args, **kwargs)

		# Ende der Zeitmessung
		ende = time.time()
		print(f"Zeit: {(ende - start)}s")
	return wrapper

@measureTimeParam
def longFuncAmount(limit):
	list(range(limit))
	
longFuncAmount(1_000_000)