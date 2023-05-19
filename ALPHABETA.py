from uni import Graph_ucs
class AlphaBetaPruning:
    def __init__(self, graph, graphtype):
        self.graph = graph
        self.graphtype = graphtype

    def print_path(self, tracepath):
        for t in tracepath:
            print(t, end=" ")
        print()  # Add a newline after printing the path

    def alpha_beta_pruning(self, start_node, goal_node, max_depth):
        best_path = []
        best_cost = float('-inf')
        alpha = float('-inf')
        beta = float('inf')

        self.max_depth = max_depth

        for neighbor in self.get_possible_neighbors(start_node):
            cost = self.minimax(neighbor, goal_node, 0, alpha, beta, False)
            if cost > best_cost:
                best_cost = cost
                best_path = [start_node, neighbor]

            alpha = max(alpha, best_cost)

        return best_path

    def minimax(self, current_node, goal_node, depth, alpha, beta, maximizing_player):
        if depth >= self.max_depth or current_node == goal_node:
            return self.calculate_cost(current_node, goal_node)

        if maximizing_player:
            max_cost = float('-inf')
            for neighbor in self.get_possible_neighbors(current_node):
                cost = self.minimax(neighbor, goal_node, depth + 1, alpha, beta, False)
                max_cost = max(max_cost, cost)
                alpha = max(alpha, max_cost)
                if beta <= alpha:
                    break
            return max_cost

        else:
            min_cost = float('inf')
            for neighbor in self.get_possible_neighbors(current_node):
                cost = self.minimax(neighbor, goal_node, depth + 1, alpha, beta, True)
                min_cost = min(min_cost, cost)
                beta = min(beta, min_cost)
                if beta <= alpha:
                    break
            return min_cost

    def calculate_cost(self, current_node, goal_node):
        graph = Graph_ucs(self.graph, self.graphtype)
        path = graph.uniform_cost_search(current_node, goal_node)
        return len(path) - 1

    def get_possible_neighbors(self, current_node):
        neighbors = list(self.graph.neighbors(current_node))
        return neighbors
