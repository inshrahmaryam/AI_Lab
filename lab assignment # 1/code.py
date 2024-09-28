from collections import deque

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, node):
        return self.adjacency_list.get(node, [])

    def a_star_algorithm(self, start_node, stop_node):
        all_nodes = set(self.adjacency_list.keys())
        for neighbors in self.adjacency_list.values():
            all_nodes.update([neighbor for neighbor, _ in neighbors])

        h = {node: 1 for node in all_nodes}

        g = {node: float('inf') for node in all_nodes}
        g[start_node] = 0

        # f(n) = g(n) + h(n)
        f = {node: float('inf') for node in all_nodes}
        f[start_node] = h[start_node]

        open_list = set([start_node])
        closed_list = set()

        parent = {start_node: None}

        print(f"Starting A* algorithm from {start_node} to {stop_node}")

        while open_list:

            current_node = min(open_list, key=lambda node: f[node])

            print(f"Current node: {current_node}")

            if current_node == stop_node:
                path = []
                while current_node:
                    path.append(current_node)
                    current_node = parent[current_node]
                path.reverse()
                print(f"Path found: {path}")
                return path

            open_list.remove(current_node)
            closed_list.add(current_node)

            for (neighbor, weight) in self.get_neighbors(current_node):
                print(f"Evaluating neighbor: {neighbor}, weight: {weight}")
                if neighbor in closed_list:
                    continue  # Ignore the neighbor if already processed

                tentative_g = g[current_node] + weight

                if tentative_g < g[neighbor]:
                    # If a better path is found
                    parent[neighbor] = current_node
                    g[neighbor] = tentative_g
                    f[neighbor] = g[neighbor] + h[neighbor]

                    if neighbor not in open_list:
                        open_list.add(neighbor)

        print("No path found")
        return None

adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}

graph1 = Graph(adjacency_list)
print("Running the A* algorithm...")
graph1.a_star_algorithm('A', 'D')
print("Finished running the A* algorithm.")
