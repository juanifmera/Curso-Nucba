# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al 
# usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

#divisas = {
#    'Euro':'€', 
#    'Dollar':'$', 
#    'Yen':'¥'
#    }

#pregunta = input("Cual es la moneda que desea convertir? ").capitalize()

#if pregunta in divisas:
#    simbolo = divisas[pregunta]
#    print(f"El simbolo de {pregunta} es {simbolo}")
#else:
#    print("Tu divisa no esta disponible")

#2 Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es 
# <teléfono>.

#nombre = input("Cual es su nombre? ")
#edad = int(input("Cual es su edad? "))
#direccion = input("Cual es la direccion de su casa? ")
#telefono = int(input("Cual es su numero celular? "))

#datos = {
#    "name": nombre,
#    "age": edad,
#    "direction": direccion,
#    "phone": telefono
#}

#print(f"{datos['name']} tiene {datos['age']}, vive en {datos['direction']} y su numero de telefono es {datos['phone']}.")

#3 Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, 
# un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario 
# debe mostrar un mensaje informando de ello.

#fruta = input("Cual es la fruta que usted desea comprar? ").capitalize()
#cantidad = int(input("Cuantos kilos desea comprar? "))

#datos = {
#    "Platano":1.35,
#    "Manzana":0.80,
#    "Pera":0.85,
#    "Naranja":0.70
#}

#if fruta in datos:
#    precio = datos[fruta]
#    resultado = precio * cantidad
#    print(f"Si usted desea comprar {cantidad} kilo de {fruta}, debera pagar {resultado}")
#else:
#    print("Su fruta no esat disponible")

#4 Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de 
# <mes> de aaaa donde <mes> es el nombre del mes. 

#fecha = input("¿Cuál es la fecha que desea recordar? (Por favor, dé su respuesta en formato dd/mm/yyyy): ")
#dia = int(fecha.split("/")[0])
#mes = int(fecha.split("/")[1])
#año = int(fecha.split("/")[2])

#fecha_separada = {
#    "Day": dia,
#    "Month": mes,
#    "Year": año
#}

#if dia > 31 or mes > 12:
#    print("La fecha ingresada es incorrecta.")
#else:
#   print(f"La fecha que usted desea recordar es el {fecha_separada['Day']}, del mes {fecha_separada['Month']}, del año {fecha_separada['Year']}.")

#5 Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 
# 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> 
# tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. 
# Al final debe mostrar también el número total de créditos del curso.

#asignaturas = {
#    "Matematica":6,
#    "Fisica":4,
#    "Quimica":5
#}

#creditos = asignaturas.values()

#for asignatura in asignaturas:
#    print(f"{asignatura}, tiene {asignaturas[asignatura]}")

#print(f"La suma de los creditos totales del curso son: {sum(creditos)}")

#6 Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, 
# edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse 
# el contenido del diccionario.

#datos = {}

#continuar = True

#while continuar:
#    clave = input("Cual es el dato que usted desea agregar? ")
#    valor = input(f"Coloque el valor para {clave} ")
#    datos[clave] = valor
#    print(datos)
#    continuar = input("Desea usted agregar mas informacion? (Si/No) ").lower()
#    if continuar == "No":
#        break

#7 Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio
# y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y 
# el coste total, con el siguiente formato

#cesta = {}
#precios = cesta.values()

#while True: 
#    artículo = input("Cuál es el artículo que usted desea agregar a la cesta de compras? Si usted desea terminar la lista de compras, escriba 'FIN' ").lower()
#    if artículo == "fin":
#        for artículo in cesta:
#            print(f"{artículo} : {cesta[artículo]} \n")
#        print(f"La suma total de tu lista es de {sum(precios)}")
#        break
#    precio = int(input(f"cuál es es el precio de {artículo}? "))
#    cesta[artículo] = precio

#8 Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés 
# separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras
# y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no
# está en el diccionario debe dejarla sin traducir.

#diccionario = {}

#while True:
#    palabra_español = input("Cuál es la palabra en Español que usted desea traducir al inglés? Si usted desea terminar las traducciones, escriba 'fin': ").lower()
    
#    if palabra_español == "fin":
#        frase = input("Por favor, introduzca una frase aquí: ")
#        palabras = frase.split()
        
#        for palabra in palabras:
#            palabra = palabra.lower()
#            if palabra in diccionario:
#                print(diccionario[palabra], end=" ")
#            else:
#                print(palabra, end=" ")
#        break
#    palabra_ingles = input(f"Cuál es la traducción de '{palabra_español}'? ").lower()
#    diccionario[palabra_español] = palabra_ingles

#9 Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario 
# donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario 
# si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número 
# de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará 
# del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad 
# pendiente de cobro.

#facturas_existentes = {}
#facturas_pagadas = {}

#while True:
#    pregunta = input("Por favor, indique qué operación desea realizar con su factura. Escriba 'nueva' para agregar una factura, 'pagar' para abonar o 'fin' para terminar: ").lower()
    
