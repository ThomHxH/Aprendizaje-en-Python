# Ejercicio: Funciones con Argumentos por Nombre

Este es un script simple en Python para practicar el concepto de **Keyword Arguments** (Argumentos por Nombre).

## 💡 ¿Qué aprendí con esto?
La idea principal de este ejercicio es demostrar que al llamar a una función, no importa el orden de los parámetros si especificamos sus nombres explícitamente.

## 📝 Funcionamiento
1. El programa pide el **nombre**, **edad** y **apellido**.
2. Valida que la edad no sea menor a 1 usando un ciclo `while`.
3. Llama a la función `imprimirPersona` enviando los datos en un orden diferente al de la definición, demostrando que Python lo ordena solo.

```python
# Ejemplo de la llamada en el código:
imprimirPersona(edad=edad, nombre=nombre, apellido=apellido)
