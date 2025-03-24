import math

#Ejercicio 1
print("Hola Mundo!")

#Ejercicio 2
nombre = input("Ingrese su nombre por favor: ")

print(f"Hola {nombre}!")

#Ejercicio 3
nombre = input("Ingrese su nombre por favor: ")
apellido = input("Ingrese su apellido por favor: ")
edad = input("Ingrese su edad por favor: ")
lugar_de_residencia = input("Ingrese su lugar de residencia por favor: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}")

#Ejercicio 4
radio = input("Ingrese el radio del circulo para calcular su area y perimetro: ")
area = math.pi * (float(radio) ** 2)
perimetro = 2 * math.pi * int(radio)

print(f"El area es {area} y el perímetro es {perimetro}")

#Ejercicio 5
segundos = input("Ingrese la cantidad de segundos para su conversión a horas: ")
horas = int(segundos) / 3600

print(f"La cantidad de horas es {horas}")

#Ejercicio 6 - Como el ejercicio no especifica que tienen que ser enteros (en otros ejercicios si lo hace) se toma el caso con los float para abarcar todo el espectro
numero = float(input("Ingrese un número para mostrar la tabla de mulplicar del mismo: "))

print (f"{numero} x 1 = {numero * 1}\n"
       f"{numero} x 2 = {numero * 2}\n"
       f"{numero} x 3 = {numero * 3}\n"
       f"{numero} x 4 = {numero * 4}\n"
       f"{numero} x 5 = {numero * 5}\n"
       f"{numero} x 6 = {numero * 6}\n"
       f"{numero} x 7 = {numero * 7}\n"
       f"{numero} x 8 = {numero * 8}\n"
       f"{numero} x 9 = {numero * 9}\n"
       f"{numero} x 10 = {numero * 10}\n")

#Ejercicio 7
num1 = int(input("Ingrese el primer número entero, distinto de cero por favor: "))
num2 = int(input("Ingrese el segundo número entero, distinto de cero por favor: "))

print(f"El resultado de sumarlos es: {num1 + num2}, de restarlos es: {num1 - num2}, de multiplicarlos es: {num1 * num2} y de dividirlos es: {num1 / num2}")

#Ejercicio 8
peso = float(input("Ingrese su peso en kg por favor: "))
altura = float(input("Ingrese su altura en metros por favor: "))
imc = peso / (altura ** 2)

print(f"Tu peso es {peso}, tu altura es {altura} y tu indice de masa corporal es {imc}")

#Ejercicio 9
temperatura_celsius = float(input("Ingrese la temperatura en grados celsius por favor: "))
temperatura_fahrenheit = (9/5) * temperatura_celsius + 32

print(f"La equivalencia en fahrenheit es: {temperatura_fahrenheit}")

#Ejercicio 10
num1 = float(input("Ingrese el primer número para calcular el promedio: "))
num2 = float(input("Ingrese el segundo número para calcular el promedio: "))
num3 = float(input("Ingrese el tercer número para calcular el promedio: "))

prom = (num1 + num2 + num3) / 3

print(f"El promedio es: {prom}")