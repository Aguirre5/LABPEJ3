import os
os.system("cls")

"""
    
    Crear programa que permita
al usuario agregar tareas con descripción, 
fecha límite y prioridad, así como mostrar 
la lista de tareas. 
Este menú se repite hasta que el usuario elige salir."
    
    """
    
# [ ] { } 

tareas = []

def alttarea(): 
    desc = input("Ingresa la pormenorización descriptiva de tu tarea: ")
    date = input("Ponga la fecha de entrega, (año - mes - día): ")
    prior = input("Pon la prioridad, (Alta, media o baja): ")
    
    tarea = {
        
        "descripción": desc,
        "fecha": date,
        "prioridad": prior
    }
    
    tareas.append(tarea)
    print("Tarea agregada con éxito.")
    print("")
    
def showtareas():
    if not tareas:
        print("No hay tareas cargadas.")
        print("")
        return
    
    print("\nLista de tareas: ")
    for i, tarea in enumerate(tareas, start = 1):
        print(f"{i}. {tarea['descripcion']} | Fecha: {tarea['fecha']} | Prioridad: {tarea['prioridad']}")
    print()
    
def Opciones():
    while True:
        print("=== MENÚ ===")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            alttarea()
        elif opcion == "2":
            showtareas()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente nuevamente.\n")

Opciones()
