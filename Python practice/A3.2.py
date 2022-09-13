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

for k in range(1, MAX_NUM + 1):
    # print(i)
    sumCount += 1/(k)
    # sumCount = sumCount + 1/(k)
print(f"Summe für {MAX_NUM} vorgänge: {sumCount}")