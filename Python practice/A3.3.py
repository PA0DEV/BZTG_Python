#
# name: Phillip Ahlers 
# created:  30.8.2022
# class: ETS2021
# used external libaries:
# 
# ----------------------------------------
# Aufgabe:
# Berechnen Sie die obige Summe, in dem Sie rückwärts von n = 100000000 (10^8)
# aufsummieren. Ist das Ergebnis dasselbe?

MAX_NUM = 100000000

sumCount = 0

for i in range(MAX_NUM, 0, -1):
    sumCount += 1/(i)

print(f"Summe für {MAX_NUM} vorgänge: {sumCount}")