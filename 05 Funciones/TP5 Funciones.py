import math

#1

def imprimir_Hola_Mundo():
    print("Hola Mundo")

#2    

def saludar_usuario(nombre):
    return f"Hola {nombre}"

#3

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Hola soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

#5

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

#6

def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

#7

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion =  a * b
    division = None
    if b != 0:
        division = a / b
    else:
        print("No se puede dividir por cero.")
    
    return (suma, resta, multiplicacion, division)

#8

def calcular_imc(peso, altura):
    if altura <= 0:
        return None
    else:
        imc = peso / (altura ** 2)
        return imc

#9

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

#10

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

#LLamadas

#1

imprimir_Hola_Mundo()

#2

nombre_ingresado = input("Por favor, ingresa tu nombre: ")

print(saludar_usuario(nombre_ingresado))

#3

nombre_ingresado = input("Por favor, ingresa tu nombre: ")
apellido_ingresado = input("Por favor, ingresa tu apellido: ")
edad_ingresada = input("Por favor, ingresa tu edad: ")
residencia_ingresada = input("Por favor, ingresa tu residencia: ")

informacion_personal(nombre_ingresado, apellido_ingresado, edad_ingresada, residencia_ingresada)

#4

try:
    radio_ingresado = float(input("Ingrese el radio"))
except ValueError:
    print("Intrada invalida. Por favor ingrese un valor valido para radio")
else:
    area = calcular_area_circulo(radio_ingresado)
    perimetro = calcular_perimetro_circulo(radio_ingresado)

    print(f"El area es: {area}")
    print(f"El perimetro es: {perimetro}")

#5

try:
    segundos_ingresados = float(input("Ingrese los segundos: "))
except ValueError:
    print("Valor invalido, ingrese un valor valido para los segundos por favor.")
if segundos_ingresados < 0:
    print("Por favor ingresar un número no negativo")
else:
    horas_calculadas = segundos_a_horas(segundos_ingresados)

    print(f"{segundos_ingresados} segundo equivalen a {horas_calculadas} horas")

#6

try:
    numero_ingresado = int(input("Por favor, ingresa un número entero"))
except ValueError:
    print("Entrada invalida. Debe ingresar un número entero")
else:
    tabla_multiplicar(numero_ingresado)

#7

try:
    num1 = float(input("Por favor, ingresa el primer número: "))
    num2 = float(input("Por favor, ingrese el segundo número: "))
except ValueError:
    print("Error, por favor, ingresa número válidos")
else:
    resultados = operaciones_basicas(num1, num2)
    suma_resultado, resta_resultado, multiplicacion_resultado, division_resultado = resultados

    print(f"Suma: {num1} + {num2} = {suma_resultado}")
    print(f"Resta: {num1} + {num2} = {resta_resultado}")
    print(f"Multiplicacion: {num1} * {num2} = {multiplicacion_resultado}")

    if division_resultado is not None:
        print(f"Division: {num1} / {num2} = {division_resultado}")
    else:
        print(f"Division: {num1} / {num2} = Indefinida (Division por cero)")

#8

try:
    peso_usuario = float(input("Por favor, ingresa tu peso en kilogramos"))
    altura_usuario = float(input("Por favor, ingresa tu altura en metros"))
except:
    print("Error, ingrese valores númericos válidos")
else:
    if peso_usuario <= 0 or altura_usuario <= 0:
        print("Error, el peso y la altura deben ser valores positivos y mayores a cero")
    else:
        imc_calculado = calcular_imc(peso_usuario, altura_usuario)
    
    if imc_calculado is not None:
        print(f"Tu IMC es: {imc_calculado}")

        if imc_calculado < 18.5:
            print("Clasificación: Bajo peso")
        elif 18.5 <= imc_calculado < 24.9:
            print("Clasificación: Peso normal")
        elif 25 <= imc_calculado < 29.9:
            print("Clasificación: Sobrepeso")
        else:
            print("Clasificación: Obesidad")
    else:
        print("No se pudo calcular el IMC debido a valores de altura inválidos.")

#9

try:
    temp_celsius_ingresada = float(input("Por favor, ingresa la temperatura en grados Celsius"))
except ValueError:
    print("Error, valor invalido, ignresa un numero valido para la temperatura")
else:
    temp_faherenheit_calculada = celsius_a_fahrenheit(temp_celsius_ingresada)

    print(f"{temp_celsius_ingresada}°C equivalen a {temp_faherenheit_calculada}")

#10

try:
    num1 = float(input("Por favor, ingresa el primero número: "))
    num2 = float(input("Por favor, ingresa el segundo número: "))
    num3 = float(input("Por favor, ingresa el tercer número: "))
except ValueError:
    print("Error, entrada invalida, ingresa por favor valores númericos validos.")
else:
    promedio_calculado = calcular_promedio(num1, num2, num3)
    print(f"El promedio de {num1}, {num2} y {num3} es: {promedio_calculado}")