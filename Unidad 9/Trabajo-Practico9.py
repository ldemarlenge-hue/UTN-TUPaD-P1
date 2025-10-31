#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario

#Se define la función recursiva para calcular el factorial de un número
def factorial(n):
    #Caso base, para 0 devolver 1
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#Solicito al usuario un número    
num = int(input("Ingrese un número entero positivo: "))
#Validación
if num < 1:
    #Si ingresó un número negativo se imprime un mensaje
    print("El número debía ser un entero positivo")
else:
    #Sino se imprimen los factoriales desde 1 hasta ese número
    for i in range (1, num+1):
        print(factorial(i))


#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.

#Se crea la función recursiva de la serie de Fibonacci
def fibunacci_recursivo(posicion):
    #Caso base, para 0 devolver 0
    if posicion == 0:
        return 0
    #Caso base, para 1 devolver 1
    elif posicion == 1:
        return 1
    else:
        return fibunacci_recursivo(posicion-1) + fibunacci_recursivo(posicion-2)

#Se solicita la posición al usuario
num = int(input("Ingrese un la posición hasta la que desea calcular la Serie de Fibonacci: "))
#Se muestra toda la serie hasta la posición indicada
for i in range (num+1):
    print(f"En la posición {i} tenemos el valor de Fibonacci: {fibunacci_recursivo(i)}")


#3) Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula n^m = n * n^(m-1)
#Prueba esta función en un algoritmo general.

#Se crea la función
def potencia(base, exponente):
    #Caso Base: si el exponente es 0, el resultado es 1.
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

#Se crea el programa:
print("=== Calculadora de Potencia Recursiva ===")
#Se Solicita la base y el exponente al usuario
base = int(input("Ingrese la BASE (número entero): "))
exponente = int(input("Ingrese el EXPONENTE (entero no negativo): "))
#Se Valida que el exponente sea no negativo
if exponente < 0:
    print("Error: El exponente debe ser no negativo (0 o mayor).")
else:
    #Se Llama a la función recursiva
    resultado = potencia(base, exponente)  
    #Se muestra el resultado
    print("\n--- Resultado ---")
    print(f"La base ({base}) elevada al exponente ({exponente}) es:")
    print(f"{base}^{exponente} = {resultado}")


#4) Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.

#Se crea la función
def decimal_a_binario(n):
    #Caso base, tomamos que para 0 devuelva una cadena vacía
    if n == 0:
        return ""
    else:
        #divide por dos y toma el resto
        return decimal_a_binario(n // 2) + str(n % 2)

#Programa
print("Conversor de números decimales a binarios")    
numero = input("Ingresa un número decimal: ").strip()
if numero.isdigit():   #valida que sea decimal
    n = int(numero)
    if n < 0:
        print("Error: ingresa solo números positivos.")
    elif n == 0:
        print("El cero en número binario es 0 también")
    else:
        #Llamar a la función
        print(f"El número decimal {n} en Binario es {decimal_a_binario(n)}")
        #Confirmación rápida con la función bin() incorporada
        print(f"Confirmación (bin()): {bin(n)[2:]}")
else:
    print("Error: ingresa solo números decimales enteros.")


#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
#lo es.

#Se crea la función
def es_palindromo(palabra):
    #Caso Base, si la longitud es 0 o 1
    #Devuelve True porque una cadena vacía o con un solo carácter siempre es un palíndromo.
    if len(palabra) <= 1:
        return True
    #Caso Base, si los caracteres de los extremos no coinciden
    #La palabra no es un palíndromo, se termina la ejecución.
    if palabra[0] != palabra[-1]:
        return False
    #Si los extremos coinciden, se llama a la función con la sub-cadena que excluye 
    # el primer y último carácter.
    #[1:-1] toma la cadena desde el índice 1 (segundo carácter) hasta el índice -1 (excluyendo el último carácter).
    return es_palindromo(palabra[1:-1])

#Se crea el programa
print("=== Verificador de Palíndromos Recursivo ===")
#Se solicita al usuario una palabra
entrada = input("Ingresa una palabra (sin espacios ni tildes): ").lower().strip()
#Se muestra el resultado
print(f"La palabra '{entrada}' {'es un' if es_palindromo(entrada) else 'NO es un'} palíndromo.")


#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.

#Creamos la función
def suma_digitos(n):
    #Caso Base, si el número tiene un solo dígito (n < 10) o es 0.
    #La suma es el número mismo.
    if n < 10:
        return n
    #Suma el último dígito (n % 10) con la suma recursiva del resto del número (n // 10).
    return (n % 10) + suma_digitos(n // 10)

#Se crea el programa
print("=== Sumador de Dígitos Recursivo ===")
numero_str = input("Ingrese un número entero positivo: ").strip()
if not numero_str.isdigit():
    print("Error: Ingrese solo dígitos.")
else:
    n = int(numero_str)
    if n < 0:
        print("Error: El número debe ser positivo.")
    else:
        #Llamar a la función recursiva y mostrar el resultado
        print(f"La suma de los dígitos de {n} es: {suma_digitos(n)}")


#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
#último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la
#pirámide.

#Se crea la función
def contar_bloques(n):
    #Caso Base:, si el nivel es 1, solo se necesita 1 bloque.
    if n == 1:
        return 1
    #Sumar los bloques del nivel actual (n) con el total de bloques de los niveles superiores (n-1).
    return n + contar_bloques(n - 1)

#Se crea el programa
print("=== Pirámide de bloques ===")
#Solicitar el número de bloques en el nivel más bajo
n_str = input("Ingrese el número de bloques en el nivel más bajo (n): ").strip()
if not n_str.isdigit():
    print("Error: Ingrese solo dígitos.")
else:
    n = int(n_str)
    if n < 1:
        print("Error: El número de bloques debe ser un entero positivo (mínimo 1).")
    else:
        #Llamar a la función y mostrar resultados
        print(f"Para una pirámide con {n} bloques en la base, se necesitan un total de {contar_bloques(n)} bloques.")


#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número.

#Se crea la función
def contar_digito(numero, digito):
    #Caso Base, si el número es 0, no quedan más dígitos por analizar.
    if numero == 0:
        return 0
    #Obtener el último dígito del número
    ultimo_digito = numero % 10
    #Conteo del dígito actual: 
    #Comprobar si el último dígito es igual al dígito buscado. Suma 1 si coincide, 0 si no.
    conteo_actual = 1 if ultimo_digito == digito else 0
    #Sumar el conteo actual más el resultado de la función aplicada al resto del número.
    resto_del_numero = numero // 10
    return conteo_actual + contar_digito(resto_del_numero, digito)

#Se crea el programa
print("=== Contador de Dígitos Recursivo ===")
#Se solicitan las entradas
numero_str = input("Ingrese el número entero positivo (ej: 122452): ").strip()
digito_str = input("Ingrese el dígito a buscar (0-9): ").strip()
#Validaciones
if not numero_str.isdigit() or not digito_str.isdigit():
    print("Error: Ingrese solo dígitos en ambos campos.")
else:
    numero = int(numero_str)
    digito = int(digito_str)     
    if not (0 <= digito <= 9) or numero < 0:
        print("Error: Asegúrese que el número sea positivo y el dígito esté entre 0 y 9.")
    else:
        #Manejo especial para el caso del número 0, donde la recursión debe funcionar correctamente.
        if numero == 0:
            #Si el número es 0 y el dígito buscado es 0, la respuesta es 1.
            resultado = 1 if digito == 0 else 0
        else:
            #Llamar a la función recursiva y mostrar resultados
            print(f"El dígito {digito} aparece {contar_digito(numero,digito)} veces en el número {numero}.")