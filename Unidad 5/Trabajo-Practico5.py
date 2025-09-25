#1) Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja.

#Creo la lista (invento los valores)
notas = [5, 8, 1.5, 5.6, 7, 9.3, 10, 8.75, 6.5, 7.25]
#con "for" muestro la lista con un valor debajo del otro
for i in notas:
    print(i)
#Calculo la suma de todos los valores de la lista con la función "sum"
suma = sum(notas)
#Calculo la cantidad de elementos de la lista con la función "len".
#En este caso ya sé que son 10, pero en caso de que se llegue a modificar la lista 
#(agregando o quitando elementos) con esta función me aseguro de tener la cantidad correcta de elementos que contiene
cant = len(notas)
#Muestro el promedio haciendo el cociente entre suma y cant
print(f"El promedio de las notas es", suma/cant)
#Calculo la nota más alta con la función "max"
mas_alta = max(notas)
#Calculo la nota más baja con la función "min"
mas_baja = min(notas)
#Muestro los valores obtenidos
print(f"La nota más alta fue {mas_alta} y la más baja fue {mas_baja}")


#2) Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

#Doy la instrucción
print("Ingrese los productos de la lista")
#Creo una lista vacía para ir llenándola luego
lista_productos = []
#Como sé que necesito pedir 5 elementos, uso un "for"
for i in range(5):
    print("Ingrese el producto", (i+1)) #i+1 le indicará en qué elemento estamos, el primero, el segundo, etc.
    producto = input().lower() #.lower() para que transforme el string a minúsculas
    lista_productos.append(producto) #agrego cada vez el producto ingresado a la lista
#la función "sorted" los ordena por defecto alfabéticamente si son strings, defino una nueva variable
lista_productos_ordenada = sorted(lista_productos)
#imprimo la lista ordenada alfabéticamente
print(lista_productos_ordenada)
#Le pregunto al usuario qué producto va a eliminar y lo paso a minúscula con "lower"
eliminar = input("Escriba cuál es el producto que desea eliminar ").lower()
#valido si el elemento ingresado está en la lista con un if
if eliminar in lista_productos_ordenada:
    lista_productos_ordenada.remove(eliminar) #elmino el producto que el usuario ingresó, actualizando la lista
    print(lista_productos_ordenada) #Imprimo la lista actualizada
else:
    print("El producto no se encuentra en la lista")


#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.

#Llamo al paquete random para generar números aleatorios
import random
#Genero una lista que indico que será de 15 elementos y deben estar entre 1 y 100
numeros_aleatorios = [random.randint(1,100) for i in range(15)]
#Para que sea más fácil el análisis, ordeno la lista de menor a mayor
numeros_aleatorios_ordenados = sorted(numeros_aleatorios)
#La muestro
print(f"Lista de números aleatorios: {numeros_aleatorios_ordenados}")
#Creo una lista vacía para los números pares y otra para los impares
pares = []
impares = []
#Con "for" analizo si los números de la lista son pares, indico que los agregue a la lista "pares"
#Sino que los agregue a la lista "impares"
for numero in numeros_aleatorios:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
#Para que sea más fácil el análisis ordeno ambas listas de menor a mayor
pares_ordenados = sorted(pares)
impares_ordenados = sorted(impares)
#Las muestro y también muestro cuántos elementos tiene cada una
print(f"Lista de números pares: {pares_ordenados}")
print(f"La lista de números pares tiene {len(pares_ordenados)} elementos")
print(f"Lista de números impares: {impares_ordenados}")
print(f"La lista de números impares tiene {len(impares_ordenados)} elementos")


#4) Dada una lista con valores repetidos:
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado.

#Creo la lista que nos da el enunciado
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
#creo una nueva lista vacía donde se irán acumulando los elementos
sin_repetidos = []
#para ir acumulando los elementos a la lista vacía uso un ciclo for.
for i in datos:
    if i not in sin_repetidos: #dentro del ciclo for uso un if para evaluar si el elemento NO se encuentra en la lista vacía con "not in"
        sin_repetidos.append(i) #lo agrego con append. Si el elemento ya está en esta lista no se agregará.
#muestro la lista original y luego la lista sin los elementos repetidos:
print("Lista original: ", datos)
print("Lista sin elementos repetidos: ", sin_repetidos)


#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada.

#Solicito que ingrese los estudiantes de a uno creando una lista vacía
print("Ingrese los nombres de los estudiantes presentes")
lista_nombres = []
cant_valores = 8 #por si se modifica la cantidad en un futuro defino una variable con el total
for i in range(cant_valores): #con el ciclo for los voy agregando
    print("Ingrese el nombre del estudiante", (i+1))
    nombre = input().lower() #con lower los escribo a todos en minúscula, para mejorar la visual solamente
    lista_nombres.append(nombre) #con append los voy agregando a la lista que tenía vacía
#Imprimo la lista generada, utilizo for para mostrarlos uno al lado del otro separado por guiones con end = " - "
print("Asistencia actual: ")
for i in lista_nombres:
     print (i, end= " - ")
