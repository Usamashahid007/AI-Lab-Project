import heapq

class Graph_ucs:
    def __init__(self, graph, graphType):
        self.graph = graph
        self.graphType = graphType

    def print_path(self, tracepath):
        for t in tracepath:
            print(t, end=" ")
        print()  # Add a newline after printing the path

    def uniform_cost_search(self, start_node, goal_node):
        if self.graphType == "Undirectd Graph":
            return self.uniform_cost_search_undirected(start_node, goal_node)
        else:
            return self.uniform_cost_search_directed(start_node, goal_node)

    def uniform_cost_search_undirected(self, start_node, goal_node):
        visited = set()
        queue = []
        cost = {start_node: 0}
        parent = {start_node: None}

        heapq.heappush(queue, (cost[start_node], start_node))

        def sort_neighbors(n):
            return cost[current_vertex] + int(self.graph[current_vertex][n]['weight'])

        while queue:
            current_cost, current_vertex = heapq.heappop(queue)

            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            if current_vertex in goal_node:
                path = []
                while current_vertex is not None:
                    path.append(current_vertex)
                    current_vertex = parent[current_vertex]
                path.reverse()
                return path, current_cost

            neighbors = self.graph[current_vertex]
            sorted_neighbors = sorted(neighbors, key=sort_neighbors)

            for neighbor in sorted_neighbors:
                if neighbor in visited:
                    continue

                new_cost = cost[current_vertex] + int(neighbors[neighbor]['weight'])
                if neighbor not in cost or new_cost < cost[neighbor]:
                    cost[neighbor] = new_cost
                    parent[neighbor] = current_vertex
                    heapq.heappush(queue, (cost[neighbor], neighbor))

        return []

    def uniform_cost_search_directed(self, start_node, goal_node):
        visited = set()
        queue = []
        cost = {start_node: 0}
        parent = {start_node: None}

        heapq.heappush(queue, (cost[start_node], start_node))

        def sort_neighbors(n):
            return cost[current_vertex] + int(self.graph[current_vertex][n]['weight'])

        while queue:
            current_cost, current_vertex = heapq.heappop(queue)

            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            if current_vertex in goal_node:
                path = []
                while current_vertex is not None:
                    path.append(current_vertex)
                    current_vertex = parent[current_vertex]
                path.reverse()
                return path, current_cost

            neighbors = list(self.graph[current_vertex])
            sorted_neighbors = sorted(neighbors, key=sort_neighbors)

            for neighbor in sorted_neighbors:
                if neighbor in visited:
                    continue

                new_cost = cost[current_vertex] + int(self.graph[current_vertex][neighbor]['weight'])
                if neighbor not in cost or new_cost < cost[neighbor]:
                    cost[neighbor] = new_cost
                    parent[neighbor] = current_vertex
                    heapq.heappush(queue, (cost[neighbor], neighbor))

        return []

