diccionario = {
    "Nombre" : "Juan",
    "Apellido" : "Mera",
    "Altura" : 1.83
}

#Recorriendo diccionario con items() para obtenerla clase y el valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es: {key} y el valor es {value}")