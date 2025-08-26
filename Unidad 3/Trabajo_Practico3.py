#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#defino que edad otorga la mayoría de edad legal
MAYOR_EDAD = 18 
#solicito al usuario que ingrese su edad y guardo el dato en la variable "edad"
edad = int(input("Ingrese su edad: ")) 
#con un condicional simple determino que si la edad ingresada por el usuario es mayor
#a 18 (definia anteriormente), se imprime el mensaje. Caso contrario el programa termina.
if edad >= MAYOR_EDAD:
    print("Es mayor de edad")


#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; 
# en caso contrario deberá mostrar el mensaje “Desaprobado”.

#solicito al usuario que ingrese su nota y guardo el dato en la variable "nota"
nota = int(input("Ingrese su nota: "))
#con un condicional evalúo que si la nota es mayor o igual que 6 se indica "Aprobado".
#Caso contrario (con else) se indica que está "Desaprobado". Sí o sí una de las condiciones se ejecuta.
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, 
# imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, 
# imprimir por pantalla "Por favor, ingrese un número par". 

#solicito al usuario que ingrese un número y guardo el dato en la variable "numero"
numero = int(input("Ingrese un número par: "))
#con un condicional evalúo que si el numero es par se indica "Ha ingresado un número par".
#Caso contrario (con else) se indica "Por favor ingrese un número par". Sí o sí una de las condiciones se ejecuta.
#No hemos visto como hacer para que el programa siga ejecutándose y aguardando otra respuesta.
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor ingrese un número par")


#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

#solicito al usuario que ingrese su edad y guardo el dato en la variable "edad"
edad = int(input("Ingrese su edad: "))

#con un condicional anidado evalúo si son valores válidos y dependiendo el caso le informo al usuario su categoría
if edad >= 0 and edad < 12:
    print ("Eres un/a niño/a")
elif edad >= 12 and edad < 18:
    print("Eres un adolescente")
elif edad >= 18 and edad < 30:
    print("Eres un/a adulto/a jóven")
elif edad >= 30 and edad < 130:
    print("Eres un/a adulto/a")
else:
    print("Edad no válida")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 

#solicito al usuario que ingrese una contraseña, la defino como string porque pueden ser números, letras o símbolos y guardo el dato en la variable "contraseña"
contraseña = str(input("Ingrese una contraseña: "))
#defino la variable longitud para que cuente los caracteres de la contraseña ingresada con la función len()
longitud = len(contraseña)
#con un condicional simple evalúo la longitud de la contraseña ingresada.
if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media 
# y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. 
# Imprimir el resultado por pantalla.

#genero una lista de 50 números aleatorios
import random
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
#defino como "mi lista" a los números aleatorios generados y hago que el programa los muestre
mi_lista = numeros_aleatorios
print(mi_lista)
#calculo la media, la moda y la mediana y los muestro en pantalla
from statistics import mode, median, mean
media = mean(mi_lista)
moda= mode (mi_lista)
mediana = median(mi_lista)
print(f"La media es {media}, la moda es {moda} y la mediana es {mediana}")
#con un condicional anidado colocolo las condiciones para que sea sesgo positivo, negativo o sin sesgo y hago
#que se muestre el resultado por pantalla
if media > mediana and mediana > moda:
    print ("Sesgo positivo")
elif media < mediana and mediana < moda:
    print ("Sesgo negativo")
elif media == mediana and media == moda:
    print ("Sin sesgo")


#7) Escribir un programa que solicite una frase o palabra al usuario. 
# Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; 
# en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

#Solicito al usuario que ingrese una frase o cadena y la defino como string
frase = str(input("Ingrese una frase o palabra: "))
#calculo su longitud para poder separar la última letra
longitud = len(frase)
ultima_letra = frase [longitud - 1]
#utilizo un condicional para indicar que si la frase termina en a o A debe agregar un ! sino queda igual
if ultima_letra == "a" or ultima_letra == "A":
    print(f"{frase}!")
