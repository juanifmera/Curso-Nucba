
frase_usuario = input("Que haces Titan, decime una frase y te diré cuánto tardaría en decirla: ")
tiempo_promedio = 0.5
cantidad_de_palabras = frase_usuario.split(" ")
total_palabras = len(cantidad_de_palabras)
tiempo_tardado_promedio = total_palabras * tiempo_promedio

if tiempo_tardado_promedio > 1:
    print("Para, flaco, tampoco te pedí un testamento.")
else:
    tiempo_tardado = len(frase_usuario) * tiempo_promedio
    tiempo_tardado_promedio = round(tiempo_tardado_promedio / 1.3, 2)
    print(f"Dalto, al hablar más rápido, tardaría {tiempo_tardado_promedio} segundos.")

