class Graph_ids:
    def __init__(self, graph, graphType):
        self.graph = graph
        self.graphType = graphType

    def print_path(self, tracepath):
        for t in tracepath:
            print(t, end=" ")
        print()  # Add a newline after printing the path

    def ids(self, start_node, goal_node):
        if self.graphType == "Undirectd Graph":
            return self.iterative_deepening_search_undirected(start_node, goal_node)
        else:
            return self.iterative_deepening_search_directed(start_node, goal_node)

    def iterative_deepening_search_undirected(self, start_node, goal_node):
        depth = 0
        while True:
            result = self.depth_limited_search_undirected(start_node, goal_node, depth)
            if result:
                print("DEPTH : ",depth)
                return result
            depth += 1

    def iterative_deepening_search_directed(self, start_node, goal_node):
        depth = 0
        while True:
            result = self.depth_limited_search_directed(start_node, goal_node, depth)
            if result:
                print("DEPTH : ", depth)
                return result
            depth += 1

    def depth_limited_search_undirected(self, current_vertex, goal_node, depth, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []

        if depth == 0:
            if current_vertex in goal_node:
                path.append(current_vertex)
                return path
            else:
                return None

        visited.add(current_vertex)
        path.append(current_vertex)

        neighbors = self.graph[current_vertex]

        for neighbor in neighbors:
            if neighbor not in visited:
                result = self.depth_limited_search_undirected(neighbor, goal_node, depth-1, visited, path)
                if result:
                    return result

        path.pop()
        return None

    def depth_limited_search_directed(self, current_vertex, goal_node, depth, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []

        if depth == 0:
            if current_vertex in goal_node:
                path.append(current_vertex)
                return path
            else:
                return None

        visited.add(current_vertex)
        path.append(current_vertex)

        neighbors = self.graph[current_vertex]

        for neighbor in neighbors:
            if neighbor not in visited:
                result = self.depth_limited_search_directed(neighbor, goal_node, depth-1, visited, path)
                if result:
                    return result

        path.pop()
        return None
