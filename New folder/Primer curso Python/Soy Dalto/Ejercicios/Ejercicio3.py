#Funcion para obtener al asistente y al profesor segun la edad.
def obtener_compañeros(cantidad_de_compañeros):
    
    #creando la lista con los compañeros
    compañeros = []
    
    #Ejecutando un for para pedir informacion de cada compañero
    for i in range(7):
        nombre = input("Ingrese el nombre del compañero ")
        edad = int(input("Ingrese la edad del compañero "))
        compañero = (nombre, edad)
        
        #Agregando la informacion a la lista
        compañeros.append(compañero)
        
        #ordenando de menor a mayor segun su edad
        compañeros.sort(key=lambda x:x[1])
        asistente = compañeros[0][0]
        profesor = compañeros[-1][0]
        
        #Retornamos una tupla
        return asistente,profesor

#Desempaquetamos la que nos retorna la funcion
asistente,profesor = obtener_compañeros(5)

#Mostramos el resultado
print(f"El profesor es {profesor} y su asistente es {asistente}")



