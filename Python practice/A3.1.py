#
# name: Phillip Ahlers 
# created:  30.8.2022
# class: ETS2021
# used external libaries:
# 
# ----------------------------------------
# Aufgabe:
# Lassen Sie für abgefragte Basis und Exponenten ein Ergebnis berechnen.¨
# Beispiel: 2^10 = 1024 3^4 = 81

while True:
    try:
        in1 = int(input("Basis eingeben: "))
        in2 = int(input("Exponenten eingeben: "))

        out = in1 ** in2 
        print(f"Ergebnis: {out}")
    except:
        print("Die Eingaben sind ungültig.")