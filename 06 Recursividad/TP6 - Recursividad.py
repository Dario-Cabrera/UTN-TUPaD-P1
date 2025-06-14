#Funciones

#1

def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return "El factorial no esta definido para numero negativos"
    else:
        return n * factorial(n - 1)

#2

def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    elif posicion < 0:
        return "La posicion debe ser un numero entero positivo"
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

#3

def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente < 0:
        return "Exponentes negativos no soportados"
    else:
        return base * potencia(base, exponente - 1)

#4

def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"
    elif decimal == 1:
        return "1"
    else:
        return decimal_a_binario(decimal // 2) + str(decimal % 2)

#5

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    else:
        if palabra[0] == palabra[-1]:
            return es_palindromo(palabra[1:-1])
        else:
            return False

#6

def suma_digitos(n):
    if n < 0:
        return "El numero debe ser positivo"
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

#7

def contar_bloques(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n < 0:
        return "El numero de bloques debe ser positivo."
    else:
        return n + contar_bloques(n - 1)

#8

def contar_digito(numero, digito):
    if numero < 0:
        return "El numero debe ser positivo"
    if not (0 <= digito <= 9):
        return "El digito a buscar debe estar entre 0 y 9"
    
    if numero == 0:
        return 0
    
    ultimo_digito = numero % 10

    if numero < 10:
        if ultimo_digito == digito:
            return 1
        else:
            return 0
    else:
        contador = 0
        if ultimo_digito == digito:
            contador = 1
        
        return contador + contar_digito(numero // 10, digito)

#Principal

#1

def calcular_factoriales_hasta_n():
    try:
        num_ingresado = int(input("Ingresa un numero entero positivo"))
        if num_ingresado < 1:
            print("Por favor ingresar un numero igual o mayor a 1")
            return

        for i in range(1, num_ingresado + 1):
            resultado_factorial = factorial(i)
            print(f"{i}! = {resultado_factorial}")
    except ValueError:
        print("Entrada invalida. Por favor ingresa un numero entero.")

#2

def mostrar_serie_fibonacci():
    try:
        pos_limite = int(input("Ingrese la posicion hasta la cual queres ver la serie"))
        if pos_limite < 0:
            print("Por favor, ingresa una posicion positiva")
            return
        
        for i in range(pos_limite + 1):
            valor = fibonacci(i)
            print(f"F({i}) = {valor}")
    except ValueError:
        print("Entrada invalida. Ingrese un numero entero.")

#3

def calcular_potencia():
    try:
        base_ingresada = float(input("Inre la base en numero: "))
        exponente_ingresado = int(input("Ingrese el exponente: "))

        resultado_potencia = potencia(base_ingresada, exponente_ingresado)

        print(F"{base_ingresada} elevado a la {exponente_ingresado} es: {resultado_potencia}")
    except ValueError:
        print("Entrada invalida. Verifique los numeros ingresados")

#4

def convertir_decimal_a_binario():
    try:
        num_decimal = int(input("Ingrese un numero entero positivo en decimal: "))
        if num_decimal < 0:
            print("Ingrese un numero entero positivo")
            return
        elif num_decimal == 0:
            print(f"El numero {num_decimal} en binario es: 0")
        else:
            binario_resultado = decimal_a_binario(num_decimal)
            print(f"El número {num_decimal} en binario es: {binario_resultado}")
    except ValueError:
        print("Entrada invalida, por favor ingrese un numero entero positivo")

#5

def verificar_palindromo():
    palabra_ingresada = input("Ingresa una palabra")

    if es_palindromo(palabra_ingresada):
        print(f"{palabra_ingresada} SI es un palindromo")
    else:
        print(f"{palabra_ingresada} NO es un palindromo")

#6

def calcular_suma_digitos():
    try:
        numero_ingresado = int(input("Ingrese un numero entero positivo"))
        if numero_ingresado < 0:
            print("Por favor, ingresa un numero entero positivo")
            return
        
        resultado_suma = suma_digitos(numero_ingresado)
        print(f"La suma de los digitos de {numero_ingresado} es: {resultado_suma}")
    except ValueError:
        print("Entrada invalida. Ingrese un numero entero positivo")

#7

def calcular_total_bloques():
    try:
        bloques_base = int(input("Ingrese un numero de bloques de la base"))
        if bloques_base < 1:
            print("El numero de bloques en la base debe ser al menos 1")
            return
        
        total = contar_bloques(bloques_base)
        print(f"Para una piramide con {bloques_base} bloques en la base, se necesitan {total} bloques en total")
    except ValueError:
        print("Entrada invalida, ingrese un numero entero positivo")

#8

def contar_digito_en_numero():
    try:
        num_ingresado = int(input("Ingresa un numero entero positivo: "))
        if num_ingresado < 0:
            print("Por favor ingrese un numero entero positivo")
            return
        
        digito_buscar = int(input("Ingresa el digito (0-9) que queres contar: "))
        if not (0 <= digito_buscar <= 9):
            print("El digito a buscar debe ser un numero entero entre 0 y 9")
            return
        
        if num_ingresado == 0 and digito_buscar == 0:
            print(f"El digito {digito_buscar} aparece 1 vez en el numero {num_ingresado}")
            return
        elif num_ingresado == 0 and digito_buscar != 0:
            print(f"El digito {digito_buscar} aparece 0 veces en el número {num_ingresado}")
            return
        
        cantidad_veces = contar_digito(num_ingresado, digito_buscar)
        print(f"El digito {digito_buscar} aparece {cantidad_veces} veces en el numero {num_ingresado}")
    except ValueError:
        print("Entrada invalida. Por favor ingrese numeros enteros.")

#Llamadas

#1

calcular_factoriales_hasta_n()

#2

mostrar_serie_fibonacci()

#3

calcular_potencia()

#4

convertir_decimal_a_binario()

#5

verificar_palindromo()

#6

calcular_suma_digitos()

#7

calcular_total_bloques()

#8

contar_digito_en_numero()