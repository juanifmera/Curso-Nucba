
animales = ["gato","perro","loro","cocodrilo"]
numeros = [10,15,78,986]

#Recorriendo lista animales
for animal in animales:
    print(f"Ahora la variable es igual a: {animal}")

#Recorriendo lista con numeros
for numero in numeros:
    resultado = numero * 10
    print(resultado)

#Iterando dos listas del mismo tamaño al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f"Recorriendo lista 1: {numero}")
    print(f"Recorriendo lista 2: {animal}")

#Forma no optima de recorer una lista con su indice (No funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])

#Forma correcta de recorrer una lista
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El indice es: {indice} y el valor es: {valor}")

#Usando el for/else
for numero in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("El bucle termino")

#Todo lo anterior funciona exactamente igual para tuplas
    