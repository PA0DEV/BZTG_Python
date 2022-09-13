#
# name: Phillip Ahlers 
# created:  6.9.2022
# class: ETS2021
# used external libaries:
# 
# ----------------------------------------
#
# Ein Eisenwarenhandler bietet verschiedenste Waren zu unterschiedlichen Preisen an. Er führt
# unter anderem auch Schrauben, Muttern und Unterlegscheiben.
# Die Preise für diese Artikel sind:
# • Schrauben: 7 ct
# • Muttern: 4 ct
# • Unterlegscheiben 2 ct
# Aufgabe: Schreiben Sie eine Funktion hornbach, die für eine gegebene Anzahl Schrauben,
# Muttern und Unterlegscheiben den Endpreis berechnet. 

def calcPrice(numScrews: int, numNuts: int, numWasher: int) -> int:
    """
        Function to calculate the total price of the charge in cents
        Params:
            numScrews:  Total number of screws
            numNuts:    Total number of screw nuts
            numWasher:  Total number of washers
        Return:
            returns the total in cents
    """
    price = numScrews * 7
    price += numNuts * 4
    price += numWasher * 2

    return price
