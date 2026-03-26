import os
os.system("cls")

# Verificacion palíndroma.
def palindromia(text):
    normaltext = text.replace(" ", "").lower()
    return normaltext == normaltext[::-1]

text = input("Pon una frase: ")

if palindromia(text):
    print("La frase es palíndroma.")
else:
    print("La frase no es palíndroma.")
