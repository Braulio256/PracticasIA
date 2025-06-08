import os
import random
import heapq
from itertools import islice


def generar_archivo(nombre, tamano):
    """Genera un archivo con números aleatorios."""
    with open(nombre, 'w') as f:
        for _ in range(tamano):
            f.write(f"{random.randint(1, 1000)}\n")


def distribucion_fibonacci(M, num_runs):
    """Calcula la distribución óptima de runs usando secuencia Fibonacci."""
    fib = [1, 1]
    while fib[-1] < num_runs:
        fib.append(fib[-1] + fib[-2])

    distribucion = []
    remaining = num_runs
    for f in reversed(fib[1:]):
        if f <= remaining:
            distribucion.append(f)
            remaining -= f
    return distribucion


def crear_runs(archivo_entrada, tamano_bloque):
    """Divide el archivo en runs ordenados."""
    runs = []
    with open(archivo_entrada, 'r') as f:
        while True:
            bloque = [int(linea.strip()) for linea in islice(f, tamano_bloque)]
            if not bloque:
                break
            bloque.sort()
            runs.append(bloque)
    return runs


def polyphase_merge_sort(archivo_entrada, archivo_salida, M=3, tamano_bloque=1000):
    """Implementación del algoritmo Polyphase Merge Sort."""

    # Paso 1: Crear runs iniciales
    runs = crear_runs(archivo_entrada, tamano_bloque)
    num_runs = len(runs)

    if num_runs == 0:
        open(archivo_salida, 'w').close()
        return

    # Paso 2: Calcular distribución Fibonacci
    distribucion = distribucion_fibonacci(M, num_runs)
    while len(distribucion) < M:
        distribucion.append(0)

    # Paso 3: Distribuir runs en archivos temporales
    temporales = [f"temp_{i}.txt" for i in range(M)]
    for i in range(M):
        with open(temporales[i], 'w') as f:
            for _ in range(distribucion[i]):
                if runs:
                    for num in runs.pop(0):
                        f.write(f"{num}\n")

    # Paso 4: Fase de mezcla
    while True:
        # Determinar archivo de salida (el vacío)
        archivo_vacio = None
        for i, archivo in enumerate(temporales):
            if os.path.getsize(archivo) == 0:
                archivo_vacio = i
                break

        if archivo_vacio is None:
            break  # Todos los archivos tienen datos

        # Seleccionar archivos de entrada
        archivos_entrada = [temporales[i] for i in range(M) if i != archivo_vacio]

        # Mezclar
        with open(temporales[archivo_vacio], 'w') as f_out:
            # Abrir archivos de entrada
            handles = [open(archivo, 'r') for archivo in archivos_entrada]
            heap = []

            # Inicializar heap
            for i, handle in enumerate(handles):
                linea = handle.readline()
                if linea:
                    heapq.heappush(heap, (int(linea.strip()), i))

            # Mezcla
            while heap:
                valor, idx = heapq.heappop(heap)
                f_out.write(f"{valor}\n")

                # Leer siguiente elemento
                linea = handles[idx].readline()
                if linea:
                    heapq.heappush(heap, (int(linea.strip()), idx))

            # Cerrar handles
            for handle in handles:
                handle.close()

        # Verificar si terminamos
        archivos_con_datos = sum(1 for archivo in temporales if os.path.getsize(archivo) > 0)
        if archivos_con_datos == 1:
            break

    # Paso 5: Identificar archivo resultante
    for archivo in temporales:
        if os.path.getsize(archivo) > 0:
            if os.path.exists(archivo_salida):
                os.remove(archivo_salida)
            os.rename(archivo, archivo_salida)
            break

    # Limpieza
    for archivo in temporales:
        if os.path.exists(archivo):
            os.remove(archivo)


# Ejemplo de uso
if __name__ == "__main__":
    archivo_entrada = "datos_polyphase.txt"
    archivo_salida = "datos_ordenados_polyphase.txt"

    # Generar archivo de prueba (10,000 números)
    if not os.path.exists(archivo_entrada):
        generar_archivo(archivo_entrada, 10000)

    # Ejecutar Polyphase Merge Sort con 3 archivos temporales
    polyphase_merge_sort(archivo_entrada, archivo_salida, M=3, tamano_bloque=1000)

    print(f"Archivo original: {archivo_entrada}")
    print(f"Archivo ordenado: {archivo_salida}")