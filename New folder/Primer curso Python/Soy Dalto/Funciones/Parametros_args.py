#Forma no optima de sumar valores
#def suma(lista):
#    numeros_sumados = 0
#    for numero in lista:
#        numeros_sumados = numeros_sumados + numero
#    return numeros_sumados

#resultado = suma([5,2,9])

#Forma optima utilizando el parametro args
def suma(*numeros):
    return sum(numeros)

resultado = suma(4,5,6,7)

print(resultado)

#Forma optima utilizando el parametro args con varios argumentos
def frase(nombre,apellido,adjetivo):
    return f"hola {nombre} {apellido}, sos muy {adjetivo}"

frase_resultade = frase("Juan", "Mera", "lindo")
print(frase_resultade)
