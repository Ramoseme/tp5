#ejercicio 1
def redondear(numero):
    entero_menor = int(numero)
    decimal = numero - entero_menor

    if decimal > 0.5:
        return entero_menor + 1
    else:
        return entero_menor

numero_decimal = float(input("Ingresa un número decimal: "))

resultado = redondear(numero_decimal)
print(f"El número {numero_decimal} redondeado es: {resultado}")

#ejercicio 2
