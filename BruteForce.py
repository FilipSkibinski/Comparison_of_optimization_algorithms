import itertools
from Algorithm import Algorithm


class BruteForce:

    @staticmethod
    def find_distances(starting_distances: dict, shelves_distances: dict) -> None:
        brute_force_traces = {}
        all_shelves = []

        # get "names" of all shelves
        for key, value in shelves_distances.items():
            all_shelves.append(key)

        # get all possible permutations of shelves
        all_traces = list(itertools.permutations(all_shelves, len(all_shelves)))
        for i in range(len(all_traces)):
            brute_force_traces[i] = all_traces[i]

        # calculate distances for every trace
        distances = Algorithm.calculate_distances(brute_force_traces, starting_distances, shelves_distances)
        # choose the shortest path
        best_distance = min(distances, key=distances.get)
        print("####################################################")
        print(f"Best trace: {brute_force_traces[best_distance]}")
        print(f"Length: {distances[best_distance]}")
        print("####################################################")



