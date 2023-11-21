eleccion = input("Piedra, Papel o tijera? ")

#if eleccion == "Piedra":
    #print("Papel")
#elif eleccion == "Papel":
    #print("Tijera")
#elif eleccion =="Tijera":
    #print("Piedra")

import random

opciones = ["Piedra", "Papel", "Tijera"]

opcion_elegida = random.choice(opciones)

print(f"La opcion elegida es {opcion_elegida}")
