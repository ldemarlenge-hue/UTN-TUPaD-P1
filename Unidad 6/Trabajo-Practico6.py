#1) Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

def imprimir_hola_mundo():       #definimos la función con def
    return print("Hola Mundo!")  #con return hacemos que la función devuelva algo
#desde el programa principal llamamos a la función:
saludo = imprimir_hola_mundo()


#2) Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
#“Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

#definimos la función:
def saludar_usuario(nombre):
    return print(f"Hola {nombre}!") #creamos el saludo
#creamos el programa, pedimos al usuario su nombre:
nombre_usuario = input("Ingrese su nombre: ")
#llamamos la función
saludo = saludar_usuario(nombre_usuario)


#3) Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
#los datos al usuario y llamar a esta función con los valores ingresados.

#definimos la función:
def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
#creamos el programa, pedimos al usuario sus datos:
print("¡Bienvenido al programa!")
nombre_usuario = input("Por favor ingrese su nombre: ").title()
apellido_usuario = input("Ahora su apellido: ").title()
edad_usuario = input("¿Cuántos años tiene? (ingrese sólo valores numéricos): ")
residencia_usuario = input("¿Dónde reside actualmente? ").title()
#llamamos la función
info_usuario = informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)


#4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
#como parámetro y devuelva el área del círculo. calcular_perimetro_
#circulo(radio) que reciba el radio como parámetro y devuelva
#el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
#funciones para mostrar los resultados.

#definimos las funciones:
def calcular_area_circulo(radio):
    import math
    return (radio**2)*math.pi
def calcular_perimetro_circulo(radio):
    import math
    return 2*radio*math.pi
#creamos el programa, pedimos al usuario el radio del círculo:
print("Hola! Este programa calculará el área y el perímetro de un círculo.")
radio_circulo = int(input("Ingrese el radio del círculo a en cuestión: "))
#llamamos a la función área
area = round(calcular_area_circulo(radio_circulo),2) #para una vista más limpia redondeamos los decimales
#llamamos a la función perímetro
perimetro = round(calcular_perimetro_circulo(radio_circulo),2)
#mostramos los resultados
print(f"El círculo de radio {radio_circulo} tiene {area} de área y {perimetro} de perímetro")


#5) Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar
#el resultado usando esta función.

#definimos la función
def segundos_a_horas(segundos):
    return print(f"{segundos} segundos equivalen a {segundos / 3600} horas")
#creamos el programa, pedimos al usuario que ingrese los segundos:
print("Hola! Este programa calculará la cantidad de horas si se ingresan los segundos.")
segundos = int(input("Ingrese la cantidad de segundos que desea convertir a horas: "))
#llamamos a la función 
conversion = segundos_a_horas(segundos)


#6) Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

#definimos la función
def tabla_multiplicar(numero):
    for i in range (1,11):
        print(f"{numero}x{i}={i*numero}")
    return print()
#creamos el programa, pedimos al usuario que ingrese el número:
print("Si ingresa un número se le mostrará la tabla de multiplicar del mismo")
numero = int(input("Ingrese un número: "))
#llamamos a la función
tabla = tabla_multiplicar(numero)


#7) Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado
#de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
#de forma clara.

#definimos la función
def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b!= 0:
        division = a / b
    else:
        division = None
    return (suma, resta, multiplicacion, division) #se crea una tupla, no se mostrará tendremos que llamar a sus valores por los índices
#creamos el programa, pedimos al usuario los números:
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
#llamamos a la función
operaciones = operaciones_basicas(a,b)
#mostramos los resultados, llamando a cada elemento de la tupla por su índice
print(f"La suma entre {a} y {b} es {operaciones[0]}")
print(f"La resta entre {a} y {b} es {operaciones[1]}")
print(f"La multiplicación entre {a} y {b} es {operaciones[2]}")
if operaciones[3] is not None:
    print(f"La división entre {a} y {b} es {operaciones[3]}")
else:
    print("No se puede dividir por cero")


#8) Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
#para mostrar el resultado con dos decimales.

#definimos la función
def calcular_imc(peso, altura):
    return round(peso/altura**2,2)
#creamos el programa, pedimos al usuario los valores:
print("Cálculo del índice de masa corporal: IMC")
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en m: "))
#Mostramos el resultado:
print(f"El IMC es {calcular_imc(peso,altura)}")

#9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

#definimos la función
def celsius_fahrenheit(celsius):
    F = ((9*celsius)/5)+32
    return print(f"{celsius} grados Celsius equivalen a {F} grados Fahrenheit")
#creamos el programa, pedimos al usuario la temp en Celsius:
print("Conversor de temperatura - Celsius a Fahrenheit")
celsius = int(input("Ingrese una temperatura en grados Celsius: "))
#llamamos a la función 
conversor = celsius_fahrenheit(celsius)


#10) Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

#definimos la función
def calcular_promedio(a,b,c):
    return (a + b + c)/3
#creamos el programa, pedimos al usuario los valores:
print("Cálculo del promedio")
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
#llamamos a la función y mostramos el resultado
print(f"El promedio de los tres valores es {calcular_promedio(a,b,c)}")