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

for i in range(MAX_NUM):
    sumCount += 1/(MAX_NUM-i+1)

print(f"Summe für {MAX_NUM} vorgänge: {sumCount}")