#
# name: Phillip Ahlers 
# created:  6.9.2022
# class: ETS2021
# used external libaries:
# 
# ----------------------------------------
#
# Das gute, alte „6 aus 49“
# Aufgabe: Schreibe Sie eine Funktion lotto, welche sechs Zufallszahlen von 1 bis 49 ausgibt.
# Zum Vorgehen:
# • Wie generiert man Zufallszahlen?
# • Wie garantiert man, dass diese im gewünschten Zahlenbereich sind?
# • Wie stellt man sicher, dass jede Zahl nur ein einziges Mal gezogen wird?
# • Wie garantiert man, dass nur sechs Zahlen gezogen werden?
# • Welchen Rückgabewert hat die Funktion?¨

import random


def lotto() -> list[int]:
    """
        Run a default lotto 6 out of 49

        Returns:
            returns a list of 6 numbers
    """
    outList = []

    for i in range(6):
        num = random.randint(1, 49)
        
        while num in outList:
            num = random.randint(1, 49)
            
        outList.append(num)

    return outList

print(lotto())