lista = []

def menu():
    print("A) Agregar un numero a la lista")
    print("B) Agregar un numero a la lista segun la posición")
    print("C) Ver longitud de la lista")
    print("D) Eliminar el ultimo numero")
    print("E) Eliminar un numero")
    print("F) Contar repeticiones de un numero")
    print("G) Salir")
    
def seleccionarOpcion(opcion):
    print("\n")
    opcion = opcion.upper()
    
    if opcion == "A":
        numero == int(input("Ingresa un numero"))
        lista.append(numero)
    elif opcion == "B":
        posicion =int(input("Ingresa la posicion"))
        numero = int(input("Ingresa el numero"))
        lista.insert(posicion, numero)
    elif opcion == "C":
        print("La longitud de la lista es de {0}".format(len(lista)))
    elif opcion == "D":
        numero = lista.pop()
        print("Se borro el numero {0}".format(numero))
    elif opcion == "E":
        print("De la lista que numero desea borrar", lista)
        numero = int(input("Ingresa el numero a borrar: "))
        lista.remove(numero)
        print("Se borro {0}".format(numero))
    elif opcion == "F":
        numero = int(input("Ingresa el numero que se desea contar"))
        total = lista.count(numero)
        print("En la lista {0} se repite {1}".format(numero, total))
    elif opcion == "G":
        print("Gracias por usar nuestro programa")
    else:
        print("Esta opcion no es valida :()")
        
while True: 
    menu()
    
    opcion = input("Ingresa una opcion A-G: ")
    seleccionarOpcion(opcion)
    
    if opcion.upper() == "G":
        break