else:
    print(f"{frase}")


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. 

#Solicito al usuario que ingrese su nombre y lo defino como string
nombre = str(input("Ingrese su nombre: "))
#le doy las opciones y guardo la salida en la variable opcion
opcion = input("Si desea que se devuelva su nombre en mayúsculas, presione 1. Si desea que se devuelva su nombre en minúsculas, presione 2. Si desea que la primer letra de su nombre se muestre en mayúscula, presione 3. ")
#dependiendo la opcion, con un condicional transformo el string
if opcion == "1":
    mayusculas = nombre.upper()
    print(f"{mayusculas}")
elif opcion == "2":
    minusculas = nombre.lower()
    print(f"{minusculas}")
elif opcion == "3":
    titulo = nombre.title()
    print(f"{titulo}")


#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

#Solicito al usuario que ingrese la magnitud y guardo el valor en la variable "terremoto"
terremoto = int(input("Ingrese la magnitud del terremoto ocurrido: "))

#evalúo el dato ingresado y clasifico
if terremoto < 3:
    print("Categoría MUY LEVE. Imperceptible")
elif terremoto >= 3 and terremoto < 4:
    print("Categoría LEVE. Ligeramente perceptible")
elif terremoto >= 4 and terremoto < 5:
    print("Categoría MODERADO. Sentido por personas, pero generalmente no causa daños")
elif terremoto >= 5 and terremoto < 6:
    print("Categoría FUERTE. Puede causar daños en estructuras débiles")
elif terremoto >= 6 and terremoto < 7:
    print("Categoría MUY FUERTE. Puede causar daños significativos")
elif terremoto >= 7:
    print("Categoría EXTREMO. Puede causar graves daños a gran escala")


#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

#solicito los datos al usuario
hemisferio = str(input("Indique en que hemisferio se encuentra. Utilice N para Norte y S para Sur. "))
mes = str(input("Indique en que mes se encuentra: "))
dia = int(input("Indique con números qué día es: "))
#con condicionales anidados evalúo la estación que corresponde a cada condición
if hemisferio == "S" or hemisferio == "s":
    if (mes == "enero" or mes == "febrero") and dia <=31:
        print("Es verano")
    elif mes == "diciembre":
        if dia >= 21:
            print("Es verano")
        else:
            print("Es primavera")
    elif mes == "marzo":
        if dia <= 20:
            print("Es verano")
        else:
            print("Es otoño")
    
    if (mes == "abril" or mes == "mayo") and dia <=31:
        print("Es otoño")
    elif mes == "junio":
        if dia <= 20:
            print("Es otoño")
        else:
            print("Es invierno")
    
    if (mes == "julio" or mes == "agosto") and dia <=31:
        print("Es invierno")
    elif mes == "septiembre":
        if dia <= 20:
            print("Es invierno")
        else:
            print("Es primavera")
    
    if (mes == "octubre" or mes == "noviembre") and dia <=31:
        print("Es primavera")

elif hemisferio == "N" or hemisferio == "n":
    if (mes == "enero" or mes == "febrero") and dia <=31:
        print("Es invierno")
    elif mes == "diciembre":
        if dia >= 21:
            print("Es invierno")
        else:
            print("Es otoño")
    elif mes == "marzo":
        if dia <= 20:
            print("Es invierno")
        else:
            print("Es primavera")
    
    if (mes == "abril" or mes == "mayo") and dia <=31:
        print("Es primavera")
    elif mes == "junio":
        if dia <= 20:
            print("Es primavera")
        else:
            print("Es verano")
    
    if (mes == "julio" or mes == "agosto") and dia <=31:
        print("Es verano")
    elif mes == "septiembre":
        if dia <= 20:
            print("Es verano")
        else:
            print("Es otoño")
    
    if (mes == "octubre" or mes == "noviembre") and dia <=31:
        print("Es otoño")