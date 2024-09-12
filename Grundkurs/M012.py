# Exceptions
# Werden verursacht wenn Fehler auftreten, welche nicht generisch behandelt werden können
# Wenn ein Error nicht behandelt wird, stürzt das Skript ab

eingabe = "5"  # input("Gib eine Zahl ein: ")
# zahl = int(eingabe)
# Wenn der User keine Zahl eingibt -> ValueError

# Lösungen:
# - 1. if-Anweisung
if eingabe.isnumeric():
	zahl = int(eingabe)
else:
	print("Keine Zahl eingegeben")

# - 2. Fehlerbehandlung mittels try-except
# Wird verwendet, wenn der Fehler nicht vorhergesehen werden kann
# z.B.: Verbindungsaufbau zu externer Resource schlägt fehlt

# try: Code, welcher einen Fehler verursachen könnte
try:
	eingabe = input("Gib eine Zahl ein: ")  # KeyboardInterrupt
	zahl = int(eingabe)  # ValueError
# except: Fehlerbehandlung, falls der Fehler auftritt
except ValueError:
	print("Eingabe ist keine Zahl")
except KeyboardInterrupt:
	print("Programm beendet")
except:  # Except ohne Error behandelt alle Fehler, welche davor noch nicht behandelt wurden
	print("Anderer Fehler")

# Wird außerdem verwendet, um plattformunabhängig Fehlermeldungen auszugeben
# z.B. GUI hat keine Konsole, Webseite hat auch keine Konsole, Log-Files sind auch keine Konsole
# Mithilfe von raise können Fehler plattformunabhängig gemacht werden

# raise
# Fehler verursachen/Programm abstürzen lassen
# Zusätzlich kann bei jedem Fehler eine Nachricht mitgegeben werden
# raise ValueError("Das ist ein Test")

class Fahrzeug:
	def __init__(self, maxV: int, aktV: int):
		self.maxV = maxV
		self.aktV = aktV

	def beschleunige(self, a: int):
		if self.aktV + a > self.maxV:
			raise ValueError(f"Geschwindigkeit darf {self.maxV}km/h nicht überschreiten")
		elif self.aktV + a < 0:
			raise ValueError(f"Geschwindigkeit darf 0km/h nicht unterschreiten")
		else:
			return f"Das Fahrzeug fährt jetzt {self.aktV}km/h"
		
f = Fahrzeug(200, 0)
try:
	f.beschleunige(500)
except ValueError as e:  # Mit as <Name> kann dem Fehler ein Name gegeben werden
	print(e)
	# Hier kann jetzt aus e die Fehlermeldung entnommen werden
	# Diese kann jetzt nicht nur in print(...) sondern auch z.B. in ein Log geschrieben werden
	
	# Traceback: Fehlerbaum ausgeben, um den Fehler zurückzuverfolgen
	import traceback
	t = traceback.format_exception(e)
	with open("Log.txt", "w") as file:  # Fehlerbaum direkt in ein Log schreiben
		file.writelines(t)
else:  # else: Wird ausgeführt, wenn hier kein Fehler aufgetreten ist (kein except)
	print()
finally:  # finally: Wird immer ausgeführt, egal ob Fehler auftreten oder nicht
	print()

################################################################

# Debugging
# Code Step-by-Step durchgehen
# Für detailierte Fehlersuche

# Variables, Console
# Step Over, Step Into, Step Out
# Continue, Stop, Rerun
print()