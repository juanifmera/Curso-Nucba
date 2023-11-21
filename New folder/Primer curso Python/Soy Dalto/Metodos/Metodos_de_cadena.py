#Estructura DATO.METODO()

cadena1 = "Hola soy Juan"
cadena2 = "Bienvenido capo"

resultado1 = cadena1.upper()
resultado2 = cadena1.lower()
resultado3 = cadena1.capitalize()
busqueda_de_hola1 = cadena1.find("Juan")
# index si no encuentra algo, lanza una excepcion
busqueda_de_hola2 = cadena1.index("Juan")
count_de_o = cadena1.count("Hola")
cuenta_de = len(cadena1)
empieza_con = cadena2.startswith("Bienvenido")
termina_con = cadena2.endswith("ca")
remplaza_por = cadena1.replace("Hola","Holus")
#Separa las cadenas
espacio = " "
cadena_separada = cadena1.split(espacio)



print(resultado1)
print(resultado2)
print(resultado3)
print(busqueda_de_hola1)
print(busqueda_de_hola1)
print(count_de_o)
print(cuenta_de)
print(empieza_con)
print(termina_con)
print(remplaza_por)
print(cadena_separada)