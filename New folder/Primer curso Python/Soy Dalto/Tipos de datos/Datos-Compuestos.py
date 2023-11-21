#Lista --> Se puede modificar
Juan_Capo = ["Lucas", "Soy Dalto", True, 1.85]
print(Juan_Capo[0])


#Tupla --> No se puede modificar
tupla = ["Lucas", "Soy Dalto", True, 1.85]
print(tupla[1])

# Set --> EN un conjuto no hay duplicados pero no se puede acceder por un indice
tupla = {"Pedro", "Juan", "Soy Dalto", True, 1.85}
print(tupla)

#Dioccionario
diccionario = {
    "Nombre" : "Juan Mera",
    "Canal" : "Soy Dalto",
    "Altura" : 1.85,
    "Apellido" : "Francisco Mera"
    }
print(diccionario["Canal"])
