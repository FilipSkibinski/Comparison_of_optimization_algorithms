import random
from Algorithm import Algorithm


class RandomSearch:

    @staticmethod
    def find_distances(starting_distances: dict, shelves_distances: dict, number_of_iterations: int) -> None:
        random_traces = {}
        # draw traces no. of iterations times (every shelf is unique)
        for i in range(number_of_iterations):
            current_trace = []
            while len(current_trace) != len(shelves_distances):
                next_shelf = random.choice(list(shelves_distances))
                if next_shelf not in current_trace:
                    current_trace.append(next_shelf)
            random_traces[i] = current_trace

        # calculate distances for every trace
        distances = Algorithm.calculate_distances(random_traces, starting_distances, shelves_distances)
        # choose the shortest path
        best_distance = min(distances, key=distances.get)
        print("####################################################")
        print(f"Best trace: {random_traces[best_distance]}")
        print(f"Length: {distances[best_distance]}")
        print("####################################################")

