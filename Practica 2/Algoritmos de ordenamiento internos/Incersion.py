def ordenamiento_insercion(lista):
    # Recorremos la lista desde el segundo elemento hasta el final
    for i in range(1, len(lista)):
        # Elemento actual que vamos a insertar en su posición correcta
        elemento_actual = lista[i]
        # Posición del elemento anterior al actual
        j = i - 1

        # Movemos los elementos mayores que el elemento actual
        # una posición adelante de su posición actual
        while j >= 0 and elemento_actual < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1

        # Insertamos el elemento actual en su posición correcta
        lista[j + 1] = elemento_actual


# Ejemplo de uso
if __name__ == "__main__":
    datos = [12, 4, 15, 13, 2, 6, 8, 1]
    print("Lista original:", datos)

    ordenamiento_insercion(datos)
    print("Lista ordenada:", datos)