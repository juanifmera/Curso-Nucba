#Creando una funcion simple
def saludar():
    print("Hola Juan como estas?")

#Ejecutando la funcion simple
saludar()

#Creando una funcion que tenga parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "Titan"
    else:
        adjetivo = "amor"
    print(f"Hola {nombre}, mi {adjetivo}, como estas?")

saludar("Camila","Mujer")
saludar("Juan", "Hombre")
saludar("Fran", "No binario")

#Creando una funcion que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3= num -5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num_entero*2}"
    print(contraseña)
    return(contraseña)

password = crear_contraseña_random(1)
frase = f"Tu contraseña nueva es {password}"
print(frase)