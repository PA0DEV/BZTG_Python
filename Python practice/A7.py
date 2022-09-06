#
# name: Phillip Ahlers 
# created:  6.9.2022
# class: ETS2021
# used external libaries:
# 
# ----------------------------------------
#
# Aufgabe: Schreiben Sie eine Funktion, welche Dominosteine bis zu einer gewissen Grenze
# erzeugt. Die Dominosteine können z.B. so aussehen:¨
# (1|1),(1|2),(1|3),(2|2),(2|3),(3|3),...
# Es dürfen dabei jedoch keine Duplikate auftreten! Ist bspw. (1|2) schon erzeugt, darf (2|1) nicht
# nochmals erzeugt werden, usw.

def createDominos(maxValue: int) -> list:
    """
        Creates a list of Dominos (1, 1), (1, 2)

        Params:
            maxValue: the max value of a domino
        Returns:
            returns a List of Tuples of Domino bricks
    """
    outList = []
    for i in range(maxValue):
        for j in range(i):
            outList.append((i+1, j+1))
        outList.append((i+1, i+1))

    print(outList)

createDominos(6)