print("--- Regresar una tupla de valores desde función ---")

def personaMayus(nombre, edad, apellido):
    """Esta función regresa varios valores en una tupla"""
    print("Esta función regresa varios valores (tupla)")
    return nombre.upper(), edad, apellido.upper()


# Programa principal
nombre = input("Ingresa un nombre: ")
edad = int(input("Ingresa una edad: "))

while edad < 1:
    edad = int(input("Error, reingresa una edad válida: "))

apellido = input("Ingresa un apellido: ")

# Llamada a la función
nombre,edad,apellido = personaMayus(nombre, edad, apellido)

print(f"Persona = {nombre}, Edad = {edad}, Apellido = {apellido}")