#    if pregunta == "nueva":
#        numero_factura = input("¿Cuál es el número de su factura? ")
#        valor_factura = int(input("¿Cuál es el precio de su factura? "))
#        facturas_existentes[numero_factura] = valor_factura
#        total_pendiente = sum(facturas_existentes.values())
#        total_cobrado = sum(facturas_pagadas.values())
#        print(f"La suma total de sus facturas pendientes es de {total_pendiente} pesos y el total de las facturas cobradas es de {total_cobrado} pesos.")
    
#    elif pregunta == "pagar":
#        numero_factura = input("¿Cuál es su número de factura que desea pagar? ")
#        if numero_factura in facturas_existentes:
#            valor_pagar = facturas_existentes[numero_factura]
#            facturas_pagadas[numero_factura] = valor_pagar
#            del facturas_existentes[numero_factura]
#            total_pendiente = sum(facturas_existentes.values())
#            total_cobrado = sum(facturas_pagadas.values())
#            print(f"La suma total de sus facturas pendientes es de {total_pendiente} pesos y el total de las facturas cobradas es de {total_cobrado} pesos.")
#        else:
#            print("Factura no encontrada en las facturas pendientes.")
    
#    elif pregunta == "fin":
#        break
    
#    else:
#        print("Operación incorrecta")

#10 Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente 
# será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si 
# se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) 
# Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

#Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
#Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
#Preguntar por el NIF del cliente y mostrar sus datos.
#Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
#Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
#3yt el programa.            

#encabezado = "Buenos días, ¿qué operación le gustaría realizar hoy?"
#print(encabezado)
#cliente = {}

#while True:
#    pregunta_inicial = input(
#        "'1' Para añadir un cliente\n'2' Para Eliminar un cliente\n'3' Para mostrar un cliente\n'4' Para Listar todos los clientes\n'5' Para listar clientes Preferentes\n'6' Para Terminar\n"
#    )

#    if pregunta_inicial == "1":
#        nif = input("Cual es el NIF de su cliente? ")
#        nombre = input("Cual es el nombre de su cliente? ")
#        direccion = input("Cual es la dirección de su cliente? ")
#       telefono = input("Cual es el número de teléfono de su cliente? ")
#        correo = input("Cual es el correo de su cliente? ")
#        preferente = input("Es su cliente preferente? (si/no) ").lower()

#        if preferente == "si":
#            preferente = True
#        elif preferente == "no":
#            preferente = False
#        else:
#            print("Dato Incorrecto.")

#        datos = {
#            "name": nombre,
#            "direction": direccion,
#            "phone": telefono,
#            "mail": correo,
#           "pref": preferente,
#        }
#
#        cliente[nif] = datos
#        print("Cliente añadido correctamente.")
#   
#    elif pregunta_inicial == "2":
#        eliminar = input("Cual es el NIF del cliente que desea eliminar? ")
#        if eliminar in cliente:
#            del cliente[eliminar]
#            print(f"Cliente con NIF: {eliminar} eliminado exitosamente.")
#        else:
#            print(f"No se encontró el cliente con NIF: {eliminar}")
#    
#    elif pregunta_inicial == "3":
#        busqueda = input("Cual es el NIF del cliente que quiere buscar? ")
#        if busqueda in cliente:
#            print(f"Se muestra la información del cliente con NIF: {busqueda} a continuación:")
#            print(cliente[busqueda])
#        else:
#            print(f"El cliente con NIF {busqueda} no fue encontrado en el sistema")
#            
#    elif pregunta_inicial == "4":
#        print("Se muestra una lista de todos los clientes a continuación:")
#        for nif, datos in cliente.items():
#            print(f"NIF: {nif}, Nombre: {datos['name']}")
#    
#    elif pregunta_inicial == "5":
#       preferentes = [nif for nif, datos in cliente.items() if datos["pref"]]
#        if preferentes:
#            print("A continuación se muestra la lista de clientes Preferentes:")
#            for nif in preferentes:
#                print(f"NIF: {nif}, Nombre: {cliente[nif]['name']}")
#        else:
#            print("No hay clientes Preferentes")
#    
#    elif pregunta_inicial == "6":
#        print("Gracias por utilizar este programa. Hasta luego.")
#        break  # Exit the loop
#    else:
#        print("Opción no válida. Por favor, seleccione una opción válida.")

#El directorio de los clientes de una empresa está organizado en una cadena de texto como la de más abajo, donde cada línea contiene la información del nombre, email, 
# teléfono, nif, y el descuento que se le aplica. Las líneas se separan con el carácter de cambio de línea \n y la primera línea contiene los nombres de los campos con 
# la información contenida en el directorio.

#Escribir un programa que genere un diccionario con la información del directorio, donde cada elemento corresponda a un cliente y tenga por clave su nif y por valor 
# otro diccionario con el resto de la información del cliente. Los diccionarios con la información de cada cliente tendrán como claves los nombres de los campos y como 
# valores la información de cada cliente correspondientes a los campos. Es decir, un diccionario como el siguiente

#directorio_texto = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

#lineas = directorio_texto.split('\n')

#campos = lineas[0].split(';')

#directorio = {}

#for linea in lineas[1:]:
#    datos = linea.split(';')
#    cliente = {}
#    for i in range(len(campos)):
#        cliente[campos[i]] = datos[i]
#    nif = datos[0]
#    directorio[nif] = cliente

#print(directorio)

    







