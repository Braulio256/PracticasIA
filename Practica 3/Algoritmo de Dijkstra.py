# Importa la biblioteca heapq para usar colas de prioridad (mínimo en la raíz)
import heapq
# Importa NetworkX para manipular grafos
import networkx as nx
# Importa matplotlib para graficar
import matplotlib.pyplot as plt


# Función que implementa el algoritmo de Dijkstra mostrando los pasos
def dijkstra_con_pasos(grafo, inicio):
    # Inicializa todas las distancias como infinitas
    distancias = {nodo: float('inf') for nodo in grafo}
    # La distancia del nodo de inicio es cero
    distancias[inicio] = 0
    # Cola de prioridad con la tupla (distancia, nodo)
    cola_prioridad = [(0, inicio)]
    # Conjunto para llevar registro de nodos visitados
    visitados = set()
    # Diccionario para guardar los caminos más cortos
    caminos = {nodo: [] for nodo in grafo}
    # El camino al nodo de inicio comienza en sí mismo
    caminos[inicio] = [inicio]
    # Contador de pasos para impresión
    paso = 1

    print("=== Simulador de Dijkstra (Paso a Paso) ===")
    print(f"Inicio: Nodo {inicio}\n")

    # Mientras haya elementos en la cola de prioridad
    while cola_prioridad:
        print(f"--- Paso {paso} ---")
        # Extrae el nodo con menor distancia acumulada
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        # Si ya fue visitado, se omite
        if nodo_actual in visitados:
            print(f"El nodo {nodo_actual} ya fue visitado. Se omite.")
            paso += 1
            continue

        # Muestra el nodo actual y su distancia acumulada
        print(f"Nodo actual: {nodo_actual} (Distancia acumulada: {distancia_actual})")
        # Marca el nodo como visitado
        visitados.add(nodo_actual)

        # Revisa todos los vecinos del nodo actual
        for vecino, peso in grafo[nodo_actual].items():
            # Calcula la distancia si se pasa por el nodo actual
            distancia = distancia_actual + peso
            # Si esta ruta es más corta que la previamente conocida
            if distancia < distancias[vecino]:
                print(f"  Mejor camino encontrado a {vecino}: {distancia} (antes {distancias[vecino]})")
                # Actualiza la distancia mínima
                distancias[vecino] = distancia
                # Agrega el vecino a la cola de prioridad
                heapq.heappush(cola_prioridad, (distancia, vecino))
                # Guarda el nuevo camino
                caminos[vecino] = caminos[nodo_actual] + [vecino]

        # Muestra el estado actual de distancias y cola
        print(f"Distancias actualizadas: {distancias}")
        print(f"Cola de prioridad: {cola_prioridad}\n")
        # Incrementa el contador de pasos
        paso += 1

    # Devuelve las distancias mínimas y los caminos más cortos
    return distancias, caminos


# Función para dibujar el grafo y resaltar los caminos más cortos
def dibujar_grafo(grafo, caminos, inicio):
    # Crea un grafo dirigido
    G = nx.DiGraph()
    # Listas para los colores de nodos y aristas
    colores_nodos = []
    colores_aristas = []

    # Añade nodos y aristas con pesos al grafo
    for nodo in grafo:
        G.add_node(nodo)
        for vecino, peso in grafo[nodo].items():
            G.add_edge(nodo, vecino, weight=peso)

    # Determina el color de cada nodo
    for nodo in G.nodes():
        if nodo == inicio:
            colores_nodos.append('red')  # Nodo de inicio en rojo
        elif nodo in caminos and caminos[nodo]:
            colores_nodos.append('lightgreen')  # Nodos alcanzados en verde claro
        else:
            colores_nodos.append('lightblue')  # Nodos no alcanzados en azul claro

    edge_colors = []  # Colores para las aristas

    # Determina qué aristas están en los caminos más cortos
    for u, v in G.edges():
        camino_valido = False
        for nodo in caminos:
            if len(caminos[nodo]) >= 2:
                for i in range(len(caminos[nodo]) - 1):
                    if caminos[nodo][i] == u and caminos[nodo][i + 1] == v:
                        camino_valido = True
                        break
        # Aristas en camino corto se pintan de verde, el resto de gris
        edge_colors.append('green' if camino_valido else 'gray')

    # Calcula posiciones para los nodos
    pos = nx.spring_layout(G)
    # Dibuja el grafo con los colores y flechas
    nx.draw(G, pos, with_labels=True, node_color=colores_nodos, edge_color=edge_colors, width=2, arrows=True)
    # Agrega etiquetas a las aristas con sus pesos
    etiquetas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)
    # Título del gráfico
    plt.title(f"Caminos más cortos desde {inicio}")
    # Muestra el gráfico
    plt.show()


# Diccionario que representa el grafo con nodos y pesos
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Nodo inicial del algoritmo de Dijkstra
inicio = 'A'
# Ejecuta Dijkstra y obtiene distancias y caminos
distancias, caminos = dijkstra_con_pasos(grafo, inicio)

# Imprime los resultados finales
print("\n=== Resultados Finales ===")
for nodo in distancias:
    print(f"Nodo {nodo}: Distancia = {distancias[nodo]}, Camino = {' -> '.join(caminos[nodo])}")

# Dibuja el grafo con los caminos más cortos resaltados
dibujar_grafo(grafo, caminos, inicio)
