import matplotlib.pyplot as plt
import networkx as nx

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Compresión de camino
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u
            return True
        return False

def mostrar_resultado(G, pos, aristas_resultado, titulo):
    plt.figure(figsize=(6, 5))
    plt.title(titulo)

    nx.draw(G, pos, with_labels=True, node_color='lightgray', edge_color='gray', node_size=700, font_weight='bold')
    edges = [(u, v) for u, v, _ in aristas_resultado]
    edge_labels = {(u, v): w for u, v, w in aristas_resultado}
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='blue', width=2.5)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='blue')
    plt.show()

def kruskal(adj_matrix, modo="minimo"):
    num_vertices = len(adj_matrix)
    aristas = []

    # Extraer todas las aristas del grafo
    for u in range(num_vertices):
        for v in range(u + 1, num_vertices):
            if adj_matrix[u][v] != 0:
                aristas.append((adj_matrix[u][v], u, v))

    # Ordenar aristas según modo
    aristas.sort(reverse=(modo == "maximo"))

    uf = UnionFind(num_vertices)
    arbol = []
    total = 0
    paso = 1

    tipo = "mínimo" if modo == "minimo" else "máximo"
    print(f"\n🔷 Simulación del Árbol de Expansión de {tipo} costo (Kruskal):")

    for peso, u, v in aristas:
        print(f"\nPaso {paso}: Considerando arista ({u}, {v}) con peso {peso}")
        if uf.union(u, v):
            arbol.append((u, v, peso))
            total += peso
            print(f"   ✅ Se añade al árbol")
        else:
            print(f"   ❌ Forma un ciclo, se descarta")
        paso += 1

        if len(arbol) == num_vertices - 1:
            break

    print(f"\n✅ Árbol de Expansión de {tipo} costo completado:")
    for u, v, w in arbol:
        print(f"   ({u}, {v}) peso = {w}")
    print(f"   ➕ Costo total: {total}")

    # Graficar resultado
    G = nx.Graph()
    for u in range(num_vertices):
        for v in range(u + 1, num_vertices):
            if adj_matrix[u][v] != 0:
                G.add_edge(u, v, weight=adj_matrix[u][v])
    pos = nx.spring_layout(G, seed=42)
    mostrar_resultado(G, pos, arbol, f"Árbol de {tipo.capitalize()} Costo (Kruskal)")

# Matriz de adyacencia de ejemplo
adj_matrix = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

# Ejecutar simulador
kruskal(adj_matrix, modo="minimo")
kruskal(adj_matrix, modo="maximo")
