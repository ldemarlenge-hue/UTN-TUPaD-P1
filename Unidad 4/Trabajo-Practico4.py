#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

#Se resuelve con el ciclo for porque sé de antemano cuántas veces se va a repetir el ciclo.
#dentro de "range" se coloca 101 porque no incluye el valor final y queremos que se imprima el 100 inclusive.
#el valor de inicio no se coloca porque por defecto comienza en 0
for i in range(101):
    print(i)


#2)Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

#Solicito al usuario que ingrese un número y lo defino como string
numero=str(input("Ingrese un número:"))
#calculo su longitud
longitud = len(numero)

#Así el programa funciona y cumple con lo solicitado, pero solo se puede ingresar un número y el programa termina.
#Si quisiéramos que el usuario pueda seguir ingresando números cuantas veces quiera tengo que pensar en un ciclo while (porque no sé de antemano cuántos números se ingresarán)
#planteo una variable que funcione como bandera
CORTE = "*"
#como while evalúa la condición al final, puede que nunca se ejecute si ingresan el caracter de corte como primera opción
#por eso tengo que poner dentro y fuera del while la instrucción
numero=str(input("Ingrese un número(utilice " + CORTE + " para finalizar):"))
while numero != CORTE:
    longitud = len(numero)
    print(longitud)
    numero=str(input("Ingrese otro número(utilice " + CORTE + " para finalizar):"))


#3)Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

#Mensaje inicial al usuario
print("Ingrese dos números. Se hará la suma de los números enteros comprendidos entre ellos, excluyendo los números ingresados")
#Solicito dos números, los inicio como enteros
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
#defino una variable suma que inicio en 0
suma = 0
#Con un if evalúo si el primer número es menor que el segundo o viceversa
#Luego con un for tomo el rango correspondiente sin incluir los valores dados
#y voy sumando los números que hay entre ellos en la variable suma
if num2 > num1:
   for i in range(num1+1, num2):
        suma += i
        print(suma)
else:
    for i in range(num1-1, num2,-1):
        suma +=i
        print(suma)

#COMENTARIO: el programa funciona, pero me muestra en secuencia la suma progresiva de los números
#¿Cómo hago si sólo quiero que me muestre el total? Lo pensé y probé bastante y no lo conseguí
#Ejemplo si ingreso num1=1 y num2=5 me muestra: 2, luego 5, luego 9. Quiero que solo me muestre 9


#4)Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

#Inicio la variable suma en 0, es la que va a ir acumulando
suma = 0
#como while evalúa la condición al final, puede que nunca se ejecute si ingresan 0 como primera opción
#por eso tengo que poner dentro y fuera del while la instrucción
num = int(input("Ingrese el primer número (utilice 0 para finalizar): "))
#en while voy sumando los valores ingresados mientras sean distintos de 0
#si es 0 lo evalúo con un if y en ese caso muestro el acumulado
while num != 0:
    suma = suma + num
    num = int(input("Ingrese otro número (utilice 0 para finalizar): "))

    if num == 0:
        print(f"El acumulado de los números ingresados es {suma}")


#5)Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

#Función para crear números aleatorios: "random", con import la llamo para poder usarla
import random
#Doy las instrucciones al usuario para que sepa cómo jugar
print("El programa generará un número aleatorio entre 0 y 9.")
print("Usted debe adivinar el número generado y se le indicará cuántos intentos utilizó.")
#genero el número aleatorio y lo guardo en la variable "aleatorio"
aleatorio = random.randint(0, 9)
#pido que ingrese el número
num = int(input("El número es: "))
#en esta variable guardaré la cantidad de intentos realizados, empieza en 1 porque ya ingresó un valor
intentos = 1
#si el número que ingresa el usuario está entre 0 y 9 inclusive, ingresa al bucle
while num >= 0 and num <= 9:
#con if evalúo si el número ingresado es igual al aleatorio o no
    if num < aleatorio:
        print("Intenta con un número más alto")
        num = int(input("El número es: "))
        intentos += 1
    elif num > aleatorio:
        print("Intenta con un número más bajo")
        num = int(input("El número es: "))
        intentos += 1
    else:
        print(f"Usted adivinó el número en {intentos} intentos. El número era {num}")
        break
