#
# name: Phillip Ahlers 
# created:  30.8.2022
# class: ETS2021
# used external libaries:
# 
# ----------------------------------------
# Aufgabe
# Lesen Sie zwei Zahlen ein, dividieren Sie diese und geben Sie das Ergebnis aus.4
num1 = int(input("Erste Zahl: "))
num2 = int(input("Zweite Zahl: "))

try:
    out = num1 / num2
    print("Ergebnis: ", out)
except:
    print(f"{num1} ist nicht durch {num2} teilar!!")
