def mergesort(lista):
    # Caso base: si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(lista) <= 1:
        return lista

    # Dividimos la lista en dos mitades
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    # Ordenamos recursivamente cada mitad
    izquierda = mergesort(izquierda)
    derecha = mergesort(derecha)

    # Combinamos las mitades ordenadas
    return merge(izquierda, derecha)


def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    # Combinamos las listas ordenadas
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Añadimos los elementos restantes (si quedan)
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado


# Ejemplo de uso
if __name__ == "__main__":
    datos = [38, 27, 43, 3, 9, 82, 10]
    print("Lista original:", datos)

    datos_ordenados = mergesort(datos)
    print("Lista ordenada:", datos_ordenados)