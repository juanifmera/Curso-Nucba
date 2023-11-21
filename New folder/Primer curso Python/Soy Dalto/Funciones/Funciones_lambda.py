numeros = [1,2,3,4,5,6,7,8,9]

#Crar una funcion lambda para multiplicar por dos
multiplicar_por_dos = lambda x : x*2

#Es lo mismo que lo de arriba pero menos eficiente, por eso se usa lambda
#def multiplicar_por_dos (x):
    #return x*2
    
def es_par (num):
    if (num%2==1):
        return True
    
#Usando filder con una funcion comun
#numeros_pares = filter(es_par, numeros)

#Creando lo mismo pero con lambda
numeros_pares = filter(lambda numero:numero%2 == 0, numeros)
    
print(list(numeros_pares))
