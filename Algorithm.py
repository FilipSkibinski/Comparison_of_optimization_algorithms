class Algorithm:

    @staticmethod
    def calculate_distances(traces: dict, starting_distances: dict, shelves_distances:dict) -> dict:
        distances = {}
        for element in traces:
            current_distance = 0
            for i in range(len(traces[element])):
                # add distance between starting point and first shelf
                if i == 0:
                    current_distance += starting_distances[traces[element][i]]
                # add distance between next pairs of shelves
                else:
                    current_point = traces[element][i]
                    previous_point = traces[element][i - 1]
                    current_distance += shelves_distances[previous_point][current_point]
            # add total distance for every trace
            distances[element] = current_distance
            print("--------------------------------------------")
            print(f"Trace: {traces[element]}")
            print(f"Distance: {current_distance}")
        return distances
