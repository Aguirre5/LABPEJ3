import os
os.system("cls")

#Cue nta pa.aabras.



def recuento(inputx):
    acum = 0
    wor = False
    
    for word in inputx:
        if word != " ":
            if not wor:
                acum += 1
                wor = True
        else:
            wor = False
        
    return acum 
    
inputx = input("Ponga una frasee:")

akum = recuento(inputx)

print(f"Cantidad de palabras: {akum}")
