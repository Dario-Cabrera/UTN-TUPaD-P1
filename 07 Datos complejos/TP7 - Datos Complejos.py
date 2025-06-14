#1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

print("Diccionario original - Ejercicio 1:", precios_frutas)

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario después de añadir - Ejercicio 1:", precios_frutas)

#2

print("Diccionario antes de actualizar - Ejercicio 2:", precios_frutas)

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Diccionario después de actualizar - Ejercicio 2:", precios_frutas)

#3

print("Diccionario antes de actualizar - Ejercicio 3:", precios_frutas)

lista_frutas = list(precios_frutas.keys())

print("Lista de frutas (claves del diccionario) - Ejercicio 3:", lista_frutas)

#4

contactos_telefonicos = {}

for i in range(5):
    nombre = input(f"Ingresa el nombre del contacto {i+1}: ")
    numero = input(f"Ingresa el numero de telefono de {nombre}: ")
    contactos_telefonicos[nombre] = numero

print("Contactos cargados: ", contactos_telefonicos)

nombre_buscar = input("Ingresa el nombre del contacto que queres buscar: ")

if nombre_buscar in contactos_telefonicos:
    print(f"El número de {nombre_buscar} es: {contactos_telefonicos[nombre_buscar]}")
else:
    print(f"{nombre_buscar} no se encontro en tus contactos")

#5

frase = input("Ingresá una frase: ")

palabras = frase.lower().split()

palabras_unicas = set(palabras)
print("Palabras únicas en la frase:", palabras_unicas)

conteo_palabras = {}
for palabra in palabras:
    conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1

print("Conteo de palabras:", conteo_palabras)

#6

alumnos_notas = {}

for i in range(3):
    nombre_alumno = input(f"Ingresá el nombre del alumno {i+1}: ")
    print(f"Ingresá 3 notas para {nombre_alumno}:")
    try:
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))
        alumnos_notas[nombre_alumno] = (nota1, nota2, nota3)
    except ValueError:
        print("Error, por favor, ingresá solo números para las notas. Saltando este alumno.")

for alumno, notas_tupla in alumnos_notas.items():
    if len(notas_tupla) == 3:
        promedio = sum(notas_tupla) / len(notas_tupla)
        print(f"El promedio de {alumno} es: {promedio}")
    else:
        print(f"No se pudieron calcular las notas de {alumno} debido a un error en la entrada.")

#7

aprobados_parcial1 = {"Juan", "María", "Pedro", "Ana", "Luis"}
aprobados_parcial2 = {"María", "Pedro", "Sofía", "Carlos", "Ana"}

print("Estudiantes que aprobaron Parcial 1:", aprobados_parcial1)
print("Estudiantes que aprobaron Parcial 2:", aprobados_parcial2)

ambos_parciales = aprobados_parcial1.intersection(aprobados_parcial2)
print("Aprobaron ambos parciales:", ambos_parciales)

solo_uno = aprobados_parcial1.symmetric_difference(aprobados_parcial2)
print("Aprobaron solo uno de los dos parciales:", solo_uno)

al_menos_uno = aprobados_parcial1.union(aprobados_parcial2)
print("Aprobaron al menos un parcial:", al_menos_uno)

#8

stock_productos = {
    "Leche": 50,
    "Pan": 100,
    "Huevos": 120,
    "Arroz": 75
}

ejecutando = True

while ejecutando:
    print("Opciones:")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades a un producto existente")
    print("3. Agregar un nuevo producto")
    print("4. Mostrar todo el stock")
    print("5. Salir")

    opcion = input("Elegí una opción (1-5): ")

    if opcion == '1':
        producto = input("Ingresá el nombre del producto a consultar: ")
        if producto in stock_productos:
            print(f"Stock de {producto}: {stock_productos[producto]} unidades.")
        else:
            print(f"'{producto}' no se encuentra en el stock.")

    elif opcion == '2':
        producto = input("Ingresá el nombre del producto al que querés agregar unidades: ")
        if producto in stock_productos:
            try:
                cantidad = int(input(f"¿Cuántas unidades querés agregar a '{producto}'?: "))
                if cantidad > 0:
                    stock_productos[producto] += cantidad
                    print(f"Se agregaron {cantidad} unidades a '{producto}'. Nuevo stock: {stock_productos[producto]}.")
                else:
                    print("La cantidad a agregar debe ser positiva.")
            except ValueError:
                print("Cantidad inválida. Por favor, ingresá un número entero.")
        else:
            print(f"'{producto}' no existe. Usá la opción 3 para agregarlo como nuevo producto.")

    elif opcion == '3':
        producto = input("Ingresá el nombre del nuevo producto: ")
        if producto in stock_productos:
            print(f"'{producto}' ya existe en el stock. Usá la opción 2 para agregar unidades.")
        else:
            try:
                cantidad_inicial = int(input(f"Ingresá el stock inicial de '{producto}': "))
                if cantidad_inicial >= 0:
                    stock_productos[producto] = cantidad_inicial
                    print(f"Producto '{producto}' agregado con stock inicial de {cantidad_inicial} unidades.")
                else:
                    print("El stock inicial no puede ser negativo.")
            except ValueError:
                print("Cantidad inválida. Por favor, ingresá un número entero.")

    elif opcion == '4':
        print("--- Stock Actual ---")
        if stock_productos:
            for prod, stock in stock_productos.items():
                print(f"{prod}: {stock} unidades")
        else:
            print("El stock está vacío.")

    elif opcion == '5':
        print("Saliendo del programa de gestión de stock. ¡Hasta luego!")
        ejecutando = False

    else:
        print("Opción no válida. Por favor, elegí un número entre 1 y 5.")

#9

agenda = {
    ("Lunes", "09:00"): "Reunión de equipo",
    ("Lunes", "14:30"): "Entrenamiento",
    ("Martes", "10:00"): "Llamada con cliente",
    ("Miércoles", "18:00"): "Clase de Python",
    ("Viernes", "09:30"): "Presentación de proyecto"
}

while True:
    dia_consulta = input("Ingresá el día a consultar (ej. Lunes, Martes, 'salir' para terminar): ").capitalize()
    if dia_consulta.lower() == 'salir':
        print("Saliendo de la consulta de agenda.")
        break

    hora_consulta = input("Ingresá la hora a consultar (ej. 09:00): ")

    clave_consulta = (dia_consulta, hora_consulta)

    if clave_consulta in agenda:
        print(f"Actividad el {dia_consulta} a las {hora_consulta}: {agenda[clave_consulta]}")
    else:
        print(f"No hay actividad agendada para el {dia_consulta} a las {hora_consulta}.")

#10

paises_capitales = {
    "España": "Madrid",
    "Francia": "París",
    "Alemania": "Berlín",
    "Italia": "Roma",
    "Japón": "Tokio"
}

print("Diccionario original (País: Capital):", paises_capitales)

capitales_paises = {}
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print("Nuevo diccionario (Capital: País):", capitales_paises)