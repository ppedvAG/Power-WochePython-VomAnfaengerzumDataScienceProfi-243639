# Module
# Jedes Python Skript ist ein Modul
# Jedes Python kann in anderen Skripten eingebunden werden

# WICHTIG: Wenn ein Modul importiert wird, wird es komplett ausgeführt
# Wenn Funktionen importiert werden, muss das def Statement ausgeführt werden, damit die Funktion verwendet werden kann
# -> das ganze Skript muss vollständig ausgeführt werden

# Importmöglichkeiten
# 1. Gesamter Import
# - Syntax: import <Name>
# 2. from-Import
# - Syntax: from <Name> import <Name1>, <Name2>, ...

import M007  # Zugriff auf halloWelt, hallo, quadriere, addiere, ... möglich
M007.addiere(3, 4)

# Alias
# Imports können alternative Namen gegeben werden
# Syntax: <import Statement> as <Name>

import M006 as LC
print(LC.x)

# from-Import
from M008b import test3, test5
test3()  # Prefix/Alias fällt bei from-Import weg
test5()

################################################################

# Wo werden beim Import die Skripte gesucht?
# 1. Im selben Verzeichnis
# 2. In der Python Standardbibliothek
# 3. Bei den extern installierten Paketen
# 4. Eigene Pfade
# Wenn das Modul nicht gefunden wird: ModuleNotFoundError
import sys
sys.path.append("C:\\")  # Eigenen Pfad hinzufügen

# Alle Pfade anzeigen:
for p in sys.path:
	print(p)

################################################################

# Externe Pakete installieren
# Über Python Packages
# Name eingeben -> Auswählen -> Install
# Über pip
# - pip install <Name>
# - pip uninstall <Name>
# pip aktualisieren: py -m ensurepip --upgrade

# Pakete werden in venv/Lib/site-packages installiert

# Pakete können ab jetzt importiert werden
# z.B.: import numpy as np

################################################################

# Die Main-Methode
# Der Einstiegspunkt von allen Python Skripten
# Ist generell am Ende eines Skripts platziert

# __name__
# Ist der Name des Skripts selbst, wenn es importiert wird
# Ist __main__ wenn es direkt gestartet wird
print(__name__)

def main():
	print()

if __name__ == "__main__":
	main()

################################################################

# Packages
# Ordner, welche eine bessere Strukturierung des Projekts ermöglichen

# __init__.py
# Wenn ein Ordner angegriffen wird, wird dieses Skript ausgeführt