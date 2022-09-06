#
# name: Phillip Ahlers 
# created:  30.8.2022
# class: ETS2021
# used external libaries:
# 
# ----------------------------------------
# Aufgabe
# Lesen Sie eine Zahl ein, ziehe Sie die Quadratwurzel und geben Sie das Ergebnis aus.
# Hinweis: Potenzgesetze 

inp = int(input("Zahl Eingeben: "))

try:
    out = inp ** 0.5
    print(f"{out} ist die Wurzel von {inp}.")
except:
    print(f"Es gibt keine Wurzel von {inp}")
