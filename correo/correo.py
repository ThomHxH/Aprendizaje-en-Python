nombre=input("ingresa tu nombre")
empresa=input("ingresa el nombre de tu empresa")
dominio=input("ingresa el nombre del dominio")
nombre=nombre.replace(" ",".")
nombre=nombre.lower()
gmail=nombre+"@"+empresa+dominio
gmail=gmail.strip()
print(gmail)