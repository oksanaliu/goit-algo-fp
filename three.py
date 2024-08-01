import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  

    def dijkstra(self, start):
        if start not in self.graph:
            raise ValueError(f"Вершина {start} не існує в графі")

        # Ініціалізуємо відстані до всіх вершин як нескінченність
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0

        # Ініціалізуємо бінарну купу з початковою вершиною
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

def main():
    # Створення графа
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)

    start_vertex = input("Введіть стартову вершину: ")

    try:
        # Виконуємо алгоритм Дейкстри
        distances = g.dijkstra(start_vertex)

        print("Відстані від вершини", start_vertex)
        for vertex, distance in distances.items():
            print(f"Вершина {vertex}: {distance}")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()