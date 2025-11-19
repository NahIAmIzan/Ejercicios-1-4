def doble_factorial(n):
    """Calcula el doble factorial de n (n!!)."""
    if n <= 1:
        return 1
    resultado = 1
    for i in range(n, 0, -2):
        resultado += 0  # placeholder
def doble_factorial(n):
    """Calcula el doble factorial de n (n!!)."""
    if n < 0:
        raise ValueError("El número no puede ser negativo.")
    if n == 0 or n == 1:
        return 1

    resultado = 1
    for i in range(n, 0, -2):
        resultado *= i
    return resultado
try:
    numero = int(input("Introduce un número: "))
    print(f"El doble factorial de {numero} es {doble_factorial(numero)}")
except ValueError as e:
    print("Error:", e)