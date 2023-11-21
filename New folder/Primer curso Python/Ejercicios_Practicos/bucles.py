#1
#palabra = input("Por favor, introduzca una palabra: ")

#for i in range(10):
#    print(palabra)

#2
#edad = int(input("Cual es su edad?"))

#for i in range(edad):
#    print(f"Usted cumplio {i+1} ")

#3
#entero_positivo = int(input("Proporcione un numero entero positivo: "))

#if entero_positivo <= 0:
#    print("Por favor, proporcione un número entero positivo válido.")
#else:
#    for i in range(entero_positivo):
#        if i % 2 != 0:
#            print(f"Los numeros impares son: {i}")

#3
#x = int(input("Porfavor introduzca un numero par positivo: "))

#for i in range(x):
#    if i % 2 != 0:
#        print(i, end = ", ") 

#4
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde 
#ese número hasta cero separados por comas.

#x = int(input("Por favor, introduzca un número entero positivo: "))

#if x <= 0:
#    print("El número ingresado no es positivo.")
#else:

#    for i in range(x, -1, -1):
#        if i == 0:
#            print(i, end=".\n")
#        else:
#            print(i, end=", ")
#5
#CO = float(input("¿Cuál es el capital que desea invertir? "))
#int_rate = float(input("¿Cuál es el interés que le proporciona el banco? (Ingrese un valor decimal, por ejemplo, 0.05 para un 5%): "))
#t = int(input("¿Cuántos años desea mantener la inversión? "))

#if t <= 0:
#    print("El período de tiempo debe ser un número positivo.")
#else:
#    resultado = round(CO * ((1 + int_rate) ** t),2)

#    for i in range(1,t + 1):
#        if i == t:
#            print(f"Tu inversión después de {i} años es: {resultado}")
#        else:
#            print(f"Después de {i} años, tu inversión es: {CO}")
#            CO = round(CO * (1 + int_rate),2)

#6 
#num = int(input("Porfavor introduzca un numero entero: "))

#if num <= 0:
#    print("Un numero entero positivo porfavor")
#else:
#   for i in range(num):
#        print("*" * (i+1))

#7
#for multiplicando in range(1, 11):

#    print(f"Tabla de multiplicar del {multiplicando}:")

#    for multiplicador in range(1, 11):
#        producto = multiplicando * multiplicador
#        print(f"{multiplicando} x {multiplicador} = {producto}")
#
#    print()
#8
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1

#num = int(input("Por favor introduzca un numero entero positivo: "))

#if num <= 0:
#    print("Entero positivo como (1; 2; 3, etc)")
    
#else:
#    for i in range(1,num+1,2):
#        for j in range(i, 0, -2):
#            print(j, end=" ")
#        print("")

#9

#contraseña = "contraseña"
#contraseña_usuario = ""

#while contraseña != contraseña_usuario:
#    contraseña_usuario = input("Introduzca la contraseña: ")
    
#print("usted accedio al sitio web")

#10
#palabra = input("Coloque una palabra AQUI: ")

#for letra in palabra[::-1]:
#    print(letra)

#12
#frase = input("Por favor, introduzca una frase: ")
#letra = input("Por favor, introduzca una letra: ")
#contador = 0

#for caracter in frase:
#    if caracter.lower() == letra.lower():
#        contador += 1
#print(f"La letra '{letra}' aparece {contador} veces en la frase.")

#13
#entrada = ""

#while entrada != "salir":
#    entrada = input("Por favor, introduce un mensaje (escribe 'salir' para terminar): ")
    
#    if entrada != "salir":
#        print("Eco:", entrada)





