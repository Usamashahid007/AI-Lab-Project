import random
import math
from uni import Graph_ucs

class SimulatedAnnealing:
    def __init__(self, graph,graphtype):
        self.graph = graph
        self.graphtype=graphtype

    def print_path(self, tracepath):
        for t in tracepath:
            print(t, end=" ")
        print()  # Add a newline after printing the path

    def simulated_annealing(self, start_node, goal_node, initial_temperature, cooling_rate):
        current_state = start_node
        current_cost,best_path = self.calculate_cost(current_state, goal_node)

        best_cost = current_cost
        temperature = initial_temperature

        while temperature > 1:
            neighbor = self.get_random_neighbor(current_state)
            neighbor_cost,neighbor_path = self.calculate_cost(neighbor, goal_node)
            cost_difference = neighbor_cost - current_cost

            if cost_difference < 0 or random.random() < math.exp(-cost_difference / temperature):
                current_state = neighbor
                current_cost = neighbor_cost

                if current_cost < best_cost:
                    best_path.append(current_state)  # Add the current state to the best path
                    best_cost = current_cost

            temperature *= cooling_rate

        return best_path

    def calculate_cost(self, state, goal_node):
        graph=Graph_ucs(self.graph,self.graphtype)
        # Calculate the cost (e.g., distance) of the given state to the goal node
        path = graph.uniform_cost_search(state,goal_node)
        return len(path) - 1,path

    def get_random_neighbor(self, state):
        # Generate a random neighbor of the given state
        neighbors = list(self.graph.neighbors(state))
        return random.choice(neighbors)
