#
# name: Phillip Ahlers 
# created:  6.9.2022
# class: ETS2021
# used external libaries:
# 
# ----------------------------------------
#

from time import sleep
from pynput import keyboard


def getKey() -> bool:
    # with keyboard.Events() as e:
    #     while True:
    #         event = e.get()

    #         if event.key == keyboard.KeyCode.from_char("y"):
    #             return True
    #         elif event.key == keyboard.KeyCode.from_char("n"):
    #             return False
    #         else:
    #             print("press 'Y' for yes or 'N' for no!")
    #             sleep(0.5)
    while True:
        i = input("Press Y for yes or N for no.\n")
        if i == "y" or i == "Y":
            return True
        elif i == "n" or i == "N":
            return False
    

print("Is the system working?")
if getKey():
    print("Never touch a running system!")
else:
    print("Is it your fault?")
    
    if getKey():
        print("Did anyone notice?")

        if getKey():
            print("You´re fucked!")
            print("Can you blam any one else?")

            if getKey():
                print("Don´t worry someone else is fucked")
            else:
                print("Youre really fucked!")
        else:
            print("Noone is gonna know!")

    else:
        print("Its not your problem ;)")