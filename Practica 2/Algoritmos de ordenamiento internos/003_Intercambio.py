def ordenamiento_intercambio_optimizado(lista):
    n = len(lista)

    for i in range(n):
        intercambio = False

        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True

        # Si no hubo intercambios, la lista ya está ordenada
        if not intercambio:
            break


# Ejemplo de uso
if __name__ == "__main__":
    datos = [12, 4, 15, 13, 2, 6, 8, 1]
    print("Lista original:", datos)

    ordenamiento_intercambio_optimizado(datos)
    print("Lista ordenada:", datos)