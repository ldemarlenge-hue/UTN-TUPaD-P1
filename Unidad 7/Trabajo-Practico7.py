#Práctico 7: Estructuras de datos complejas

#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
#1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

#Diccionario original:
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#Agregar pares key-value:
precios_frutas ['Naranja'] = 1200
precios_frutas ['Manzana'] = 1500
precios_frutas ['Pera'] = 2300
#Impresión del nuevo diccionario:
print(precios_frutas)


#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

#Impresión del diccionario resultante del pto. anterior:
print(precios_frutas)
#Actualizar precios:
precios_frutas ['Banana'] = 1330
precios_frutas ['Manzana'] = 1700
precios_frutas ['Melón'] = 2800
#Impresión de los precios actualizados:
print(precios_frutas)


#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
#precios.

#Lista con las frutas sin precios:
print(precios_frutas.keys())


#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

#Se define la variable cant_contactos porque es más fácil de modificar.
#Si a futuro se quiere solicitar al usuario más contactos (o menos) sólo se modifica
#el valor en esta variable y el resto del programa igual funcionaría.
cant_contactos = 5
#Se crea un diccionario vacío que se irá llenando con los datos que el usuario ingrese:
contactos = dict()
#Con un ciclo for se le solicita al usuario que ingrese los 5 contactos:
print("¡Bienvenido a su diccionario de contactos")
print("Primero lo crearemos:")
for i in range (1, cant_contactos+1):
    print("Ingrese el nombre del contacto",(i)) #le indica al usuario el orden del contacto que está ingresando
    nombre = str(input()).title() #guarda el nombre en la variable que luego se utilizará como key para crear el diccionario
    #las keys no pueden repetirse por lo que debemos validar si ese nombre ya existe en el diccionario, sino lo sobreescribirá
    if nombre in contactos:
        #si el nombre ya se ingresó, se informa al usuario.
        #si es otra persona con el mismo nombre puede identificarlo de otra manera: ejemplo el nombre con la primera letra del apellido o con un sobrenombre
        #si se equivocó tiene la posibilidad de continuar agregando a otra
        print("Ya existe un contacto con ese nombre. Si es otra persona identifíquelo de otra manera")
        print("Ingrese el nombre del contacto",(i))
        nombre = str(input()).title()
        print(f"Ingrese el número de teléfono de {nombre}:")  #solicita el número de teléfono del nombre ingresado previamente
        telefono = int(input()) #guarda el teléfono en la variable que luego se utilizará como value para crear el diccionario
        contactos[nombre] = telefono #guarda el par key-value en el diccionario
    else:
        #si el nombre no se había ingresado previamente, continúa solicitando el teléfono
        print(f"Ingrese el número de teléfono de {nombre}:")
        telefono = int(input()) 
        contactos[nombre] = telefono 
#Se muestra al usuario como quedó el diccionario:        
print("Su diccionario de contactos quedó guardado de la siguiente manera:")
print(contactos)

#Se procede a consultar un teléfono:
print("Consultar un teléfono:")
print("Ingrese el nombre del contacto a consultar")
nombre = str(input()).title()
#Validación: si existe en el diccionario se muestra el teléfono de esa persona
if nombre in contactos:
    print(f"El número de teléfono de {nombre} es {contactos[nombre]}")
#sino, se muestra un mensaje
else:
    print("El nombre ingresado no existe en su diccionario.")


#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

#Se plantea una función para analizar la frase por ser más práctico 
#el análisis y las validaciones.
#Se define la función analizar_frase y como argumento tiene la frase
#que se le solicitará ingresar al usuario.
def analizar_frase(frase):
    #A la frase ingresada se la guarda en una nueva variable ya que
    #se la convierte en una lista de palabras usando los espacios como separadores con la función .split()
    #con .lower() lo que hacemos es convertir toda la frase en minúscula para que no tome como palabras diferentes
    #si por ejemplo se ingresa "Hola" y "hola"
    lista_depalabras = frase.lower().split()
    #Generamos un set con la lista antes realizada y se cumple con la primer parte del ejercicio 
    palabras_unicas = set(lista_depalabras)
    #Generamos un diccionario vacío donde iremos guardando el conteo de palabras
    contar_palabras = {}
    #Con un ciclo for recorremos la lista de palabras:
    for palabra in lista_depalabras:
        #para cada palabra aumenta su conteo en el diccionario
        #si la palabra aun no existe en el diccionario .get(palabra, 0) devuelve 0 pero le suma 1 para contar la primera aparición
        contar_palabras[palabra] = contar_palabras.get(palabra, 0) + 1
    #finalmente la función devuelve los resultados requeridos:
    print(f"Palabras únicas en la frease: {palabras_unicas}")
    print(f"frecuencia de cada palabra en la frase: {contar_palabras}")

