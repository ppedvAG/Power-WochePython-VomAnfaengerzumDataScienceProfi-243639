# In-/Output

# input()
# Stellt dem User eine Frage
# Nimmt vom Benutzer eine Eingabe bis Enter gedrückt wird

# alter = input("Gib dein Alter ein: ")  # input gibt immer einen String zurück -> Konvertierung
def jahresberechnung():
	alter = input("Gib dein Alter ein: ")
	if alter.isnumeric():
		alter = int(alter)
	else:
		raise ValueError("Keine Zahl eingegeben")
	print(f"Du bist im Jahr {2024 - alter} geboren worden vielleicht")

file = open("Test.txt", "w")
file.writelines("Hallo\n")  # Hier wird ein Buffer beschrieben
file.writelines(["Hallo\n", "Welt\n"])  # Hier wird ein Buffer beschrieben
file.flush()  # Hier wird der Buffer in das File geschrieben
file.close()  # Stream schließen

readFile = open("Test.txt", "r")
lines = readFile.readlines()
for zeile in lines:
	print(zeile)
readFile.close()

# Escape-Sequenzen
# Undruckbare Zeichen in einen String einbetten
# u.a. Zeilenumbruch, Tabulator, ...
# https://docs.microsoft.com/en-us/cpp/c-language/escape-sequences?view=msvc-170

# Wichtigste:
# \n: Zeilenumbruch
# \t: Tabulator
# \u: Beliebiges Unicode-Zeichen
escape = "\u3A0F"
print(escape)

# with-Block
# Jede externe Resource kann damit automatisch geschlossen werden -> höhere Sicherheit
with open("Test.txt", "w") as file2:
	file2.writelines("Hallo2\n")  # Hier wird ein Buffer beschrieben
	file2.writelines(["Hallo2\n", "Welt2\n"])  # Hier wird ein Buffer beschrieben
# close() und dadurch flush() automatisch

# rstring
# Ermöglicht, einen String zu definieren, welche Escape-Sequenzen ignoriert
pfad = "C:\\Users\\lk3\\source\\repos\\Python_Grundkurs_2024_09_09\\venv\\Scripts\\python.exe"
pfadR = r"C:\Users\lk3\source\repos\Python_Grundkurs_2024_09_09\venv\Scripts\python.exe"
print(pfad, pfadR)