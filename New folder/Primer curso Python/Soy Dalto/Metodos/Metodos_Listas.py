#Creando una lista con list()

lista =  list(["Hola","Juan",34])

#Devuelve la cantidad de elementos a la lista
reusltado = len(lista)

#Agregando elementos a la lista
agregando_con_append = lista.append("Male amor")

#Agregando un elemento a la lista con un indice especifico
lista.insert(2,"Juan es un capo")

#Agregando varios elementos a la lista
lista.extend([False, 2023])

#Eliminando un elemento de la lista por su indice / Si pongo (-1) se elimina el ultimo, (-2) para el ante ultimo, y asi susesivamente
lista.pop(0)

#Eliminando un elemento por su valor
lista.remove("Juan es un capo")

#Eliminando todos los elementos de la lista
#lista.clear()

#Ordenando las listas de forma ascendente--> Solo para numeros y true y false. Los stings no se ordenan
#lista.sort()

#Ordenando la lista de forma invertida
#lista.sort(reverse=True)

#Invirtiendo los elementos de una lista
lista.reverse()

#Verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(2023)

print(lista)
print(elemento_encontrado)