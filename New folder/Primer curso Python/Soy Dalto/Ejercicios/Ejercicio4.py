#creando una funcion que nos devuelva numeros primos entre 0 y el argumento que le pasemos
def es_primo(num):
    #Verificamos que el numero pasado no pueda dividirse por ningun numero entre 2 y ese mismo numero -1
    for i in range(2, num-1):
        #Si es divisible por alguno retornamos false y termina el bucle
        if num % i == 0:
            return False
        #Si termina el bucle, significa que no fue divisible, entonces es primo
    return True

#Creando una funcion que retorne una lista con todos los primos
def primos_hasta(num):
    #Creamos la lista
    primos = []
    for i in range(3, num + 1):
        #Verificamos si el valor es primo
        resultado = es_primo(i)
        if resultado == True:
            primos.append(i)
    #Devolvemos la lista
    return primos

#Creamos el resultado llamando a la funcion y lo mostramos
resultado = primos_hasta(98)
print(resultado)


    