import random


def generar_archivo(nombre, tamano):
    """Genera un archivo con números aleatorios."""
    with open(nombre, 'w') as f:
        for _ in range(tamano):
            f.write(f"{random.randint(1, 1000)}\n")


def leer_bloque(archivo, tamano_bloque):
    """Lee un bloque de datos del archivo."""
    bloque = []
    for _ in range(tamano_bloque):
        linea = archivo.readline()
        if not linea:
            break
        bloque.append(int(linea))
    return bloque


def mezcla_directa(archivo_entrada, archivo_salida, tamano_bloque):
    """Implementación básica de Straight Merging."""
    # Fase 1: Ordenamiento interno de bloques
    with open(archivo_entrada, 'r') as f_in:
        bloques = []
        while True:
            bloque = leer_bloque(f_in, tamano_bloque)
            if not bloque:
                break
            bloque.sort()  # Ordenamos el bloque en memoria
            bloques.append(bloque)

    # Fase 2: Mezcla de bloques ordenados
    with open(archivo_salida, 'w') as f_out:
        while bloques:
            # Tomamos el primer elemento de cada bloque y escribimos el menor
            menores = []
            for bloque in bloques:
                if bloque:
                    menores.append(bloque[0])

            if not menores:
                break

            min_val = min(menores)
            f_out.write(f"{min_val}\n")

            # Eliminamos el mínimo de su bloque
            for i in range(len(bloques)):
                if bloques[i] and bloques[i][0] == min_val:
                    bloques[i].pop(0)
                    if not bloques[i]:
                        bloques.pop(i)
                    break


# Ejemplo de uso
if __name__ == "__main__":
    # Generamos un archivo de prueba con 100 números
    archivo_entrada = "datos.txt"
    archivo_salida = "datos_ordenados.txt"
    generar_archivo(archivo_entrada, 100)

    # Aplicamos Straight Merging con bloques de 10 elementos
    mezcla_directa(archivo_entrada, archivo_salida, 10)

    print(f"Archivo original: {archivo_entrada}")
    print(f"Archivo ordenado: {archivo_salida}")