from statistics import mode, median, mean
import random

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
# ACLARACION: Cabe destacar que el enunciado dice "es mayor" lo cual deja el escenario donde el usuario ingresa 18 como edad.
# Por fines practicos se utiliza el ">=", ya que, se entiende que 18 años es mayoria de edad.

edad = int(input("Ingrese su edad"))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
# mensaje “Desaprobado”. 

nota = float(input("Ingrese su nota"))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
# operador de módulo (%) en Python para evaluar si un número es par o impar.

num = int(input("Ingrese un número par"))

if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
# siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

edad2 = int(input("Ingrese su edad"))

if edad2 < 12:
    print("Perteneces a la categoria Niño/a")
elif 12 <= edad2 < 18:
    print("Perteneces a la categoria Adolescente")
elif 18 <= edad2 < 30:
    print("Perteneces a la categoria Adulto/a joven")
else:
    print("Perteneces a la categoria Adulto/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
# como una lista o un string.

password = str(input("Ingrese una contraseña de entre 8 y 14 caracteres"))

if 8 <= len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números 
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el 
# siguiente: 
# from statistics import mode, median, mean 
# mi_lista = [1,2,5,5,3] 
# mean(mi_lista) 
# En la documentación oficial se puede encontrar más información sobre este paquete: 
# https://docs.python.org/es/3.8/library/statistics.html.  
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se 
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
# mediana es mayor que la moda. 
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
# la mediana es menor que la moda. 
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales. 
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
# Definir la lista numeros_aleatorios de la siguiente forma: 
# import random 
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de 
# forma aleatoria.

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"Media: {media}, Mediana: {mediana}, Moda: {moda}")

if (media > mediana > moda):
    print("Hay sesgo positivo")
elif (media < mediana < moda):
    print("Hay sesgo negativo")
elif media == mediana == moda:
    print("No hay sesgo")
else:
    print("No se determino un sesgo")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
# pantalla.

palabra = str(input("Ingrese una palabra o frase"))

if palabra[-1].lower() in "aeiou":
    palabra += "!"
    print(palabra)
else:
    print(palabra)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
# lower() y title() de Python para convertir entre mayúsculas y minúsculas. 

nombre = str(input("Ingrese su nombre"))

cambio = int(input("Elija una opción: 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro."))

if cambio == 1:
    print(nombre.upper())
elif cambio == 2:
    print(nombre.lower())
elif cambio == 3:
    print(nombre.title())
else:
    print("Seleccione una opcion correcta")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
# por pantalla: 
# ● Menor que 3: "Muy leve" (imperceptible). 
# ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
# ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
# generalmente no causa daños). 
# ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
# débiles). 
# ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Ingrese la magnitud del terremoto"))

if magnitud < 3:
    print("Muy leve")
elif 3 <= magnitud < 4:
    print("Leve")
elif 4 <= magnitud < 5:
    print("Moderado")
elif 5 <= magnitud < 6:
    print("Fuerte")
elif 6 <= magnitud < 7:
    print("Muy Fuerte")
elif 7 <= magnitud:
    print("Extremo")
else:
    print("Ingrese una magnitud correctamente")

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año 
# Periodo del año 
# Desde el 21 de diciembre hasta el 20 de 
# marzo (incluidos) 
# Estación en el 
# hemisferio norte 
# Invierno 
# Estación en el 
# hemisferio sur 
# Desde el 21 de marzo hasta el 20 de junio 
# (incluidos) 
# Desde el 21 de junio hasta el 20 de 
# septiembre (incluidos) 
# Desde el 21 de septiembre hasta el 20 de 
# diciembre (incluidos) 
# Primavera 
# Verano 
# Otoño 
# Verano 
# Otoño 
# Invierno 
# Primavera 
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("¿En qué hemisferio te encuentras? Ingresa 'N' para norte o 'S' para sur: ").upper()
mes = input("Ingresa el mes actual: ").lower()
dia = int(input("Ingresa el día del mes actual: "))

if hemisferio == "N":
    if ((mes == "diciembre" or mes == "12") and dia >= 21) or mes in ["enero", "1", "febrero", "2"] or ((mes == "marzo" or mes == "3") and dia <= 20):
        print("Estás en invierno")
    elif ((mes == "marzo" or mes == "3") and dia >= 21) or mes in ["abril", "4", "mayo", "5"] or ((mes == "junio" or mes == "6") and dia <= 20):
        print("Estás en primavera")
    elif ((mes == "junio" or mes == "6") and dia >= 21) or mes in ["julio", "7", "agosto", "8"] or ((mes == "septiembre" or mes == "9") and dia <= 20):
        print("Estás en verano")
    elif ((mes == "septiembre" or mes == "9") and dia >= 21) or mes in ["octubre", "10", "noviembre", "11"] or ((mes == "diciembre" or mes == "12") and dia <= 20):
        print("Estás en otoño")
elif hemisferio == "S":
    if ((mes == "diciembre" or mes == "12") and dia >= 21) or mes in ["enero", "1", "febrero", "2"] or ((mes == "marzo" or mes == "3") and dia <= 20):
        print("Estás en verano")
    elif ((mes == "marzo" or mes == "3") and dia >= 21) or mes in ["abril", "4", "mayo", "5"] or ((mes == "junio" or mes == "6") and dia <= 20):
        print("Estás en otoño")
    elif ((mes == "junio" or mes == "6") and dia >= 21) or mes in ["julio", "7", "agosto", "8"] or ((mes == "septiembre" or mes == "9") and dia <= 20):
        print("Estás en invierno")
    elif ((mes == "septiembre" or mes == "9") and dia >= 21) or mes in ["octubre", "10", "noviembre", "11"] or ((mes == "diciembre" or mes == "12") and dia <= 20):
        print("Estás en primavera")
else:
    print("Hemisferio no válido. Por favor, ingresa 'N' o 'S'.")