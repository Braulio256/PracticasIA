def ordenamiento_seleccion(lista):
    # Recorremos toda la lista
    for i in range(len(lista)):
        # Encontramos el índice del mínimo elemento en la parte sin ordenar
        indice_minimo = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j

        # Intercambiamos el elemento mínimo encontrado con el primer elemento sin ordenar
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]


# Ejemplo de uso
if __name__ == "__main__":
    datos = [12, 4, 15, 13, 2, 6, 8, 1]
    print("Lista original:", datos)

    ordenamiento_seleccion(datos)
    print("Lista ordenada:", datos)