#En el programa solo resta solicitar al usuario que ingrese una frase
frase_usuario = input("Ingrese una frase: ")
#y llamar a la función
analizar_frase(frase_usuario)


#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.

#Se guarda la cantidad de alumnos en una variable para que sea más fácil modificar a futuro
cant_alumnos = 3
#Con un ciclo for se solicitan la nota de los 3 alumnos:
for i in range(1, cant_alumnos+1):
    #primero se ingresa el nombre del alumno
    print("Ingrese el nombre del alumno", i)
    #se guarda el valor ingresado en la varibale nombre
    nombre = input().title()
    
    #Necesitamos un ciclo while que se ejecute siempre por eso comienza con True
    #nos permitirá hacer una validación importante:
    while True:
        #Ahora se solicitan las notas, será un texto por la manera en la que lo solicitamos
        print(f"Ingrese las 3 notas de {nombre}, separe cada una con un espacio (ej: 7 8 9):")
        #se guardan los valores en la variable notas
        notas = input()
        #¿qué pasa si el usuario ingresa un valor no numérico? Nos dará un ValueError y no permitirá continuar
        #para sobrepasar eso un try-except nos permite evaluarlo y continuar
        try:
            #convertimos los valores ingresados en una lista con .split() que tomará cada espacio como separación de valor
            lista_notas_str = notas.split()
            #esta lista es de string por cómo solicitamos la información, debemos convertirla a float para poder calcular el promedio
            #con for recorremos la lista de notas y con float los convertimos en numéricos 
            notas_lista = [float(nota) for nota in lista_notas_str]
            #si está ok salimos del bucle
            break
        #si uno o más de los valores no son numéricos dará ValueError la línea donde intentamos pasarlo a float
        #en ese caso se da un mensaje al usuario y puede volver a ingresar las notas (gracias a que estamos en un ciclo while)
        except ValueError:
            print("ERROR: una o más notas ingresadas no son números válidos. Ingrese las notas nuevamente.")
        
    #convertimos la lista anterior en una tupla
    notas_tupla = tuple(notas_lista)
    #calculamos el promedio, redondeamos en 2 decimales
    promedio = round(sum(notas_tupla)/len(notas_tupla),2)
    #mostramos las notas ingresadas y el promedio del alumno
    print(f"Notas ingresadas: {notas_tupla}")
    print(f"Promedio de {nombre}: {promedio}")
    #el ciclo for continuará solicitando los datos de otro alumno y hará todo el análisis hasta llegar a "cant_alumnos"


#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

#Se cre un set de estudiantes que aprobaron el primer parcial y la muestro para el análisis:
aprobaron_p1 = {"Marcos", "María", "Juan", "Keila", "Rodrigo", "Ana", "Antonio"}
print(f"Alumnos que aprobaron el primer parcial: {aprobaron_p1}")
#Se cre un set de estudiantes que aprobaron el segundo parcial y la muestro para el análisis:
aprobaron_p2 = {"Marcos", "María", "Keila", "Rodrigo", "Ana", "Miguel", "Lujan", "Sergio"}
print(f"Alumnos que aprobaron el segundo parcial: {aprobaron_p2}")

#Aprobaron ambos parciales: intersección
print(f"Aprobaron ambos parciales: {aprobaron_p1.intersection(aprobaron_p2)}")
#Aprobaron sólo uno: diferencia simétrica
print(f"Aprobaron solo un parcial: {aprobaron_p1.symmetric_difference(aprobaron_p2)}")
#Aprobaron al menos uno: unión
print(f"Aprobaron al menos un parcial: {aprobaron_p1.union(aprobaron_p2)}")


#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

#Se crea un diccionario de productos de librería y su stock:
stock_productos = {'Cuadernos': 200, 'Carpetas': 500, 'Lapiceras': 300, 'Calculadoras': 145}
#Se muestra el listado para que el usuario lo vea:
print(f"Lista de productos y su stock: {stock_productos}")

#Se utiliza una lista para guardar las opciones del menú:
opciones_menu = [
    "1. Consultar el stock de un producto",
    "2. Agregar unidades al stock si el producto ya existe",
    "3. Agregar un nuevo producto si no existe",
    "4. Salir "]

