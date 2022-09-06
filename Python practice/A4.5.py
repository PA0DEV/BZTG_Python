#
# name: Phillip Ahlers 
# created:  30.8.2022
# class: ETS2021
# used external libaries:
# 
# ----------------------------------------
# Aufgabe:
# Lassen Sie den Benutzer einen Satz und ein Wort eingeben. 
# Finden Sie heraus, ob das Wort im Satz vorkommt und geben Sie das 
# Ergebnis als „Wahr“ oder „Falsch“ aus.


s = input("Geben sie einen Satz ein!")
w = input("Geben sie das zu suchende Wort ein!")

if w in s:
    print(True)
else:
    print(False)