#1)Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

#2)Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo
# usando el nombre ingresado.
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia
# e imprima por pantalla una oración con los datos ingresados. 
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima 
# por pantalla su área y su perímetro.
radio = int(input("Ingrese el radio del círculo: "))
import math
valor_pi = math.pi
area = valor_pi*radio**2
perimetro = 2*valor_pi*radio
print(f"Dado el círculo de radio {radio}, su área es {area} y su perímetro es {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e 
# imprima por pantalla a cuántas horas equivale.
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = round(segundos/3660,2) #redondea la cantidad de decimales que indicamos
print(f"{segundos} segundos equivale a {horas} horas")

#6) Crear un programa que pida al usuario un número e 
# imprima por pantalla la tabla de multiplicar de dicho número.
numero = input("Ingrese un número: ")
print("1 x " + numero + " = ", 1*int(numero))
print("2 x " + numero + " = ", 2*int(numero))
print("3 x " + numero + " = ", 3*int(numero))
print("4 x " + numero + " = ", 4*int(numero))
print("5 x " + numero + " = ", 5*int(numero))
print("6 x " + numero + " = ", 6*int(numero))
print("7 x " + numero + " = ", 7*int(numero))
print("8 x " + numero + " = ", 8*int(numero))
print("9 x " + numero + " = ", 9*int(numero))
print("10 x " + numero + " = ", 10*int(numero))

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 
# y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos 
# y restarlos.
num1 = input("Ingrese un número distinto de 0: ")
num2 = input("Ingrese otro número también distinto de 0: ")
print(num1 + " + " + num2 + " = ", int(num1) + int(num2))
print(num1 + " - " + num2 + " = ", int(num1) - int(num2))
print(num1 + " / " + num2 + " = ", int(num1) / int(num2))
print(num1 + " * " + num2 + " = ", int(num1) * int(num2))

#8) Crear un programa que pida al usuario su altura y su peso 
# e imprima por pantalla su índice de masa corporal.
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en m: "))
IMC = round(peso/altura**2,2)
print(f"Su índice de masa corporal es {IMC}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius 
# e imprima por pantalla su equivalente en grados Fahrenheit.
celcius = int(input("Ingrese una temperatura en grados Celcius: "))
F = ((9*celcius)/5)+32
print(f"El equivalente en grados Fahrenheit es {F}")

#10) Crear un programa que pida al usuario 3 números 
# e imprima por pantalla el promedio de dichos números.
num1=int(input("Ingrese un número: "))
num2=int(input("Ingrese otro número: "))
num3=int(input("Ingrese un último número: "))
promedio = (num1 + num2 + num3)/3
print("El promedio de los tres números ingresados es", promedio)