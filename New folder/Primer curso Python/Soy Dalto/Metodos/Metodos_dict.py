diccionario = {
    "nombre" : "Juan",
    "apellido" : "Mera",
    "edad" : 21,
}
#Nos devuelve un objeto dict_item
claves = diccionario.keys()

#Obteniendo un elemento con get() ( si no encuentra un objeto el programa continua)
claves = diccionario.get("edad")

#Elimiando todo del diccionario
#diccionario.clear()
#diccionario.pop("apellido")

#Obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario)


