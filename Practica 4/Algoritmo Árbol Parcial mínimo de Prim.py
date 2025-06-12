# Importa la biblioteca heapq para usar una cola de prioridad (montículo mínimo)
import heapq

# Importa pyplot para graficar
import matplotlib.pyplot as plt

# Importa NetworkX para manipular grafos
import networkx as nx

def dibujar_resultado_final(G, pos, aristas_mst):
    """
    Dibuja solo el resultado final del MST sobre el grafo completo.
    """
    # Crea una nueva figura para el gráfico
    plt.figure(figsize=(6, 5))
    # Establece el título del gráfico
    plt.title("Resultado final: Árbol de expansión mínima (Prim)")

    # Dibuja todos los nodos y aristas del grafo original con colores base
    nx.draw(G, pos, with_labels=True, node_color='lightgray', edge_color='gray',
            node_size=700, font_weight='bold')

    # Extrae solo las aristas del árbol de expansión mínima (MST)
    mst_edges = [(u, v) for u, v, _ in aristas_mst]
    # Extrae etiquetas de pesos para las aristas MST
    edge_labels = {(u, v): w for u, v, w in aristas_mst}
    # Dibuja las aristas del MST en color verde
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='green', width=2.5)
    # Dibuja las etiquetas (pesos) de las aristas del MST
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,
                                 font_color='green', font_weight='bold')

    # Muestra el gráfico
    plt.show()

def prim_con_terminal_y_resultado_final(adj_matrix):
    # Número de vértices en el grafo
    num_vertices = len(adj_matrix)
    # Lista para marcar los vértices ya visitados
    visited = [False] * num_vertices
    # Inicializa los costos con infinito
    cost = [float('inf')] * num_vertices
    # Almacena el nodo padre en el MST
    edge_to = [-1] * num_vertices
    # El costo para el primer vértice es cero
    cost[0] = 0
    # Cola de prioridad: (costo, nodo)
    pq = [(0, 0)]
    # Lista para guardar las aristas del MST
    mst_edges = []
    # Peso total del MST
    total_weight = 0
    # Contador de pasos para mostrar en consola
    paso = 1

    # Crea el grafo usando NetworkX
    G = nx.Graph()
    for u in range(num_vertices):
        for v in range(u + 1, num_vertices):
            if adj_matrix[u][v] != 0:
                # Agrega la arista con peso al grafo
                G.add_edge(u, v, weight=adj_matrix[u][v])
    # Calcula la posición de los nodos para la visualización
    pos = nx.spring_layout(G, seed=42)

    # Bucle principal del algoritmo de Prim
    while pq:
        # Extrae el nodo con menor costo
        weight_u, u = heapq.heappop(pq)
        # Si ya fue visitado, se omite
        if visited[u]:
            continue

        # Marca el nodo como visitado
        visited[u] = True
        # Suma el peso al total del MST
        total_weight += weight_u

        # Si no es el primer nodo, se agrega la arista al MST
        if edge_to[u] != -1:
            mst_edges.append((edge_to[u], u, weight_u))
            print(f"\n🟢 Paso {paso}: Se añade la arista ({edge_to[u]}, {u}) con peso {weight_u}")
        else:
            print(f"\n🟡 Paso {paso}: Comienza desde el vértice {u}")

        # Muestra el estado actual
        print(f"   ⮕ Vértice actual: {u}")
        print(f"   ⮕ Costos actuales: {cost}")
        print(f"   ⮕ Visitados: {visited}")
        paso += 1

        # Revisa los vecinos del nodo actual
        for v, weight_uv in enumerate(adj_matrix[u]):
            # Si hay una arista, el nodo no fue visitado y el peso es menor al actual
            if weight_uv > 0 and not visited[v] and weight_uv < cost[v]:
                # Actualiza el costo y el nodo padre
                cost[v] = weight_uv
                edge_to[v] = u
                # Agrega el nuevo costo a la cola de prioridad
                heapq.heappush(pq, (weight_uv, v))
                print(f"       ✅ Se actualiza el costo para v={v}: nuevo padre = {u}, peso = {weight_uv}")

    # Al finalizar, se muestra el MST en consola
    print("\n✅ Árbol de Expansión Mínima completo:")
    for u, v, w in mst_edges:
        print(f"   ({u}, {v})  peso = {w}")
    print(f"Peso total = {total_weight}")

    # Llama a la función para graficar el resultado final
    dibujar_resultado_final(G, pos, mst_edges)

# Matriz de adyacencia del grafo de prueba
adj_matrix = [
    [ 0, 2, 0, 6, 0],  # Nodo 0
    [ 2, 0, 3, 8, 5],  # Nodo 1
    [ 0, 3, 0, 0, 7],  # Nodo 2
    [ 6, 8, 0, 0, 9],  # Nodo 3
    [ 0, 5, 7, 9, 0]   # Nodo 4
]

# Ejecuta el algoritmo de Prim con visualización y pasos
prim_con_terminal_y_resultado_final(adj_matrix)
