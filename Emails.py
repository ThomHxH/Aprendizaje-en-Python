print("---Generador de Emails---")

nombre = input("Ingresa tu nombre: ")
empresa = input("Ingresa el nombre de tu empresa: ")
dominio = input("Ingresa el nombre del dominio: ")
nombre = nombre.replace(" ", ".").lower()

emailFinal = nombre + "@" + empresa + dominio
emailFinal = email_final.strip()

print(f"Tu email generado es: {email_final}")
