from collections import deque

class Graph_bi:
    def __init__(self, graph, graphType):
        self.graph = graph
        self.graphType = graphType

    def print_path(self, tracepath):
        for t in tracepath:
            print(t, end=" ")
        print()  # Add a newline after printing the path

    def bidirectional(self,start_node,goal_node):
        if self.graphType=="Undirectd Graph":
            return self.bfs_bidirectional_undirected(start_node,goal_node)
        else:
            return self.bfs_bidirectional_directed(start_node,goal_node)

    def bfs_bidirectional_undirected(self, start_node, goal_node):
        visited_forward = set()
        visited_backward = set()
        queue_forward = deque()
        queue_backward = deque()
        path_forward = {}
        path_backward = {}

        queue_forward.append(start_node)
        visited_forward.add(start_node)
        path_forward[start_node] = None

        for g in goal_node:
            queue_backward.append(g)
            visited_backward.add(g)
            path_backward[g] = None

        while queue_forward and queue_backward:
            # Expand forward search tree
            current_vertex_forward = queue_forward.popleft()

            if current_vertex_forward in visited_backward:
                # Intersection point found
                path = self._merge_paths(path_forward, path_backward, current_vertex_forward)
                return path

            neighbors_forward = self.graph[current_vertex_forward]

            for neighbor_forward in neighbors_forward:
                if neighbor_forward not in visited_forward:
                    visited_forward.add(neighbor_forward)
                    queue_forward.append(neighbor_forward)
                    path_forward[neighbor_forward] = current_vertex_forward

            # Expand backward search tree
            current_vertex_backward = queue_backward.popleft()

            if current_vertex_backward in visited_forward:
                # Intersection point found
                path = self._merge_paths(path_forward, path_backward, current_vertex_backward)
                return path

            neighbors_backward = self.graph[current_vertex_backward]

            for neighbor_backward in neighbors_backward:
                if neighbor_backward not in visited_backward:
                    visited_backward.add(neighbor_backward)
                    queue_backward.append(neighbor_backward)
                    path_backward[neighbor_backward] = current_vertex_backward

        return []

    def _merge_paths(self, path_forward, path_backward, intersection_point):
        # Combine forward and backward paths to form the complete path
        path = []
        current_vertex = intersection_point

        while current_vertex is not None:
            path.append(current_vertex)
            current_vertex = path_forward[current_vertex]

        path.reverse()

        current_vertex = path_backward[intersection_point]

        while current_vertex is not None:
            path.append(current_vertex)
            current_vertex = path_backward[current_vertex]

        return path

    def bfs_bidirectional_directed(self, start_node, goal_node):
        visited_forward = set()
        queue_forward = deque()
        path_forward = {}

        queue_forward.append(start_node)
        visited_forward.add(start_node)
        path_forward[start_node] = None

        while queue_forward:
            # Expand forward search tree
            current_vertex_forward = queue_forward.popleft()

            # Check if any of the neighbors is the goal node
            for g in goal_node:
                if g in self.graph[current_vertex_forward]:
                    path = self._get_path(path_forward, current_vertex_forward, g)
                    return path

            neighbors_forward = self.graph[current_vertex_forward]

            for neighbor_forward in neighbors_forward:
                # Check if there is an edge from the current vertex to the neighbor
                if current_vertex_forward in self.graph[neighbor_forward] and neighbor_forward not in visited_forward:
                    visited_forward.add(neighbor_forward)
                    queue_forward.append(neighbor_forward)
                    path_forward[neighbor_forward] = current_vertex_forward

        return []

    def _get_path(self, path_forward, start_node, goal_node):
        # Reconstruct the path from start to goal
        path = []
        current_vertex = goal_node

        while current_vertex is not None:
            path.append(current_vertex)
            current_vertex = path_forward[current_vertex]

        path.reverse()
        return path