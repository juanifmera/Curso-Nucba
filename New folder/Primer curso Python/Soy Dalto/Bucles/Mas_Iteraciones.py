
frutas = ["banana", "manzana", "ciruela","pera", "naranja", "granada", "durazno"]
cadena = "Hola Juan"
numeros = [2, 5, 7]

#Evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == "granada":
        continue
    print(f"Me voy a comer {fruta}")

#Evitar que el bucle siga ejecutandose
for fruta in frutas:
    print(f"Me voy a comer una {fruta}")
    if fruta == "pera":
        break
else:
    print("Terminado")
    
#Recoriendo una cadena de texto

for letra in cadena:
    print(letra)

#For en una sola linea de codigos
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
