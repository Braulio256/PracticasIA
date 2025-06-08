import random

def generar_archivo_entrada(nombre_archivo, cantidad_numeros, rango_min=1, rango_max=100):
    """
    Genera un archivo con números aleatorios, uno por línea.

    :param nombre_archivo: Nombre del archivo a generar
    :param cantidad_numeros: Número total de valores aleatorios
    :param rango_min: Valor mínimo posible
    :param rango_max: Valor máximo posible
    """
    with open(nombre_archivo, 'w') as f:
        for _ in range(cantidad_numeros):
            numero = random.randint(rango_min, rango_max)
            f.write(f"{numero}\n")

def generar_corridas_iniciales(archivo_entrada, tam_memoria, archivos_salida):
    """
    Divide los datos del archivo de entrada en corridas ordenadas y
    las distribuye alternadamente entre los archivos de salida.

    :param archivo_entrada: Nombre del archivo con los datos desordenados
    :param tam_memoria: Tamaño de la memoria disponible (número máximo de elementos a cargar)
    :param archivos_salida: Lista con los nombres de archivos para distribuir las corridas
    """
    with open(archivo_entrada, 'r') as entrada:
        fin_archivo = False
        indice_salida = 0  # Para alternar entre archivos de salida

        while not fin_archivo:
            datos = []
            for _ in range(tam_memoria):
                linea = entrada.readline()
                if not linea:
                    fin_archivo = True
                    break
                datos.append(int(linea.strip()))

            if datos:
                datos.sort()  # Ordenamos la corrida en memoria
                archivo_destino = archivos_salida[indice_salida]

                with open(archivo_destino, 'a') as salida:
                    salida.write('\n'.join(map(str, datos)) + '\n')

                indice_salida = (indice_salida + 1) % len(archivos_salida)


# === CONFIGURACIÓN GENERAL ===
archivo_entrada = 'input.txt'
archivos_salida = ['run1.txt', 'run2.txt']
tam_memoria = 5            # Tamaño de la memoria simulada
total_numeros = 20         # Total de números aleatorios a generar

# Paso 1: Generar archivo de entrada aleatorio
generar_archivo_entrada(archivo_entrada, total_numeros)

# Paso 2: Limpiar archivos de salida antes de escribir en ellos
for archivo in archivos_salida:
    open(archivo, 'w').close()

# Paso 3: Generar corridas iniciales
generar_corridas_iniciales(archivo_entrada, tam_memoria, archivos_salida)

print("Archivos de entrada y corridas distribuidas generados correctamente.")
