#
# name: Phillip Ahlers 
# created:  6.9.2022
# class: ETS2021
# used external libaries:
# 
# ----------------------------------------
#
# Aufgabe: Oma Liesel braucht immer sehr lange an der Kasse, 
# um die richtigen Münzen¨ in ihrer Geldbörse zu finden. 
# Helfen Sie ihr und anderen Supermarktkunden, indem Sie:

# - einen Ablaufplan eines Programmes zeichnen (Mit Papier+Stift ;), welches Oma Liesel die
# Münzen nennt, die zusammen ihren Betrag (in Cent!)¨ bilden.
# -  ein Programm zu diesem Diagramm schreiben.
# Hinweis: Verwende Sie keine Kommazahlen.
# Beispiel: fur 1553 Cent:¨ [’2 Euro’, ’2 Euro’, ’2 Euro’, ’2 Euro’, ’2 Euro’, ’2
# Euro’, ’2 Euro’, ’1 Euro’, ’50 Cent’, ’2 Cent’, ’1 Cent’]
# Für Fortgeschrittene:¨
# – Oma Liesel bezahlt auch mit Geldscheinen.
# – Geben Sie die Münzen nicht einzeln zurück sondern ihre jeweilige Anzahl.¨

target = int(input("Betrag: "))

numCoins = {
    "20000": 0,     # 200€
    "10000": 0,     # 100€
    "5000": 0,      # 50€
    "2000": 0,      # 20€
    "1000": 0,      # 10€
    "500": 0,       # 5€
    "200": 0,       # 2€
    "100": 0,       # 1€
    "50": 0,        # 50ct
    "20": 0,        # 20ct
    "10": 0,        # 10ct
    "5": 0,         # 5ct
    "2": 0,         # 2ct
    "1":0,          # 1ct
}

numCoins["20000"] = target // 20000
target = target - (numCoins["20000"] * 20000)

numCoins["10000"] = target // 10000
target = target - (numCoins["10000"] * 10000)

numCoins["5000"] = target // 5000
target = target - (numCoins["5000"] * 5000)

numCoins["2000"] = target // 2000
target = target - (numCoins["2000"] * 2000)

numCoins["1000"] = target // 1000
target = target - (numCoins["1000"] * 1000)

numCoins["500"] = target // 500
target = target - (numCoins["500"] * 500)

numCoins["200"] = target // 200
target = target - (numCoins["200"] * 200)

numCoins["100"] = target // 100
target = target - (numCoins["100"] * 100)

numCoins["50"] = target // 50
target = target - (numCoins["50"] * 50)

numCoins["20"] = target // 20
target = target - (numCoins["20"] * 20)

numCoins["10"] = target // 10
target = target - (numCoins["10"] * 10)

numCoins["5"] = target // 5
target = target - (numCoins["5"] * 5)

numCoins["2"] = target // 2
target = target - (numCoins["2"] * 2)

numCoins["1"] = target

print(numCoins)

