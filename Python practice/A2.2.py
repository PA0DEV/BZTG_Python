#
# name: Phillip Ahlers 
# created:  30.8.2022
# class: ETS2021
# used external libaries:
# 
# ----------------------------------------
# Aufgabe:
# Bestimme Sie die Größte aus drei vorher eingegeben Zahlen und geben Sie diese Zahl aus.

COUNT = 3

inList = []

for i in range(COUNT):
    inList.append(int(input(f"{i+1}. Zahl eingaben: ")))

inList.sort()

print(f"Die größte Zahl ist {inList[0]}")