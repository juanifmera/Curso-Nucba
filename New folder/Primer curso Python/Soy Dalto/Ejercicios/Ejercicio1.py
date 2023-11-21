#A
este_curso = 1.5
el_mas_rapido_de_otro_curso = 2.5
el_mas_lento_de_otro_curso = 7
promedio_de_cursos = 4

resultado_A1 = 100 - (este_curso / el_mas_rapido_de_otro_curso * 100)
resultado_A2 = 100 - (este_curso * 1000 // el_mas_lento_de_otro_curso / 10)
resultado_A3 = 100 - (este_curso / promedio_de_cursos * 100)

print(resultado_A1)
print(resultado_A2)
print(resultado_A3)

#B

crudo_de_este_curso = 3.5
crudo_de_otros_curso = 5

resultado_B1 = 100 - (promedio_de_cursos / crudo_de_otros_curso * 100 )
resultado_B2 = 100 - (este_curso * 1000 // crudo_de_este_curso / 10 )

print(resultado_B1)
print(resultado_B2)

#C

respuesta_final = promedio_de_cursos * 1000 // este_curso / 100
print(respuesta_final)
