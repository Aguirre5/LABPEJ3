import os
os.system("cls")

"""
2- Definir función, parámetros, retorno,
capturar un valor o varios
"""

def saludo():
    print(f"Holiwis")
    
def saludarte(nombre):
    print(f"Hol", nombre)
    
saludarte("Manzana")

def sumación(a, b):
    return a+b

suma = sumación(6+7)
print(suma)

def sumaresta(a, b):
    suma = a + b
    resta =  a - b
    return suma, resta

s, r = sumaresta(7, 6)
print (s) 
print (r)

def calculo (a,b):
    sum = a + b
    prod = a * b
    return sum, prod

x = int(input("Ingrese un número: "))
y = int(input("Ingrese otro número: "))

s, p = calculo(x, y)

print("Suma:", s)
print("Producto:", p)
