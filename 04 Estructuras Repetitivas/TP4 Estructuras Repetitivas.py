import random
from statistics import mean

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for numero in range(101):
    print(numero)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene.

numero = input("Por favor, introduce un número entero: ")
cantidad_digitos = len(numero)
print(f"El número tiene {cantidad_digitos} dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores.

valor1 = int(input("Introduce el primer valor: "))
valor2 = int(input("Introduce el segundo valor: "))
suma = sum(range(min(valor1, valor2) + 1, max(valor1, valor2)))
print(f"La suma de los números entre {valor1} y {valor2}, excluyendo estos valores, es: {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0.

total = 0
numero = int(input("Introduce un número entero (ingresa 0 para finalizar): "))
while numero != 0:
    total += numero
    numero = int(input("Introduce un número entero (ingresa 0 para finalizar): "))
print(f"El total acumulado es: {total}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

numero_secreto = random.randint(0, 9)
intentos = 0
adivinanza = -1

print("Adivina el número entre 0 y 9.")

while adivinanza != numero_secreto:
    adivinanza = int(input("Introduce tu número: "))
    intentos += 1
    if adivinanza < numero_secreto:
        print(f"Demasiado bajo. Intenta de nuevo. Intento número: {intentos}")
    elif adivinanza > numero_secreto:
        print(f"Demasiado alto. Intenta de nuevo. Intento número: {intentos}")

print(f"¡Felicidades! Adivinaste el número {numero_secreto} después de {intentos} intentos.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente.

for numero in range(100, -1, -2):
    print(numero)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario.

numero = int(input("Introduce un número entero positivo: "))
suma = sum(range(numero + 1))
print(f"La suma de los números entre 0 y {numero} es: {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

pares = 0
impares = 0
positivos = 0
negativos = 0

print("Introduce 100 números enteros:")
for _ in range(100):
    numero = int(input("Número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor).

numeros = []

print("Introduce 100 números enteros:")
for _ in range(100):
    numero = int(input("Número: "))
    numeros.append(numero)

media = mean(numeros)
print(f"La media de los números ingresados es: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 

numero = input("Introduce un número: ")
numero_invertido = numero[::-1]
print(f"El número invertido es: {numero_invertido}")