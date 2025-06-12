import matplotlib.pyplot as plt         # Importa matplotlib para graficar el resultado
import networkx as nx                  # Importa NetworkX para crear y manipular grafos

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))   # Inicializa cada nodo como su propio padre (conjunto disjunto)

    def find(self, u):
        if self.parent[u] != u:        # Si u no es su propio padre, busca recursivamente su raíz
            self.parent[u] = self.find(self.parent[u])  # Aplica compresión de camino para optimizar
        return self.parent[u]          # Devuelve el representante del conjunto de u

    def union(self, u, v):
        root_u = self.find(u)          # Encuentra la raíz del conjunto de u
        root_v = self.find(v)          # Encuentra la raíz del conjunto de v
        if root_u != root_v:           # Si están en diferentes conjuntos, se pueden unir
            self.parent[root_v] = root_u   # Une los conjuntos haciendo que root_v apunte a root_u
            return True                # Devuelve True si se unieron
        return False                   # Devuelve False si ya estaban unidos (formarían ciclo)

def mostrar_resultado(G, pos, aristas_resultado, titulo):
    plt.figure(figsize=(6, 5))                         # Crea una nueva figura de 6x5 pulgadas
    plt.title(titulo)                                  # Establece el título de la figura

    # Dibuja todos los nodos y aristas originales en color gris
    nx.draw(G, pos, with_labels=True, node_color='lightgray', edge_color='gray',
            node_size=700, font_weight='bold')

    edges = [(u, v) for u, v, _ in aristas_resultado]  # Extrae solo las tuplas (u, v) de las aristas resultado
    edge_labels = {(u, v): w for u, v, w in aristas_resultado}  # Crea un diccionario con etiquetas de peso

    # Dibuja las aristas seleccionadas (del árbol) en azul
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='blue', width=2.5)

    # Dibuja las etiquetas de los pesos sobre las aristas seleccionadas
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='blue')
    plt.show()                                         # Muestra la gráfica


def kruskal(adj_matrix, modo="minimo"):
    num_vertices = len(adj_matrix)  # Obtiene el número de vértices del grafo
    aristas = []  # Lista para almacenar todas las aristas

    # Recorre la matriz para extraer las aristas únicas (grafo no dirigido)
    for u in range(num_vertices):
        for v in range(u + 1, num_vertices):
            if adj_matrix[u][v] != 0:  # Si hay conexión entre u y v
                aristas.append((adj_matrix[u][v], u, v))  # Agrega la arista (peso, u, v)

    # Ordena las aristas por peso: ascendente para mínimo, descendente para máximo
    aristas.sort(reverse=(modo == "maximo"))

    uf = UnionFind(num_vertices)  # Inicializa estructura Union-Find
    arbol = []  # Lista de aristas del árbol resultante
    total = 0  # Acumulador del peso total del árbol
    paso = 1  # Contador de pasos para mostrar en consola

    tipo = "mínimo" if modo == "minimo" else "máximo"  # Define el tipo de árbol según el modo
    print(f"\n🔷 Simulación del Árbol de Expansión de {tipo} costo (Kruskal):")  # Título en consola

    # Recorre todas las aristas ordenadas
    for peso, u, v in aristas:
        print(f"\nPaso {paso}: Considerando arista ({u}, {v}) con peso {peso}")  # Muestra arista actual
        if uf.union(u, v):  # Si unir u y v no forma ciclo
            arbol.append((u, v, peso))  # Agrega arista al árbol
            total += peso  # Suma el peso al total
            print(f"   ✅ Se añade al árbol")  # Mensaje de éxito
        else:
            print(f"   ❌ Forma un ciclo, se descarta")  # Mensaje si se descarta
        paso += 1  # Incrementa el paso

        if len(arbol) == num_vertices - 1:  # Si ya se tienen n-1 aristas, termina
            break

    # Muestra el resultado final por consola
    print(f"\n✅ Árbol de Expansión de {tipo} costo completado:")
    for u, v, w in arbol:
        print(f"   ({u}, {v}) peso = {w}")
    print(f"   ➕ Costo total: {total}")

    # Crea el grafo completo con networkx para graficar
    G = nx.Graph()
    for u in range(num_vertices):
        for v in range(u + 1, num_vertices):
            if adj_matrix[u][v] != 0:
                G.add_edge(u, v, weight=adj_matrix[u][v])  # Agrega todas las aristas al grafo

    pos = nx.spring_layout(G, seed=42)  # Calcula posiciones de los nodos para graficar
    mostrar_resultado(G, pos, arbol,
                      f"Árbol de {tipo.capitalize()} Costo (Kruskal)")  # Llama a la función para graficar

# Matriz de adyacencia de ejemplo
adj_matrix = [
    [0, 2, 0, 6, 0],   # Nodo 0
    [2, 0, 3, 8, 5],   # Nodo 1
    [0, 3, 0, 0, 7],   # Nodo 2
    [6, 8, 0, 0, 9],   # Nodo 3
    [0, 5, 7, 9, 0]    # Nodo 4
]

# Ejecutar simulador para árbol de mínimo costo
kruskal(adj_matrix, modo="minimo")

# Ejecutar simulador para árbol de máximo costo
kruskal(adj_matrix, modo="maximo")
