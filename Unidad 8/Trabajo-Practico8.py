#1. Crear archivo inicial con productos: Crear un archivo de texto llamado
#productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

print("Archivo incial")
#Crear el archivo por primera vez:
with open("productos.txt", "w") as archivo:
    archivo.write("Naranja, 1200, 20\n")
    archivo.write("Banana, 1500, 50\n")
    archivo.write("Palta, 2200, 8\n")

#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
#formato:
#Producto: Lapicera | Precio: $120.5 | Cantidad: 30

#Se crea una lista vacía donde se irán guardando las líneas con el formato solicitado:
productos_list = []

#Se lee el archivo creado anteriormente
with open("productos.txt", "r") as archivo:
    #readlineas lee todas las lineas y devuelve una lista
    lineas = archivo.readlines()
    #Recorremos todas las lineas:
    for linea in lineas:
        partes = linea.strip().split(",") #se guarda en la lista partes gracias a split que usa las comas como separación
    
        #definimos el formato para mostrarlo, es un diccionario formado por 3 keys (nombre, precio y cantidad) y 3 valores (los que corresponden a esas keys)
        producto = {
                "nombre": partes[0], #de la lista partes, el elemento 0 corresponde al nombre del producto
                #Se debe convertir precio y cantidad a números (int en este caso)
                "precio": int(partes[1]), #de la lista partes, el elemento 1 corresponde al precio del producto
                "cantidad": int(partes[2]) #de la lista partes, el elemento 2 corresponde la cantidad del producto
            }
        #Agregamos el diccionario a la lista creada inicialmente:
        productos_list.append(producto)
            
        #Se muestra el producto en el formato solicitado:
        print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")

#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente.

#Se utiliza un ciclo while para evaluar si el usuario ingresó un dato correcto, de no ser así puede corregirlo
while True:
    nombre = input("Ingrese el nombre del nuevo producto: ").title().strip()
    #Validamos, si ingresó un número se le informa el error y vuelve a solicitarlo
    if nombre.isdigit():
        print("El nombre del producto no puede ser un número.")
    #sino continúa
    else:
        break

#Igualmente se utiliza un ciclo while para evaluar si el usuario ingresó un dato correcto, de no ser así puede corregirlo
while True:
    precio_str = input("Ingrese el precio: ").strip()
    #Validamos, si ingresó un número es correcto y avanza. Guarda el valor en la variable precio
    if precio_str.isdigit():
        precio = precio_str
        break
    #sino, se informa el error y vuelve a solicitar el precio
    else:
        print("El precio debe ser un número entero.")

#De nuevo se utiliza un ciclo while para evaluar si el usuario ingresó un dato correcto, de no ser así puede corregirlo
while True:
    cantidad_str = input("Ingrese la cantidad: ").strip()
    #Validamos, si ingresó un número es correcto y avanza. Guarda el valor en la variable cantidad
    if cantidad_str.isdigit():
        cantidad = cantidad_str
        break
    #sino, se informa el error y vuelve a solicitar la cantidad
    else:
        print("La cantidad debe ser un número entero.")

#Se guarda el nuevo producto en una nueva línea que será la que agregaremos:
nueva_linea = f"{nombre}, {precio}, {cantidad}\n"

#Se abre el archivo en modo 'a' para AGREGAR y no sobreescribir y agregamos la nueva línea
with open("productos.txt", "a") as archivo:
        archivo.write(nueva_linea)

#Se muestra el archivo actualizado con r y .read()
print("Archivo actualizado:")
with open("productos.txt", "r") as archivo:
    print(archivo.read())

#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
#una lista llamada productos, donde cada elemento sea un diccionario con claves:
#nombre, precio, cantidad.

#Se crea una lista denominada productos que será la que luego iremos completando
productos = []

#Se abre el archivo existente con r para leerlo
with open("productos.txt", "r") as archivo:
    #Se lee el archivo iterando sobre cada línea
    for linea in archivo:
        #Se guarda cada linea en la varibale partes
        #Se usa strip y split para transformar cada linea en una lista
        partes = linea.strip().split(",")
        
        #Se verifica que haya 3 partes en cada línea con if
        if len(partes) == 3:
            #si tenemos 3 partes guardamos cada elemento de la lista con la variable correspondiente
            nombre = partes[0]
            #A precio y cantidad hay que convertirlos a números enteros (int)
            precio = int(partes[1])
            cantidad = int(partes[2])
                
            #Se crea un diccionario con las claves especificadas
            producto = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
                }
                
            #Agregamos a la lista productos el diccionario que acabamos de crear
            productos.append(producto)
        #si no tenemos 3 partes mostramos un mensaje al usuario
        else:
            print(f"Advertencia: La línea '{linea.strip()}' no tiene el formato esperado (nombre,precio,cantidad).")


#Se muestra los productos actualizados con la estructura deseada
print(productos)

#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
#no existe, mostrar un mensaje de error.

print("Consultar un producto")
nombre = input("Ingrese el nombre del producto a consultar: ").strip().title()

#Se crea esta variable que nos ayudará en la validación:
encontrado = False

#Buscamos el producto en la lista productos creada anteriormete
for producto in productos:
    #Si el producto ingresado se encuentra en la lista, muestra los datos
    if producto['nombre'] == nombre:
        print(f"  Nombre: {producto['nombre']}")
        print(f"  Precio: ${producto['precio']}")
        print(f"  Cantidad: {producto['cantidad']}")
        
        #La variable encontrado pasa a ser verdadera y se cierra el bucle
        encontrado = True
        break
    
#Si se recorrió toda la lista y la bandera sigue en False es porque el producto no está en la lista
if not encontrado:
    #se le informa al usuario
    print(f"ERROR: El producto '{nombre}' no se encontró en el inventario.")

#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
#productos actualizados desde la lista.

#Se define una función para que cada vez que se la llame actualice y guarde el archivo txt
def guardar_productos_actualizados(productos):
    print("\nGuardando Productos Actualizados en el Archivo")
    
    #Se abre el archivo en modo 'w' (write), lo que SOBREESCRIBE el contenido
    with open("productos.txt", "w") as archivo:
        #Recorremos la lista de diccionarios productos la cual ya existe en el programa
        for producto in productos:
            #Formateamos el diccionario como una línea de texto: nombre, precio, cantidad\n
            linea = f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n"
                
            #Escribimos la línea en el archivo
            archivo.write(linea)
    #Se informa al usuario que el archivo se actualizó            
    print("Éxito: El archivo 'productos.txt' ha sido sobrescrito con la información actualizada.")

#Llamamos a la función para probarla
guardar_productos_actualizados(productos)

#Para verificar que funciona, abrimos e imprimimos el archivo
print("\nContenido de 'productos.txt' después de guardar")
with open("productos.txt", "r") as archivo:
    print(archivo.read())