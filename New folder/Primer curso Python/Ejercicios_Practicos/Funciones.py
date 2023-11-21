#1 Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

#def bienvenida():
#    print("Hola amiga")
#    return

#bienvenida()

#2 Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

#def saludar():
#    nombre = input("Cual es su nombre? ")
#    print(f"Hola {nombre}!. Un gusto en conocerte")
#    return

#saludar()

#3 Escribir una función que reciba un número entero positivo y devuelva su factorial.

#def funcion_factorial():
#    numero_base = int(input("Cual es el numero entero positivo que le gustaria saber su factorial? "))
#    if numero_base < 0:
#        print("Numero Incorrecto")
#        return
    
#    elif numero_base == 0:
#        print("El factorial de 0 es 1")
        
#    else:
#        factorial = 1
#        for numeros in range(1, numero_base+1):
#            factorial *= numeros
#        print(f"El vectorial se su numero {numero_base} es {factorial}")

#funcion_factorial()

#Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
# y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

