def radix_sort(lista):
    # Encontramos el número máximo para saber el número de dígitos
    max_num = max(lista)
    exp = 1  # Empezamos por el dígito menos significativo (unidades)

    while max_num // exp > 0:
        counting_sort_por_digito(lista, exp)
        exp *= 10  # Pasamos al siguiente dígito (decenas, centenas, etc.)


def counting_sort_por_digito(lista, exp):
    n = len(lista)
    salida = [0] * n
    contador = [0] * 10  # Contador para dígitos del 0 al 9

    # Contamos la frecuencia de cada dígito
    for num in lista:
        digito = (num // exp) % 10
        contador[digito] += 1

    # Calculamos las posiciones finales
    for i in range(1, 10):
        contador[i] += contador[i - 1]

    # Construimos la lista de salida
    for i in range(n - 1, -1, -1):
        num = lista[i]
        digito = (num // exp) % 10
        salida[contador[digito] - 1] = num
        contador[digito] -= 1

    # Copiamos la salida a la lista original
    for i in range(n):
        lista[i] = salida[i]


# Ejemplo de uso
if __name__ == "__main__":
    datos = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Lista original:", datos)

    radix_sort(datos)
    print("Lista ordenada:", datos)