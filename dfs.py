class Graph_dfs:
    def __init__(self, graph, graphType):
        self.graph = graph
        self.graphType = graphType

    def print_path(self, tracepath):
        for t in tracepath:
            print(t, end=" ")
        print()  # Add a newline after printing the path

    def dfs(self, start_node, goal_node):
        if self.graphType == "Undirectd Graph":
            return self.depth_first_search_undirected(start_node, goal_node)
        else:
            return self.depth_first_search_directed(start_node, goal_node)

    def depth_first_search_undirected(self, current_vertex, goal_node, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(current_vertex)
        path.append(current_vertex)

        if current_vertex in goal_node:
            return path

        neighbors = self.graph[current_vertex]


        for neighbor in neighbors:
            if neighbor not in visited:
                result = self.depth_first_search_undirected(neighbor, goal_node, visited, path)
                if result:
                    return result

        path.pop()
        return []

    def depth_first_search_directed(self, current_vertex, goal_node, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(current_vertex)
        path.append(current_vertex)

        if current_vertex in goal_node:
            return path

        neighbors = self.graph[current_vertex]

        for neighbor in neighbors:
            if neighbor not in visited:
                result = self.depth_first_search_directed(neighbor, goal_node, visited, path)
                if result:
                    return result

        path.pop()
        return []
