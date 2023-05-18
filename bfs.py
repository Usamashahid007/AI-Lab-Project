from collections import deque

class Graph_bfs:
    def __init__(self, graph,graphType):
        self.graph = graph
        self.graphType=graphType

    def print_path(self, tracepath):
        for t in tracepath:
            print(t, end=" ")
        print()  # Add a newline after printing the path

    def bfs(self,start_node,goal_node):
        if self.graphType =="Undirectd Graph":
            return self.breadth_first_searchundirected(start_node,goal_node)
        else:
            return  self.breadth_first_search_directed(start_node,goal_node)



    def breadth_first_searchundirected(self, start_node, goal_node):
        visited = set()
        queue = deque()
        path = []

        queue.append(start_node)
        visited.add(start_node)

        while queue:
            current_vertex = queue.popleft()
            path.append(current_vertex)

            if current_vertex in goal_node:
                return path

            neighbors = self.graph[current_vertex]
            sorted_neighbors = sorted(neighbors)  # Sort neighbors in chronological order

            for neighbor in sorted_neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return []

    def breadth_first_search_directed(self, start_node, goal_node):
        visited = set()
        queue = deque()
        path = []

        queue.append(start_node)
        visited.add(start_node)

        while queue:
            current_vertex = queue.popleft()
            path.append(current_vertex)

            if current_vertex in goal_node:
                return path

            neighbors = self.graph[current_vertex]
            sorted_neighbors = sorted(neighbors)  # Sort neighbors in chronological order

            for neighbor in sorted_neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return []


