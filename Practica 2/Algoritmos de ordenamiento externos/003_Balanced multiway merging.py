import os
import random
import heapq
from itertools import islice


def generar_archivo(nombre, tamano):
    """Genera un archivo con números aleatorios."""
    with open(nombre, 'w') as f:
        for _ in range(tamano):
            f.write(f"{random.randint(1, 1000)}\n")


def dividir_y_ordenar(archivo_entrada, tamano_bloque, M):
    """Divide el archivo en M bloques ordenados."""
    bloques = []
    with open(archivo_entrada, 'r') as f:
        while True:
            bloque = [int(linea.strip()) for linea in islice(f, tamano_bloque)]
            if not bloque:
                break
            bloque.sort()
            bloques.append(bloque)

    # Asegurarse de tener exactamente M bloques
    while len(bloques) < M:
        bloques.append([])

    return bloques


def mezcla_multicamino(archivos_entrada, archivo_salida):
    """Realiza la mezcla multicamino balanceada."""
    # Filtrar archivos no vacíos
    archivos_validos = [archivo for archivo in archivos_entrada if
                        os.path.exists(archivo) and os.path.getsize(archivo) > 0]

    if not archivos_validos:
        open(archivo_salida, 'w').close()  # Crear archivo vacío
        return

    handles = []
    heap = []

    try:
        # Abrir archivos y preparar heap
        for i, archivo in enumerate(archivos_validos):
            handle = open(archivo, 'r')
            handles.append(handle)
            linea = handle.readline()
            if linea:
                heapq.heappush(heap, (int(linea.strip()), i))

        # Escribir archivo de salida
        with open(archivo_salida, 'w') as f_out:
            while heap:
                valor, idx = heapq.heappop(heap)
                f_out.write(f"{valor}\n")

                # Leer siguiente elemento
                linea = handles[idx].readline()
                if linea:
                    heapq.heappush(heap, (int(linea.strip()), idx))

    finally:
        # Cerrar todos los handles
        for handle in handles:
            handle.close()


def balanced_multiway_merge(archivo_entrada, archivo_salida, M=3, tamano_bloque=1000):
    """Algoritmo completo de Balanced Multiway Merging."""
    # Fase 1: Crear M runs iniciales ordenados
    bloques = dividir_y_ordenar(archivo_entrada, tamano_bloque, M)

    # Escribir bloques a archivos temporales
    temporales = []
    for i, bloque in enumerate(bloques):
        if not bloque:
            continue  # Saltar bloques vacíos

        nombre_temp = f"temp_{i}.txt"
        with open(nombre_temp, 'w') as temp:
            for num in bloque:
                temp.write(f"{num}\n")
        temporales.append(nombre_temp)

    # Fase 2: Mezcla multicamino iterativa
    nivel = 0
    while len(temporales) > 1:
        nuevo_temp = f"temp_mezcla_{nivel}.txt"
        mezcla_multicamino(temporales[:M], nuevo_temp)

        # Eliminar solo los archivos temporales que existen
        for archivo in temporales[:M]:
            try:
                if os.path.exists(archivo):
                    os.remove(archivo)
            except:
                pass

        # Actualizar lista de temporales
        temporales = [nuevo_temp] + temporales[M:]
        nivel += 1

    # Renombrar el último temporal como salida
    if temporales:
        if os.path.exists(archivo_salida):
            os.remove(archivo_salida)
        os.rename(temporales[0], archivo_salida)


# Ejemplo de uso
if __name__ == "__main__":
    archivo_entrada = "datos_grandes.txt"
    archivo_salida = "datos_grandes_ordenados.txt"

    # Generar archivo de prueba (10,000 números)
    if not os.path.exists(archivo_entrada):
        generar_archivo(archivo_entrada, 10000)

    # Ejecutar con M=3 (3-way merge)
    balanced_multiway_merge(archivo_entrada, archivo_salida, M=3, tamano_bloque=1000)

    print(f"Archivo original: {archivo_entrada}")
    print(f"Archivo ordenado: {archivo_salida}")