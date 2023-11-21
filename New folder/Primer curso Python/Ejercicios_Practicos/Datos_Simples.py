#1
#print("Hola Mundo")

#2
#texto = "Hola Mundo"
#print(texto)

#3
#usuario = input("Como es su nombre? ")
#print(f"Hola {usuario}")

#4
#print((((3+2)/(2*5)))**2)

#5
#horas_diarias = int(input(("Cuantas horas trabaja usted por dia? ")))
#costo_por_hora = int(input(("Cuanto le pagan por hora? ")))
#horas_semanales = horas_diarias * 5
#horas_mensuales = horas_semanales * 4
#ganancia_semanal = horas_semanales * costo_por_hora
#ganancia_mensual = horas_mensuales * costo_por_hora
#print(f"Usted esta cobrando {ganancia_semanal} pesos por semana y {ganancia_mensual} pesos por mes")

#6
#n = int(input("Escribe un numero entero "))
#suma = int(n * (n+1) / 2)
#print(f"La suma ed los primeros numeros enteros desde el 1 hasta {n} es {suma}")

#7
peso = float(input("Cual es su peso? "))
altura =float(input("Cuanto mide ? "))
imc = round((float(peso)/float(altura)),2)
print(f"Su indice de masa corporal es {imc}")

#8
#n = int(input("Ingrese el primer número entero (n): "))
#m = int(input("Ingrese el segundo número entero (m): "))
#cociente = n // m
#resto = n % m
#print(f"{n} dividido por {m} da un cociente de {cociente} y un resto de {resto}.")

#9
#cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
#interes_anual = float(input("Ingrese el interés porcentual anual: "))
#numero_años = int(input("Ingrese el número de años de la inversión: "))
#interes_decimal = interes_anual / 100
#capital_obtenido = round((cantidad_invertir * (1 + interes_decimal) ** numero_años),2)
#print(f"El capital obtenido en la inversión es: {capital_obtenido}")

#10
#peso_payasos = 112
#peso_muñecas = 75
#num_payasos = int(input("cuantos payasos se vendieron en el ultimo periodo? "))
#num_muñecas = int(input("Cuantas muñecas se vendieron en el ultimo periodo? "))
#peso_total = round((peso_payasos*num_payasos + peso_muñecas*num_muñecas) / 1000,2)
#print(f"El peso total del paquete es de {peso_total} kilos")

#11
#monto_inicial = float(input("Ingrese la cantidad inicial de dinero en la cuenta de ahorros: "))
#tasa_interes_anual = 0.04
#saldo_despues_del_primer_anio = monto_inicial * (1 + tasa_interes_anual)
#saldo_despues_del_segundo_anio = saldo_despues_del_primer_anio * (1 + tasa_interes_anual)
#saldo_despues_del_tercer_anio = saldo_despues_del_segundo_anio * (1 + tasa_interes_anual)
#print(f"Después del primer año, el saldo es: {saldo_despues_del_primer_anio:.2f}")
#print(f"Después del segundo año, el saldo es: {saldo_despues_del_segundo_anio:.2f}")
#print(f"Después del tercer año, el saldo es: {saldo_despues_del_tercer_anio:.2f}")

#12
cantidad_vendidas_fresco = int(input("Cuantas barras de pan fresco vendio hoy? "))
cantidad_vendidas_descuento = int(input("Cuantas barras de pan de otr dia vendio hoy? "))
cantidad_panes_totales = cantidad_vendidas_fresco + cantidad_vendidas_descuento
precio_pan_fresco = 3.49 * cantidad_vendidas_fresco
precio_pan_descuento = (3.49 - (3.49 * 0.6)) * cantidad_vendidas_descuento
factura_total = round(precio_pan_fresco + precio_pan_descuento,2)
print(f"Usted vendio en total {cantidad_panes_totales}, de los cuales {cantidad_vendidas_fresco} son frescos y los otros {cantidad_vendidas_descuento} son de otro dia. Su factura total es de {factura_total} euros")


