cadena = input("Ingrese una cadena que desee saber cuantas palabras tiene: ")

listaPalabras = cadena.split()
cantidadPalabras = len(listaPalabras)

print("La cadena tiene", cantidadPalabras, "palabras.")