#en caso de que el usuario ingrese un número fuera del rango:
if num < 0 or num > 9:
    print("Debía ingresar un número entre 0 y 9, lo siento.")


#6)Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

#se resuelve de manera similar al pto. 1, con un ciclo for.
#La diferencia es que ahora queremos que se muestren solo los números pares y en orden decreciente.
#Para esto en range tenemos que especificar el valor de inicio que será 100, el valor final que será -1 
#(porque no lo incluye y yo quiero que se me muestre el 0) y el valor de actualización que para que sea
#decreciente será negativo y para que se muestren los pares será 2.
for i in range(100,-1,-2):
    print(i)


#7)Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

#Defino suma y la inicio en 0, será el que vaya acumulando los valores
suma = 0
#solicito al usuario el número final
num = int(input("Ingrese el número final: "))
#para obtener la suma desde 0 hasta el número ingresado por el usuario, utilizo un for y realizo la sumatoria
for i in range(0,num+1):
   suma += i
   print(suma)

#COMENTARIO:igual que para el pto. 3, ¿cómo hago si quiero mostrar sólo la suma total de todos los números?


#8)Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos.

#Defino la cantidad de números a ingresar, son 100
cant_numeros=100
#inicio las variables que necesito analizar en 0
pares = 0
impares = 0
negativos = 0
positivos = 0
#utilizo for porque sé que es una cantidad fija de números
#el rango lo comienzo en 1 y para que me incluya el valor final le sumo 1
#con cont le indico al usuario en qué pedido estamos solo para que sepa cuántos le faltan ingresar
for cont in range(1,cant_numeros+1):
    print("Ingrese número",(cont))
    num = int(input())
#con dos if evalúo si son par/impar y también si son positivos/negativos
    if num > max_numero:
        max_numero = num
        pos_max = cont
    elif num < min_numero:
        min_numero = num
        pos_min = cont
#finalmente muestro el resultado
print(f"Hubo {pares} números pares, {impares} números impares, {positivos} números positivos y {negativos} números negativos")


#9)Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. 

#Defino la cantidad de números a ingresar, son 100
cant_numeros=100
#inicio la variable que necesito analizar en 0
suma = 0
#utilizo for porque sé que es una cantidad fija de números
#el rango lo comienzo en 1 y para que me incluya el valor final le sumo 1
#con cont le indico al usuario en qué pedido estamos solo para que sepa cuántos le faltan ingresar
#los voy sumando
for cont in range(1,cant_numeros+1):
    print("Ingrese número",(cont))
    num = int(input())
    suma = suma + num
#la media es la suma de los números dividido la cantidad de números totales
print(f"La media de los valores ingresados es ", (suma/cant_numeros))


#10)Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

#Le pido al usuario el número a invertir
num = int(input("Ingrese un número: "))
#defino la variable que voy a usar para invertir el número y la inicio en 0
num_invertido = 0
#con el bucle while voy a ir desglosando el número mientras sea distinto de 0
while num != 0:
    #con esta variable obtengo el resido del cociente entre el número y 10, que será el último número
    digito = num % 10
    #multiplico el número invertido por 10 para mover el "cursor" hacia la izquierda
    num_invertido = num_invertido * 10
    #le sumo el digito obtenido a número invertido para ir formándolo
    num_invertido = num_invertido + digito
    #realizo la división entera entre el número y 10 para descartar el último dígito 
    #(que fue el obtenido en el primer renglón del while)
    #de esta manera el número se va a ir "acortando", decartando en cada vuelta el último
    #Se repite hasta que este valor de 0, quiere decir que llegamos al final y ya no ingresa en el ciclo 
    num = num // 10
#muestro el resultado
print("El número invertido es ", num_invertido)