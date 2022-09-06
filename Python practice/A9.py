#
# name: Phillip Ahlers 
# created:  6.9.2022
# class: ETS2021
# used external libaries:
# 
# ----------------------------------------
#
# Aufgabe: Schreiben Sie eine Funktion, die den Median berechnet.

def median(values:list[int]) -> float:
    values.sort()
    num = len(values)
    if num % 2 == 0:
        # even number of items
        r = (values[num//2-1] + values[num//2])/2
        return r
    else:
        # odd number of items
        return float(values[num//2])

print(median([1, 2, 3, 4]))