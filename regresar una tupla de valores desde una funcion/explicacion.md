# Ejercicio: Retorno de Tuplas desde Funciones

Este script muestra una característica potente de Python: la capacidad de devolver múltiples valores desde una sola función utilizando tuplas.

## 💡 ¿Qué aprendí con esto?
Aprendí que una función no está limitada a devolver un solo dato. Puede devolver varios, y puedo capturarlos todos en una sola línea mediante el **desempaquetado de variables**.

## 📝 Funcionamiento
1. La función `personaMayus` toma los datos, convierte el texto a mayúsculas y los devuelve agrupados.
2. El programa principal captura esos valores sobrescribiendo las variables originales.

```python
# Así se atrapan múltiples valores al mismo tiempo:
nombre, edad, apellido = personaMayus(nombre, edad, apellido)
