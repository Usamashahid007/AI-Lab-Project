import heapq
from uni import Graph_ucs

class Graph_astar:
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

    def astar_search(self, start_node, goal_node):
        if self.graphType == "Undirectd Graph":
            return self.astar_search_undirected(start_node, goal_node)
        else:
            return self.astar_search_directed(start_node, goal_node)

    def astar_search_undirected(self, start_node, goal_node):
        visited = set()
        heap = [(0, start_node, 0)]
        path = []

        while heap:
            current_cost, current_vertex, actual_cost = heapq.heappop(heap)
            path.append(current_vertex)

            if current_vertex in goal_node:
                print("TOTAL COST OF PATH IS : ", actual_cost)
                return path

            neighbors = self.graph[current_vertex]
            sorted_neighbors = sorted(neighbors, key=lambda x: self.graph[current_vertex][x]['weight'])

            for neighbor in sorted_neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    priority = self.heuristic_cost(neighbor, goal_node,
                                                   actual_cost + int(self.graph[current_vertex][neighbor]['weight']))
                    heapq.heappush(heap,
                                   (priority, neighbor,
                                    actual_cost + int(self.graph[current_vertex][neighbor]['weight'])))

        return [], float('inf')

    def astar_search_directed(self, start_node, goal_node):
        visited = set()
        heap = [(0, start_node, 0)]
        path = []

        while heap:
            current_cost, current_vertex, actual_cost = heapq.heappop(heap)
            path.append(current_vertex)

            if current_vertex in goal_node:
                print("TOTAL COST OF PATH IS : ",actual_cost)
                return path

            neighbors = self.graph[current_vertex]
            sorted_neighbors = sorted(neighbors, key=lambda x: self.graph[current_vertex][x]['weight'])

            for neighbor in sorted_neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    priority = self.heuristic_cost(neighbor, goal_node,
                                                   actual_cost + int(self.graph[current_vertex][neighbor]['weight']))
                    heapq.heappush(heap,
                                   (priority, neighbor, actual_cost + int(self.graph[current_vertex][neighbor]['weight'])))

        return [], float('inf')

    def heuristic_cost(self, current_node, goal_node, actual_cost):
        # Calculate the heuristic cost as the sum of the actual cost and the estimated cost to reach the goal node
        graph = Graph_ucs(self.graph, self.graphType)
        _, dist = graph.uniform_cost_search(current_node, goal_node)
        return actual_cost + dist + self.HeuristicDict[current_node]




