import random


def generar_archivo(nombre, tamano):
    """Genera un archivo con números aleatorios."""
    with open(nombre, 'w') as f:
        for _ in range(tamano):
            f.write(f"{random.randint(1, 1000)}\n")


def obtener_runs(archivo):
    """Identifica runs naturales (secuencias ordenadas) en el archivo."""
    runs = []
    with open(archivo, 'r') as f:
        anterior = None
        run_actual = []

        for linea in f:
            num = int(linea.strip())
            if anterior is None or num >= anterior:
                run_actual.append(num)
            else:
                runs.append(run_actual)
                run_actual = [num]
            anterior = num

        if run_actual:
            runs.append(run_actual)

    return runs


def mezcla_natural(archivo_entrada, archivo_salida):
    """Implementación de Natural Merging Sort."""
    # Fase 1: Identificar runs naturales
    runs = obtener_runs(archivo_entrada)

    # Fase 2: Mezcla iterativa hasta tener un solo run
    while len(runs) > 1:
        nuevos_runs = []

        # Mezcla de runs por pares
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                mezclado = merge(runs[i], runs[i + 1])
                nuevos_runs.append(mezclado)
            else:
                nuevos_runs.append(runs[i])

        runs = nuevos_runs

    # Escribir resultado final
    with open(archivo_salida, 'w') as f_out:
        for num in runs[0]:
            f_out.write(f"{num}\n")


def merge(run1, run2):
    """Mezcla dos runs ordenados."""
    resultado = []
    i = j = 0

    while i < len(run1) and j < len(run2):
        if run1[i] <= run2[j]:
            resultado.append(run1[i])
            i += 1
        else:
            resultado.append(run2[j])
            j += 1

    resultado.extend(run1[i:])
    resultado.extend(run2[j:])

    return resultado


# Ejemplo de uso
if __name__ == "__main__":
    archivo_entrada = "datos_natural.txt"
    archivo_salida = "datos_natural_ordenados.txt"

    # Generar datos de prueba
    generar_archivo(archivo_entrada, 100)

    # Ordenar con Natural Merging
    mezcla_natural(archivo_entrada, archivo_salida)

    print(f"Archivo original: {archivo_entrada}")
    print(f"Archivo ordenado: {archivo_salida}")