print() #este se utiliza para que el siguiente mensaje no me lo muestre pegado a la lista, sino debajo
#genero una variable llamada instrucción para hacer un input donde consulte si se quiere agregar o eliminar algún estudiante
instruccion = input("¿Desea eliminar (E) un estudiante? ¿O agregar (A) uno?: ").lower() #como pido que me de opciones, con lower las comparo en minúscula independientemente de cómo lo ingresen
#con if realizo las comparaciones
if instruccion == "a": #a si desean agregar a alguien
    nuevo = input("Ingrese el nombre del nuevo estudiante: ") #pido el nuevo nombre
    lista_nombres.append(nuevo) #con append lo agrego a la lista existente
elif instruccion == "e": #e para eliminar a alguien
    eliminado = input("¿Qué estudiante desea eliminar? Ingrese su nombre: ") #pregunto a quién desean eliminar
    if eliminado in lista_nombres: #con otro if evalúo si ese nombre está en la lista realmente
            lista_nombres.remove(eliminado) #si está, lo elimino con remove
    else:
         print("El estudiante ingresado no existe.") #si no está, le hago un mensaje al usuario
else: #finalmente con esta opción hago un mensaje en caso de que hayan ingresado una opción que no sea a ni e
     print("Opción incorrecta.")
#Imprimo la lista actualizada, utilizo for para mostrarlos uno al lado del otro separado por guiones con end = " - "
print("Asistencia actualizada: ")
for i in lista_nombres:
     print (i, end= " ")


#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

#Genero una lista de 7 elementos
numeros = [1, 2, 3, 4, 5, 6, 7]
#separo el último número de la lista (si escribo -1 me dará siempre el último elemento de la lista)
ultimo_numero = numeros[-1]
#genero otra lista que contenga todos los demás elementos, excepto el último.
#desde el elemento 0 (si no pongo nada por defecto comienza desde 0) hasta el final exceptuando el último (por eso hasta -1)
resto = numeros[:-1]
#genero la nueva lista con el orden alternado. Concatenando ambas listas.
#ultimo_numero es un entero, lo encierro entre [] para que se convierta en una lista
nueva_lista = [ultimo_numero] + resto
#imprimo la nueva lista
print(nueva_lista)


#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
#semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica.

#genero una lista de los días de la semana, servirá para mostrar los resultados finales
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
#genero la matriz de las temperaturas de la semana con una lista anidada.
matriz_semana = [[5, 15], [5, 18], [6, 20], [5, 19], [4, 21], [3, 22], [4, 25]]
#defino las variables que van a acumular las temperaturas mínimas y las máximas
suma_min = 0
suma_max = 0
#con un ciclo for recorremos la matriz para acumular las temperaturas mínimas y máximas
for fila in matriz_semana:
    suma_min += fila[0] #fila[0] es la mínima del día actual
    suma_max += fila[1] #fila[1] es la máxima del día actual
#calculo el promedio, es la suma acumulada dividida la cantidad de días
promedio_min = suma_min/7.0
promedio_max = suma_max/7.0
#defino una variable que guarde la mayor amplitud encontrada hasta ahora, la inicializo en -1
mayor_amp = -1
#defino una variable para guardar el día que tuvo la mayor amplitud encontrada hasta ahora, también se inicia en -1
indice_mayor = -1
#nuevamente con un ciclo for recorremos la matriz para encontrar las mínimas y máximas de cada día
for i in range (7):
    min_dia = matriz_semana[i][0]
    max_dia = matriz_semana[i][1]
    #la amplitud será la resta entre la máxima y la mínima de cada día
    amp = max_dia - min_dia
    #con un ciclo if evalúo: si la amplitud es mayor al acumulador definido previamente (mayor_amp) guardo el valor encontrado en esa variable
    if amp > mayor_amp:
        mayor_amp = amp
        indice_mayor = i #i es el día en que se registró esa mayor amplitud
#Muestro los resultados obtenidos
print("Matriz semana [min, max]:", matriz_semana)
print("Promedio mínimas:", round(promedio_min,2)) #round (x,2) redondea mostrando sólo 2 decimales
print("Promedio máximas:", round(promedio_max,2))
print("Mayor amplitud en:", dias[indice_mayor], "con", mayor_amp)


#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
#• Mostrar el promedio de cada estudiante.
#• Mostrar el promedio de cada materia.

#genero una lista de los estudiantes, servirá para mostrar los resultados finales
estudiantes = ["Ana", "Luis", "Ines", "Marcos", "Marta"]
#genero una lista de las materias, servirá para mostrar los resultados finales
materias = ["Matemáticas", "Química", "Lengua"]
#genero la matriz de las notas de cada materia con una lista anidada.
notas = [[9, 10, 7], [8, 8, 8], [5, 5, 6.5], [7, 6, 3], [6, 4, 5]]
#muestro las notas de cada estudiante:
print("Notas (filas=estudiantes, columnas=materias):")
for i in range (len(estudiantes)): #i recorre las filas
    #notas[i] es la lista de las 3 notas del estudiante i
    print(" ", estudiantes[i], ":", notas[i])
