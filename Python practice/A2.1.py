#
# name: Phillip Ahlers 
# created:  30.8.2022
# class: ETS2021
# used external libaries:
# 
# ----------------------------------------
# Aufgabe:
# Programmieren Sie die Eingabe von zwei Zahlen, sortiere Sie diese nach ihrer Größe und
# geben Sie das Ergebnis in der richtigen Reihenfolge aus.

COUNT = 2

inList = []

for i in range(COUNT):
    inList.append(int(input(f"{i+1}. Zahl eingaben: ")))

inList.sort()

for entry in inList:
    print(entry)
