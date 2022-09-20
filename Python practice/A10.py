#
# name: Phillip Ahlers 
# created:  6.9.2022
# class: ETS2021
# used external libaries:
# 
# ----------------------------------------
#
# Programmieren Sie eine Funktion, die einen String und eine Zahl k als Parameter entgegennimmt
# und die Caesar-Verschlüsselung zurückliefert. Bei der einfachen Verschlüsselungsverfahren wird
# jeder Buchstabe zyklisch mit dem Buchstaben ersetzt, der im Alphabet k Buchstaben weiter hinter
# steht.
# • Wie behandele ich Groß- und Kleinschreibung?
# Testen Sie ihre Funktion mit diesem Wort (und weiteren): caesar (k = 3)→ fdhvdu

def encryptCaesar(input:str, k:int) -> str:
    """
        Encrypt a string using Caesar enkryption.

        Params:
            input: The input string to encrypt
            k: the encryption key

        Return:
            returns the encrypted string
    """

    charList = [*input]
    outStr = ""
    for char in charList:
        c = ord(char)       # get the ASCII value of the char
        c += k              # increase by k
        c = chr(c)          # get the char to the ASCII value
        outStr += c         # append to out string

    return outStr



print(encryptCaesar("Caesar", 3))

def decryptCaesar(input:str, k:int) -> str:
    """
        Decrypt a string using Caesar enkryption.

        Params:
            input: The input string to decrypt
            k: the encryption key

        Return:
            returns the decrypted string
    """

    charList = [*input]
    outStr = ""
    for char in charList:
        c = ord(char)       # get the ASCII value of the char
        c -= k              # increase by k
        c = chr(c)          # get the char to the ASCII value
        outStr += c         # append to out string

    return outStr

print(decryptCaesar("Fdhvdu", 3))