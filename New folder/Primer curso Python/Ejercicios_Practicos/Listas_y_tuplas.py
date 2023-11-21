#1
#asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
#print(asignaturas[1])

#2
#asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

#for asignatura in asignaturas:
#    print(f"Yo estudio {asignatura}")

#3

#asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
#notas = [9, 6, 4, 8, 2]

#for asignatura, nota in zip(asignaturas, notas):
#    print(f"Yo estudio {asignatura} y me saque un {nota}")

#4
#numeros_ganadores = []
#num_numeros = 6

#for i in range(num_numeros):
#    numero = int(input(f"Ingrese el número ganador {i + 1}: "))
#    numeros_ganadores.append(numero)

#numeros_ganadores.sort()

#print("Números ganadores ordenados de menor a mayor:")
#for numero in numeros_ganadores:
#    print(numero, end=", ")

#5 Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
#numeros = list(range(1,11))
#num_ord = []

#for numero in numeros[::-1]:
#    num_ord.append(numero)
#print(num_ord)

#6

#asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
#asignaturas_desaprobadas = []

#for asignatura in asignaturas:
#    nota = int(input(f"Que nota a sacado en {asignatura}? "))
#    if nota <= 4:
#        asignaturas_desaprobadas.append((asignatura, nota))

#if asignaturas_desaprobadas:
#    for asignatura, nota in asignaturas_desaprobadas:
#        print(f"Usted a desaprobado la materia {asignatura} con una nota de {nota}")
    
#else:
#    print("Felicidades, usted no tiene que repetir ninguna materia ")

#7 
#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#for indice in range(len(alphabet), 1, -1):
#    if indice % 3 == 0:
#        alphabet.pop(indice-1)
        
#print(alphabet)

#8
#while True:
#    palabra = input("Ingrese una palabra palíndroma: ").lower()
    
#    if palabra == palabra[::-1]:
#        print("¡Es un palíndromo!")
#        break
#    else:
#        print("No es un palíndromo. Intenta de nuevo.")

#9 Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

#word = input("Introduce una palabra: ")
#vocals = ['a', 'e', 'i', 'o', 'u']
#for vocal in vocals: 
#    times = 0
#    for letter in word: 
#        if letter == vocal:
#            times += 1
#    print(f"La vocal {vocal} aparece {str(times)} veces")

#10
#lista_de_precios = [50,75,46,22,80,65,8]

#maximo = max(lista_de_precios)
#minimo = min(lista_de_precios)

#print(f"El maximo precio de la lista es {maximo} y el minimo {minimo}")

#11 Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

#v1 = [1,2,3]
#v2 = [-1,0,2]

#producto_escalar = 0

#for posicion in range(len(v1)):
#    producto_escalar += v1[posicion] * v2[posicion]

#print(f"El producto escalar de estos vectores es {producto_escalar}")

#12
#Escribir un programa que almacene las matrices en una lista y muestre por pantalla su producto.
#Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.

# Función para multiplicar dos matrices
#def multiplicar_matrices(matriz1, matriz2):
#    filas_matriz1 = len(matriz1)
#    columnas_matriz1 = len(matriz1[0])
#    filas_matriz2 = len(matriz2)
#    columnas_matriz2 = len(matriz2[0])

    # Verificar si las matrices son multiplicables
#    if columnas_matriz1 != filas_matriz2:
#        return None  # Las matrices no son multiplicables

#    # Inicializar la matriz resultante con ceros
#    resultado = []

#    for _ in range(filas_matriz1):
#        fila_resultado = []
#        for _ in range(columnas_matriz2):
#            fila_resultado.append(0)
#        resultado.append(tuple(fila_resultado))

    # Realizar la multiplicación
#    for i in range(filas_matriz1):
#        for j in range(columnas_matriz2):
#            suma = 0
#            for k in range(columnas_matriz1):
#                suma += matriz1[i][k] * matriz2[k][j]
#            fila_resultado = list(resultado[i])
#            fila_resultado[j] = suma
#            resultado[i] = tuple(fila_resultado)

#    return resultado

# Definir las matrices como listas de tuplas
#matriz1 = [(1, 2, 3), (4, 5, 6)]
#matriz2 = [(-1, 0), (0, 1), (1, 1)]

# Calcular el producto de las matrices
#producto = multiplicar_matrices(matriz1, matriz2)

# Mostrar el resultado
#if producto is not None:
#    for fila in producto:
#        print(fila)
#else:
#    print("Las matrices no son multiplicables.")


#13
#Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
#import math

# Solicitar al usuario una muestra de números separados por comas
#entrada = input("Ingrese una lista de números separados por comas: ")

# Dividir la entrada en una lista de números
#numeros = [float(numero) for numero in entrada.split(',')]

# Calcular la media
#media = sum(numeros) / len(numeros)

# Calcular la suma de los cuadrados de las diferencias con la media
#suma_cuadrados_diferencias = sum((numero - media) ** 2 for numero in numeros)

# Calcular la desviación estándar
#desviacion_estandar = math.sqrt(suma_cuadrados_diferencias / len(numeros))

# Mostrar la media y la desviación estándar
#print("La media de los números es:", media)
#print(f"La desviación estándar de los números es: {desviacion_estandar}")