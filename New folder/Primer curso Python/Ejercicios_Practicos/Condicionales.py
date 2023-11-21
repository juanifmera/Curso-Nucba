#1
#edad_usuario = int(input("Cuantos años tenes? "))
#if edad_usuario >= 18:
#    print("Sos mayor de edad")
#else:
#    print("Sos un o una pendejita de meirda")

#2
#Var_contraseña = "contraseña" 
#contraseña_usuario = input("Cual es su contraseña deseada? ").lower()
#if Var_contraseña == contraseña_usuario:
#    print("lograste entrar al programa")
#else:
#    print("Toca de aca mostro")

#3
#numero_usuario1 = int(input("Dame un Numero porfavor "))
#numero_usuario2 = int(input("Dame un numero")) 
#if numero_usuario2 == 0:
#    print("utiliza otro denominador")
#else:
#    division = numero_usuario1/numero_usuario2
#    print(f"Tu resultado es {division}")
        
#4
#numero = int(input("Porfavor entregar un numero entero "))
#verificacion = numero % 2
#if verificacion != 0:
#    print("El numero ingresado es impar")
#else:
#    print("El numero ingresado es par")

#5
#edad_usuario = int(input("Porfavor introducir su edad aqui: "))
#salario_usuario = float(input("Porfavor introoducir su salario mensual aqui: "))
#if edad_usuario > 16 and salario_usuario >= 1000:
#    print("Usted debe tributar el impuesto correspondiente")
#else:
#    print("Usted no debe tributar")

#6
#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
#El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un 
#nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al 
#usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

#nombre_usuario = input("Por favor introduzca su nombre aquí: ")
#sexo_usuario = input("Por favor introduzca su sexo aquí (Mujer/Hombre): ").title()
#letra_inicial = nombre_usuario[0].lower()

#ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
#DEF = ['n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#if (sexo_usuario == "Mujer" and letra_inicial in ABC) or (sexo_usuario == "Hombre" and letra_inicial in DEF):
#    print("Perteneces al Grupo A")
#else:
#    print("Eres del Grupo B")

#7

#renta_usuario = float(input("Porfavor introduzca su renta anual para determinar el impuesto correspondiente: "))

#if renta_usuario < 10000:
#    print("Su impuesto es del 5%")
#elif renta_usuario >= 10000 and renta_usuario < 20000:
#    print("Su impuesto es del 15%")
#elif renta_usuario >= 20000 and renta_usuario < 35000:
#    print("Su impuesto es del 20%")
#elif renta_usuario >= 35000 and renta_usuario < 60000:
#    print("Su impuesto es del 30%")
#elif renta_usuario >=60000:
#    print("Su impuesto es del 45%")

#8
#nivel_usuario = float(input("Introduzca su puntuación de empleado (0.0 / 0.4 / 0.6 o más): "))
#bono = nivel_usuario * 2400

#if nivel_usuario == 0:
#    print("Usted es mediocre y no le corresponde ningún tipo de bono")
#elif nivel_usuario == 0.4:
#    print(f"Usted es un empleado aceptable y su bono es de ${bono}")
#elif nivel_usuario >= 0.6:
#    print(f"Usted es un empleado meritorio y su bono es de ${bono}")
#else:
#    print("Puntuación no válida. Debe ser 0.0, 0.4 o 0.6 o más.")

#9
#edad_usuario = int(input("Cual es su edad? "))
#if edad_usuario < 4:
#    print("Su entrada es Gratuita")
#elif edad_usuario >= 4 and edad_usuario < 18:
#    print("Su estada cuesta 5 Euros")
#elif edad_usuario >= 18:
#    print("Su estrada cuesta 10 Euros")

#10
#eleccion = input("¿Qué tipo de pizza quiere usted? (Vegetariana / No vegetariana): ").lower()
#opciones_veg = ["pimiento", "tofu"]
#opciones_car = ["peperoni", "jamon", "salmon"]

#if eleccion == "vegetariana":
#    veg1 = input("Por favor, elija su ingrediente a continuación (pimiento o tofu): ").lower()
#    if veg1 in opciones_veg:
#        print(f"Gracias por su elección. Tu pizza tendrá entonces mozzarella, tomate y {veg1}.")
#    else:
#        print("Opción incorrecta.")
#elif eleccion == "no vegetariana":
#    noveg1 = input("Por favor, elija uno de los siguientes ingredientes (peperoni, jamon o salmon): ").lower()
#    if noveg1 in opciones_car:
#        print(f"Gracias por su elección. Tu pizza tendrá entonces mozzarella, tomate y {noveg1}.")
#    else:
#        print("Opción incorrecta.")
#else:
#    print("Elija una opción correcta: vegetariana o no vegetariana.")