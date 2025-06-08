class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


def insertar(raiz, valor):
    if raiz is None:
        return Nodo(valor)
    if valor < raiz.valor:
        raiz.izquierda = insertar(raiz.izquierda, valor)
    else:
        raiz.derecha = insertar(raiz.derecha, valor)
    return raiz


def recorrido_en_orden(raiz, resultado):
    if raiz:
        recorrido_en_orden(raiz.izquierda, resultado)
        resultado.append(raiz.valor)
        recorrido_en_orden(raiz.derecha, resultado)


def tree_sort(lista):
    if not lista:
        return lista

    raiz = None
    for item in lista:
        raiz = insertar(raiz, item)

    resultado = []
    recorrido_en_orden(raiz, resultado)
    return resultado


# Ejemplo de uso
if __name__ == "__main__":
    datos = [10, 5, 15, 3, 7, 12, 20]
    print("Lista original:", datos)

    datos_ordenados = tree_sort(datos)
    print("Lista ordenada:", datos_ordenados)