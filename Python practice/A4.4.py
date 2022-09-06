#
# name: Phillip Ahlers 
# created:  30.8.2022
# class: ETS2021
# used external libaries:
# 
# ----------------------------------------
# Aufgabe: 
# Drehen Sie eine festgelegte Liste um

list1 = [0, 1, 2, 3, 4, 5]
out = []

list1.reverse()

for i in range(len(list1)):
    out.append(list1[len(list1)-i-1])

print(out)