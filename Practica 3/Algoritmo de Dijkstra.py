import heapq
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra_con_pasos(grafo, inicio):
    # Inicialización
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    cola_prioridad = [(0, inicio)]
    visitados = set()
    caminos = {nodo: [] for nodo in grafo}
    caminos[inicio] = [inicio]
    paso = 1

    print("=== Simulador de Dijkstra (Paso a Paso) ===")
    print(f"Inicio: Nodo {inicio}\n")

    while cola_prioridad:
        print(f"--- Paso {paso} ---")
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if nodo_actual in visitados:
            print(f"El nodo {nodo_actual} ya fue visitado. Se omite.")
            paso += 1
            continue

        print(f"Nodo actual: {nodo_actual} (Distancia acumulada: {distancia_actual})")
        visitados.add(nodo_actual)

        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                print(f"  Mejor camino encontrado a {vecino}: {distancia} (antes {distancias[vecino]})")
                distancias[vecino] = distancia
                heapq.heappush(cola_prioridad, (distancia, vecino))
                caminos[vecino] = caminos[nodo_actual] + [vecino]

        print(f"Distancias actualizadas: {distancias}")
        print(f"Cola de prioridad: {cola_prioridad}\n")
        paso += 1

    return distancias, caminos


def dibujar_grafo(grafo, caminos, inicio):
    G = nx.DiGraph()
    colores_nodos = []
    colores_aristas = []

    # Añadir nodos y aristas
    for nodo in grafo:
        G.add_node(nodo)
        for vecino, peso in grafo[nodo].items():
            G.add_edge(nodo, vecino, weight=peso)

    # Colorear nodos y aristas del camino más corto
    for nodo in G.nodes():
        if nodo == inicio:
            colores_nodos.append('red')  # Nodo inicio
        elif nodo in caminos and caminos[nodo]:
            colores_nodos.append('lightgreen')  # Nodos alcanzados
        else:
            colores_nodos.append('lightblue')

    edge_colors = []
    for u, v in G.edges():
        camino_valido = False
        for nodo in caminos:
            if len(caminos[nodo]) >= 2:
                for i in range(len(caminos[nodo]) - 1):
                    if caminos[nodo][i] == u and caminos[nodo][i + 1] == v:
                        camino_valido = True
                        break
        edge_colors.append('green' if camino_valido else 'gray')

    # Dibujar el grafo
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=colores_nodos, edge_color=edge_colors, width=2, arrows=True)
    etiquetas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)
    plt.title(f"Caminos más cortos desde {inicio}")
    plt.show()


# Ejemplo de grafo
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

inicio = 'A'
distancias, caminos = dijkstra_con_pasos(grafo, inicio)

print("\n=== Resultados Finales ===")
for nodo in distancias:
    print(f"Nodo {nodo}: Distancia = {distancias[nodo]}, Camino = {' -> '.join(caminos[nodo])}")

dibujar_grafo(grafo, caminos, inicio)