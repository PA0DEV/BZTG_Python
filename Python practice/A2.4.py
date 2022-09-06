#
# name: Phillip Ahlers 
# created:  30.8.2022
# class: ETS2021
# used external libaries:
# 
# ----------------------------------------
# Aufgabe
# Lassen Sie den Benutzer Temperatur (warm, kalt) und Wetter eingeben (regnerisch,
# verschneit, sonnig) und geben Sie ihm einen Vorschlag zurück, wie er sich dem Wetter¨
# entsprechend kleiden soll.

validTemp = ["warm", "kalt"]
validWeather = ["regnerisch", "verschneit", "sonnig"]

while True:
    inpTemp = input("Wie ist die Temperatur?")
    if inpTemp in validTemp:
        inpWeather = input("Wie ist das Wetter?")

        if inpWeather in validWeather:
            if inpWeather == "warm" and inpWeather == "sonnig":
                print("Ein T-Shirt reicht heute völlig.")
            elif inpTemp == "warm" and inpWeather == "verschneit":
                print("Ich glaube das kann nicht sein.")
            elif inpTemp == "warm" and inpWeather == "regnerisch":
                print("Eine dünne Regenjacke schadet vermutlich nicht heute.")
            elif inpWeather == "kalt" and inpWeather == "sonnig":
                print("Ein Pullover schadet sicherlich nicht")
            elif inpTemp == "kalt" and inpWeather == "verschneit":
                print("Heute solltest du dich lieber dick anziehen")
            elif inpTemp == "kalt" and inpWeather == "regnerisch":
                print("Bleib drinne heute ;)")
        else:
            print(f"{inpWeather} ist keine gültige Wetterangabe.")

    else:
        print(f"{inpTemp} ist keine gültige Temperatureingabe.")
        