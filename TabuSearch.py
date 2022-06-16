import random

def calculate_distance(trace: list, starting_distances: dict, shelves_distances: dict):
    current_distance = 0
    for i in range(len(trace)):
        # add distance between starting point and first shelf
        if i == 0:
            current_distance += starting_distances[trace[i]]
        # add distance between next pairs of shelves
        else:
            current_point = trace[i]
            previous_point = trace[i - 1]
            current_distance += shelves_distances[previous_point][current_point]

    return current_distance


class TabuSearch:

    @staticmethod
    def find_distance(starting_distances: dict, shelves_distances: dict, number_of_iterations: int) -> None:
        tabu_search_traces = {}
        random_trace = {}
        all_shelves = []
        tabu_list = []
        best_distance = 999999

        for i in range(number_of_iterations):
            current_trace = []
            while len(current_trace) != len(shelves_distances):
                next_shelf = random.choice(list(shelves_distances))
                if next_shelf not in current_trace:
                    current_trace.append(next_shelf)
            random_trace[i] = current_trace
            print(random_trace[i])
            distance = calculate_distance(random_trace[i], starting_distances, shelves_distances)

            print("--------------------------------------------")
            print(f"Trace: {random_trace[i]}")
            print(f"Distance: {distance}")

            if distance in tabu_list:
                i=i-1
            if distance < best_distance:
                best_distance = distance
                best_trace = random_trace[i]
            else:
                tabu_list.append(distance)

        print("###################################")
        print(f"Best trace: " + str(best_trace))
        print(f"Length: " + str(best_distance))



        # # get "names" of all shelves
        # for key, value in shelves_distances.items():
        #     all_shelves.append(key)
        #
        # # print(all_shelves)
        #
        # # get all possible permutations of shelves
        # all_traces = list(itertools.permutations(all_shelves, len(all_shelves)))
        # for i in range(len(all_traces)):
        #     tabu_search_traces[i] = all_traces[i]
        #
        # # print(tabu_search_traces)
        #
        # # calculate distances for every trace
        # distances = Algorithm.calculate_distances(tabu_search_traces, starting_distances, shelves_distances)
        # best_distance = distances[0]
        #
        # # print(distances)
        #
        # for j in range(len(distances)):
        #     if distances[j] in tabu_list:
        #         break
        #     if distances[j] < best_distance:
        #         best_distance = distances[j]
        #         tabu_list.append(distances[j-1])
        #
        # print(best_distance)








