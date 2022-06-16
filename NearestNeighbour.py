from Algorithm import Algorithm


class NearestNeighbour:

    @staticmethod
    def find_distance(starting_distances: dict, shelves_distances: dict) -> None:
        nearest_neighbour_trace = {}
        # Nearest shelf for starting point
        first_shelf = min(starting_distances, key=starting_distances.get)
        nearest_neighbour_trace[0] = [first_shelf]

        while len(nearest_neighbour_trace[0]) != len(shelves_distances):
            last_shelf = nearest_neighbour_trace[0][-1]
            # sort distances for last_shelf  by lowest distance
            distances_for_ls = dict(sorted(shelves_distances[last_shelf].items(), key=lambda item: item[1]))
            for shelf, distance in distances_for_ls.items():
                # choose the nearest shelf for last shelf which doesn't exist in trace
                if shelf not in nearest_neighbour_trace[0]:
                    nearest_neighbour_trace[0].append(shelf)
                    break
                else:
                    continue

        distance = Algorithm.calculate_distances(nearest_neighbour_trace, starting_distances, shelves_distances)
        print("####################################################")
        print(f"NN trace: {nearest_neighbour_trace[0]}")
        print(f"Distance: {distance[0]}")
        print("####################################################")