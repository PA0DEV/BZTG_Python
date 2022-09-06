#
# name: Phillip Ahlers 
# created:  30.8.2022
# class: ETS2021
# used external libaries:
# 
# ----------------------------------------
# Aufgabe
# Bilden Sie folgende Summe für ein von Ihnen vorher festgelegtes n.

MAX_NUM = 100000000

sumCount = 0

for i in range(MAX_NUM + 2):
    sumCount += 1/(i+1)

print(f"Summe für {MAX_NUM} vorgänge: {sumCount}")