#Creando diccionario con dict()
diccionario = dict(nombre = "Juan", apellido = "Mera", altura = 1.83)

#Las listas no pueden ser calves
diccionario = {frozenset(["Dato1", "Dato2"])}

#Creando diccionario con fromkeys
diccionario = dict.fromkeys(["nombre", "apellido"])

print(diccionario)