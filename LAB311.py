import os
os.system("cls")

"""
1. Define una lista de diccionarios que 
represente información personal.
nombre,edad. Luego, accede a
elementos específicos de la lista, 
como el primer diccionario, el nombre 
de la primera persona y la edad de la 
segunda persona, para finalmente imprimir
los resultados en la consola.
2. Usar valores k y v.

"""
# Diccionario: {} estructura de datos que almacena info. en pares de clave-valor, permitiendo
# el acceso a cada valor usando la clave.
# En si, sirve para almacenar datos asociados a una clave.
people = [ 
    
    { "nombre": "Cylia", "edad": 16 },
    { "nombre": "Kilye", "edad": 43},
    {"nombre": "Maggie", "edad": 2}
    
]

diccionario = people[0]
n1erperson = people[0]["nombre"]
e2ndperson = people[1]["edad"]
n3erperson = people[2]["nombre"]

print(diccionario)
print(n1erperson)
print(e2ndperson)
print(n3erperson)

print("")
for person in people:
    for k, v in person.items():
        print(k, ":" ,v)
