class DataGenerator:

    # coordinates of all shelves + getter of specific set of shelves
    @staticmethod
    def get_shelves_set(number: int) -> dict:
        all_shelves = {
            'a': [2, 18], 'b': [4, 16], 'c': [6, 14], 'd': [3, 12], 'e': [5, 10],
            'f': [5, 8], 'g': [2, 6], 'h': [6, 4], 'i': [3, 2], 'j': [9, 18],
            'k': [9, 16], 'l': [10, 14], 'm': [9, 12], 'n': [9, 10], 'o': [10, 8],
            'p': [9, 6], 'r': [9, 4], 's': [10, 2], 't': [13, 18], 'x': [14, 16],
            'y': [13, 14], 'w': [12, 12], 'z': [15, 10], 'aa': [13, 8], 'bb': [14, 6],
            'cc': [14, 4], 'dd': [12, 2], 'ee': [17, 18], 'ff': [19, 16], 'gg': [20, 14],
            'hh': [21, 12], 'ii': [18, 10], 'jj': [19, 8], 'kk': [20, 6], 'll': [17, 4],
            'mm': [19, 2], 'nn': [24, 18], 'oo': [24, 16], 'pp': [24, 14], 'rr': [24, 12],
            'ss': [25, 10], 'tt': [24, 8], 'xx': [24, 6], 'yy': [24, 4], 'ww': [24, 2],
        }

        shelves_set = []
        if number == 3:
            shelves_set = ['a', 'bb', 'nn']
        elif number == 5:
            shelves_set = ['a', 'bb', 'nn', 't', 'i']
        elif number == 15:
            shelves_set = ['a', 'bb', 'nn', 't', 'i', 'dd', 'e', 'yy', 'ee', 'p', 'ww', 'r', 'o', 'c', 'cc']
        elif number == 30:
            shelves_set = ['a', 'b', 'e', 'g', 'i', 'j', 'k', 'l', 'n', 's', 't', 'x', 'y', 'w', 'bb', 'dd', 'ff', 'gg',
                           'hh', 'jj', 'kk', 'll', 'mm', 'nn', 'pp', 'rr', 'ss', 'tt', 'yy', 'ww']
        elif number == 45:
            return all_shelves

        set_with_positions = {}
        for key, value in all_shelves.items():
            if key in shelves_set:
                set_with_positions[key] = value
        return set_with_positions

    # calculation distance between starting point and every shelf
    @staticmethod
    def calculate_starting_distances(starting_coordinates: list, shelves_coordinates: dict) -> dict:
        starting_distances = {}
        for key, value in shelves_coordinates.items():
            # calculation distances between starting point and particular shelf
            starting_distances[key] = abs(starting_coordinates[0] - value[0]) + abs(starting_coordinates[1] - value[1])
        return starting_distances

    # calculation distances between every pair of shelves
    @staticmethod
    def calculate_shelves_distances(shelves_coordinates: dict) -> dict:
        shelves_distances = {}
        # for every single shelf calculate distances to all other shelves
        for key, value in shelves_coordinates.items():
            temporary_distances = {}
            for next_key, next_value in shelves_coordinates.items():
                if key != next_key:
                    temporary_distances[next_key] = abs(next_value[0] - value[0]) + abs(next_value[1] - value[1])
            shelves_distances[key] = temporary_distances
        return shelves_distances

