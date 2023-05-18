import heapq
from uni import Graph_ucs


class Graph_best_first_search:
    def __init__(self, graph, graphType):
        self.graph = graph
        self.graphType = graphType
        self.HeuristicDict = {}

    def print_path(self, tracepath):
        for t in tracepath:
            print(t, end=" ")
        print()  # Add a newline after printing the path

    def set_heuristics(self, heuristic_dict):
        self.HeuristicDict = heuristic_dict

    def best_first_search(self, start_node, goal_node):
        if self.graphType == "Undirectd Graph":
            return self.best_first_search_undirected(start_node, goal_node)
        else:
            return self.best_first_search_directed(start_node, goal_node)

    def best_first_search_undirected(self, start_node, goal_node):
        visited = set()
        heap = [(0, start_node)]
        path = []

        while heap:
            current_cost, current_vertex = heapq.heappop(heap)
            path.append(current_vertex)

            if current_vertex in goal_node:
                return path

            neighbors = self.graph[current_vertex]
            sorted_neighbors = sorted(neighbors, key=lambda x: self.graph[current_vertex][x]['weight'])

            for neighbor in sorted_neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    priority = self.heuristic_cost(neighbor, goal_node)
                    heapq.heappush(heap, (priority, neighbor))

        return []

    def best_first_search_directed(self, start_node, goal_node):
        visited = set()
        heap = [(0, start_node)]
        path = []

        while heap:
            current_cost, current_vertex = heapq.heappop(heap)
            path.append(current_vertex)

            if current_vertex in goal_node:
                return path

            neighbors = self.graph[current_vertex]
            sorted_neighbors = sorted(neighbors, key=lambda x: self.graph[current_vertex][x]['weight'])

            for neighbor in sorted_neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    priority = self.heuristic_cost(neighbor, goal_node)
                    heapq.heappush(heap, (priority, neighbor))

        return []

    def heuristic_cost(self, current_node, goal_node):
        # Calculate the heuristic cost as the shortest path distance to any of the goal nodes
        graph = Graph_ucs(self.graph,self.graphType)
        shortest_dist = float('inf')
        _, dist = graph.uniform_cost_search(current_node,goal_node)
        shortest_dist = min(shortest_dist, dist)
        return shortest_dist + self.HeuristicDict[current_node]

