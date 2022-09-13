#
# name: Phillip Ahlers 
# created:  30.8.2022
# class: ETS2021
# used external libaries:
# 
# ----------------------------------------
# Aufgabe:
# Überprüfen Sie, ob ein vorher eingegebenes Jahr ein Schaltjahr ist. Dabei sind folgende Regeln
# zu beachten:
# - nicht durch 4 teilbar kein Schaltjahr
# - durch 4 teilbar Schaltjahr
# - durch 100 teilbar kein Schaltjahr
# - durch 400 teilbar Schaltjahr

inp = int(input("Zu prüfendes Jahr eingeben: "))

if (inp % 4 == 0 and inp % 100 != 0 or inp % 400 == 0):
    # Schaltjahr
    print(f"{inp} ist ein Schaltjahr.")
else:
    print(f"{inp} ist kein Schaltjahr.")
