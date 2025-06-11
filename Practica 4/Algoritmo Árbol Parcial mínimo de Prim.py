import heapq
import matplotlib.pyplot as plt
import networkx as nx

def dibujar_resultado_final(G, pos, aristas_mst):
    """
    Dibuja solo el resultado final del MST sobre el grafo completo.
    """
    plt.figure(figsize=(6, 5))
    plt.title("Resultado final: Árbol de expansión mínima (Prim)")

    # Dibujar todos los nodos y aristas del grafo original
    nx.draw(G, pos, with_labels=True, node_color='lightgray', edge_color='gray', node_size=700, font_weight='bold')

    # Dibujar aristas del MST
    mst_edges = [(u, v) for u, v, _ in aristas_mst]
    edge_labels = {(u, v): w for u, v, w in aristas_mst}
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='green', width=2.5)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='green', font_weight='bold')

    plt.show()

def prim_con_terminal_y_resultado_final(adj_matrix):
    num_vertices = len(adj_matrix)
    visited = [False] * num_vertices
    cost = [float('inf')] * num_vertices
    edge_to = [-1] * num_vertices
    cost[0] = 0
    pq = [(0, 0)]
    mst_edges = []
    total_weight = 0
    paso = 1

    # Crear grafo con networkx
    G = nx.Graph()
    for u in range(num_vertices):
        for v in range(u + 1, num_vertices):
            if adj_matrix[u][v] != 0:
                G.add_edge(u, v, weight=adj_matrix[u][v])
    pos = nx.spring_layout(G, seed=42)

    while pq:
        weight_u, u = heapq.heappop(pq)
        if visited[u]:
            continue

        visited[u] = True
        total_weight += weight_u

        if edge_to[u] != -1:
            mst_edges.append((edge_to[u], u, weight_u))
            print(f"\n🟢 Paso {paso}: Se añade la arista ({edge_to[u]}, {u}) con peso {weight_u}")
        else:
            print(f"\n🟡 Paso {paso}: Comienza desde el vértice {u}")

        print(f"   ⮕ Vértice actual: {u}")
        print(f"   ⮕ Costos actuales: {cost}")
        print(f"   ⮕ Visitados: {visited}")
        paso += 1

        for v, weight_uv in enumerate(adj_matrix[u]):
            if weight_uv > 0 and not visited[v] and weight_uv < cost[v]:
                cost[v] = weight_uv
                edge_to[v] = u
                heapq.heappush(pq, (weight_uv, v))
                print(f"       ✅ Se actualiza el costo para v={v}: nuevo padre = {u}, peso = {weight_uv}")

    print("\n✅ Árbol de Expansión Mínima completo:")
    for u, v, w in mst_edges:
        print(f"   ({u}, {v})  peso = {w}")
    print(f"Peso total = {total_weight}")

    # Mostrar gráfica solo al final
    dibujar_resultado_final(G, pos, mst_edges)

# Matriz de adyacencia
adj_matrix = [
    [ 0, 2, 0, 6, 0],
    [ 2, 0, 3, 8, 5],
    [ 0, 3, 0, 0, 7],
    [ 6, 8, 0, 0, 9],
    [ 0, 5, 7, 9, 0]
]

# Ejecutar simulador
prim_con_terminal_y_resultado_final(adj_matrix)