#calculamos los promedios de cada alumno:
print("Promedio por estudiante:")
#con un ciclo for recorremos cada fila para calcualr el promedio
for i in range (len(estudiantes)): #i es el índice del estudiante actual
    suma = 0 #en esta variable se acumularán las notas para las 3 materias
    for j in range (3): #j recorre las columnas que corresponden a las materias
        suma += notas[i][j]
    promedio = suma/3.0 #son 3 materias por eso dividimos por 3
    #mostramos el promedio
    print(" ", estudiantes[i], ":", round(promedio,2))
#calculamos los promedios de cada materia:
print("Promedio por materia:")
#con un ciclo for recorremos cada columna para calcualr el promedio
for j in range (3): #j es el índice de la materia actual
    suma = 0 #en esta variable se acumularán las notas para los 5 estudiantes
    for i in range (5): #i recorre las filas que corresponden a los estudiantes
        suma += notas[i][j]
    promedio = suma/5.0 #son 5 alumnos por eso dividimos por 5
    #mostramos el promedio
    print(" ", materias[j], ":", round(promedio,2))


#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#• Mostrar el tablero después de cada jugada.

#genero una matriz vacía
tablero = []
#para completarlo utilizamos un ciclo for
for _ in range (3):
    fila = []
    for _ in range (3):
        fila.append("-")
    tablero.append(fila)
#designamos la variable turno, serán 9 totales
turno = 0
#para que se vayan alternando designamos la variable del jugador
jugador_actual = "X"

while turno < 9:
    print("Tablero actual:")
    for f in range (3):
        print(tablero[f][0], tablero[f][1], tablero[f][2])
    
    print("Juega: ", jugador_actual)
    fila_ing = int(input("Ingresá la FILA 1-3: ")) -1
    columna_ing = int(input("Ingresá la COLUMNA 1-3: ")) -1
    #validar si elige una posición fuera de la matriz
    if fila_ing < 0 or fila_ing > 2 or columna_ing < 0 or columna_ing > 2:
        print("Posición fuera del rango. Volvé a intentar")
        continue #para que no pierda el turno
    #validamos si la posición está ocupada
    if tablero[fila_ing][columna_ing] != "-":
        print("Casilla ocupada, ingresá otra")
        continue #para que no pierda el turno
    #si pasa las validaciones, colocamos la marca del jugador actual:
    tablero[fila_ing][columna_ing] = jugador_actual
    #mostramos cómo quedó el tablero luego de la jugada:
    print("Después de la jugada:")
    #utilizamos un ciclo for
    for f in range (3):
        print(tablero[f][0], tablero[f][1], tablero[f][2])
    #Cambiamos el jugador para la próxima jugada:
    if jugador_actual == "X":
        jugador_actual = "O"
    else:
        jugador_actual = "X"

    #avanzamos el contador de jugadas
    turno = turno + 1

print("Juego terminado (9 jugadas)")


#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#• Mostrar el total vendido por cada producto.
#• Mostrar el día con mayores ventas totales.
#• Indicar cuál fue el producto más vendido en la semana.

#genero la matriz de ventas
ventas =[[5, 3, 2, 7, 4, 6, 3], [2, 8, 1, 3, 5, 7, 4], [6, 4, 7, 2, 8, 8, 5], [3, 6, 4, 5, 2, 9, 7]]
#calculo los totales de los productos
totales_productos = []
#con for calculamos la cantidad de ventas de cada producto
for i in range (4): #i es la fila que corresponde al producto
    total_producto = 0
    for j in range (7): #j es la columna que corresponde al día
        total_producto += ventas[i][j]
    totales_productos.append(total_producto) #venta semanal de cada producto
    print(f"Producto {i+1}: {total_producto}")
#defino una variable que guardará cuál fue la mayor venta diaria
mayor_ventas = 0
#defino una variable que guardará el día de mayor venta
dia_mayor = 0
#calculamos el día con más ventas con un for
for j in range (7): #j es la columna que corresponde al día
    total_dia = 0
    for i in range (4): #i es la fila que corresponde al producto
        total_dia += ventas[i][j]
    print(f"Total del día {j+1}: {total_dia}")
    #con if evalúo que día se dió la mayor venta
    if total_dia > mayor_ventas:
        mayor_ventas = total_dia
        dia_mayor = j
#imprimo el resultado
print(f"El día con mayores ventas fue el {dia_mayor+1}, con {mayor_ventas} ventas.")
#Calculo cuál fue el producto más vendido
#defino dos nuevas variables para calcularlo
mayor_producto = 0
indice_producto = 0
#con for hago la evaluación sobre los productos, las filas
for i in range (4):
    if totales_productos[i] > mayor_producto:
        mayor_producto = totales_productos[i]
        indice_producto = i
print(f"El producto más vendido es {indice_producto+1}, con {mayor_ventas} ventas en la semana.")