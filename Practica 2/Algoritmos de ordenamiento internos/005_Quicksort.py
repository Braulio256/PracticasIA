def quicksort(lista):
    # Caso base: si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(lista) <= 1:
        return lista

    pivote = lista[len(lista) // 2]  # Elegimos el pivote (puede ser el medio, el primero o el último)
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]

    # Ordenamos recursivamente y combinamos
    return quicksort(menores) + iguales + quicksort(mayores)


# Ejemplo de uso
if __name__ == "__main__":
    datos = [10, 5, 2, 3, 9, 8, 7, 1, 6, 4]
    print("Lista original:", datos)

    datos_ordenados = quicksort(datos)
    print("Lista ordenada:", datos_ordenados)