#Con el ciclo While podremos recorrer el menú hasta que el usuario desee salir
while True:
    #Se imprime el menú
    print("---Menú---")
    for opcion in opciones_menu:
        print(opcion)
    #se pide al usuario que ingrese una opción
    seleccion = input("Seleccione una opción: ").strip() #elimina los espacios de adelante y atrás
    print("------------------------------")

     #Se analiza cada opción del menú con match-case
    match seleccion:
        case "1":
            print("¿De qué producto desea conocer su stock (escribalo en plural)?")
            producto = input().title() #con title nos aseguramos que esté escrito exactamente igual que en el diccionario
            #con if validamos si el producto está en el diccionario:
            if producto in stock_productos:
                #si está, mostramos el stock:
                print(f"Hay {stock_productos[producto]} {producto}")
            
            else:
                #si no está lo informamos:
                print("El producto ingresado no se encuentra registrado")

        case "2":
            print("¿De qué producto desea agregar unidades (escribalo en plural)?")
            producto = input().title()
            #con if validamos si el producto está en el diccionario:
            if producto in stock_productos:
                #si está solicito que ingrese el nuevo stock
                print("Ingrese el nuevo valor de stock")
                valor = input()
                #y modificamos el diccionario
                stock_productos[producto] = valor
                #mostramos el diccionario actualizado para conocimiento del usuario:
                print(f"Lista de productos actualizada: {stock_productos}")
            else:
                #si no está lo informamos
                print("El producto ingresado no está registrado, para registrarlo elija la opción 3")

        case "3":
            print("Nombre del producto a agregar (escribalo en plural)")
            producto = input().title()
            #con if validamos si el producto está en el diccionario:
            if producto in stock_productos:
                #si está informamos que esta no es la opción correcta
                print("El producto ingresado ya está registrado, para modificar su stock elija la opción 2")
            else:
                #si no está pedimos la cantidad de unidades
                print("Ingrese la cantidad de unidades")
                valor = input()
                #y modificamos el diccionario
                stock_productos[producto] = valor
                #mostramos el diccionario actualizado para conocimiento del usuario:
                print(f"Lista de productos actualizada: {stock_productos}")
                
        case "4":
            print("Saliendo...")
            break
        #en caso de que escriba algo diferente a las opciones del menú:
        case _:
            print("Opción incorrecta, debe elegir una opción entre 1 y 4")
    

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.

#Se genera la agenda:
agenda = {("Lunes", "10:00hs"): "Reunión", ("Lunes", "14:00hs"): "Médico", ("Martes", "15:00hs"): "Clase de Inglés", ("Sábado", "09:00hs"): "Parcial Programación"}

#Se crea una función para hacer el análisis porque es más sencillo
def consultar_agenda(agenda):
    #Solicitar día a consultar:
    dia_consulta = input("Ingrese el día que desea consultar: ").title()
    #Se crea una lista vacía donde se irán guardando las actividades del día
    actividad_dia = {}
    #se inicia la variable encontrado como falsa
    encontrado = False

    #Se itera sobre las key del diccionario (son las tuplas (día, hora)) con .items()
    #el valor del diccionario es el evento
    for dia_hora, evento in agenda.items():
        #Se desempaqueta la tupla (día, hora)
        #permite asignar el nombre del día a la variable dia y el horario a la varible hora
        dia, hora = dia_hora 

        #Se comparar el día ingresado con el día de la key
        if dia == dia_consulta:
            #si está, en actividad_dia se guarda el evento en el diccionario creado anteriormente
            actividad_dia[hora] = evento
            #y la variable encontrado pasa a True
            encontrado = True

    #Mostrar el resultado
    print(f"\n--- Actividades para el día {dia_consulta} ---")
    if encontrado:
        #Se iterar sobre las actividades encontradas para mostrarlas ordenadas por hora
        for hora, evento in sorted(actividad_dia.items()):
            print(f"{hora}: {evento}")
    else:
        print(f"No se encontraron actividades para el día {dia_consulta}.")

print("¿Desea conocer su agenda?")
#se llama a la función:
consultar_agenda(agenda)


#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.

#Diccionario original: {País: Capital}
paises_capitales = {"Argentina": "Buenos Aires", "Chile": "Santiago", "España": "Madrid", "Alemania": "Berlín"}
#Se crea un diccionario vacío para almacenar la inversión
capitales_paises = {}
#Se itera sobre los elementos (key (país), valor(capital)) del diccionario original
for pais, capital in paises_capitales.items():
    #Se asigna la capital como la NUEVA key y el país como el NUEVO valor
    capitales_paises[capital] = pais

#Se muestran los resultados
print("Diccionario original (País: Capital):")
print(paises_capitales)

print("Nuevo Diccionario Invertido (Capital: País):")
print(capitales_paises)