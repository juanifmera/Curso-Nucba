#1
#nombre_usuario = input("Por favor, ingrese su nombre: ")
#numero_entero = int(input("Ingrese un número entero: "))
#nombre_repetido = nombre_usuario + "\n"
#resultado = nombre_repetido * numero_entero
#print(resultado)

#2
#usuario = input("Cual es tu nombre? ")
#resultado1 = usuario.upper()
#resultado2 = usuario.lower()
#resultado3 = usuario.title()
#print(resultado1)
#print(resultado2)
#print(resultado3)

#3
#usuario = input("Cual es tu nombre? ")
#longitud_nombre = len(usuario)
#print(f"Hola {usuario}, su nombre tiene {longitud_nombre} letras")

#4
#numero_de_telefono_completo = input("Por favor introduzca su numero de telefono con el siguiente formato (prefijo-numero-extension) ")
#numero_de_telefono_seleccionado = numero_de_telefono_completo.split("-")
#numero_de_telefono_final = numero_de_telefono_seleccionado[1]
#print(f"Su numero de telefono celular es {numero_de_telefono_final}")

#5
#frase = input("Por favor, introduzca una frase: ")
#frase_invertida = frase[::-1]
#print("Frase invertida:", frase_invertida)

#6
#frase = input("Introduce una frase: ")
#vocal = input("Introduci una vocal: ")
#frase_modificada = frase.replace(vocal.lower(),vocal.upper())
#print(frase_modificada)

#7
#correo = input("Cual es su correo electronico? ")
#correo_modificado = correo.split("@")
#correo_nuevo = correo_modificado[0] + "@ceu.es."
#print(f"Su nuevo correo electronico es: {correo_nuevo}")

#8
#precio_entero = input("Introduzca un precio en Euros, por favor, que contenga dos decimales: ")
#euros = precio_entero[:precio_entero.find(".")]
#centimos = precio_entero[precio_entero.find(".")+1:]
#print(f"Usted deberá pagar por el producto {euros} euros, con {centimos} céntimos.")

#9
#echa_cumple = input("Cual es su fecha de nacimiento? Introduzca su respiesta en formato dd/mm/yyyy ")
#dia = fecha_cumple[:2]
#mes = fecha_cumple[3:5]
#año = fecha_cumple[6:10]
#print(f"Su dia de cumpleaños es {dia}, su mes {mes}, y el año, {año}")

#10
#lista_de_compras = input("Que le gustaria agregar al carrito de compras? Porfavor agregar cada producto separado por una coma ")
#lista_separada = lista_de_compras.split(",")
#   print(lista_de_compras.strip())

#11
#nombre_producto = input("Ingrese el nombre del producto: ")
#precio_unitario = float(input("Ingrese el precio unitario del producto: "))
#numero_unidades = int(input("Ingrese el número de unidades: "))
#coste_total = precio_unitario * numero_unidades
#adena_salida = f"Nombre del producto: {nombre_producto}\n"
#cadena_salida += f"Precio unitario: {precio_unitario:.2f}\n"
#cadena_salida += f"Número de unidades: {numero_unidades:03d}\n"
#adena_salida += f"Coste total: {coste_total:.2f}\n"
#print(cadena_salida)



