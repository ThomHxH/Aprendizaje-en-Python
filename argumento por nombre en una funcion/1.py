print("--- Funcion con argumento por nombre---")
def imprimirPersona(nombre,edad,apellido):
    print(f"nombre={nombre},edad={edad},apellido={apellido}")
nombre = input("ingresa el nombre de la persona: ")
edad = int(input("ingresa la edad de la persona: "))
while edad < 1:
    edad = int(input("ingresa la edad de la persona: "))
apellido = input("ingrese el apellido de la persona: ")
imprimirPersona(edad=edad,nombre=nombre,apellido=apellido)