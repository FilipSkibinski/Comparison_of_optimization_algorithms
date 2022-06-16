import datetime

from BruteForce import BruteForce
from DataGenerator import DataGenerator
from RandomSearch import RandomSearch
from NearestNeighbour import NearestNeighbour
from TabuSearch import TabuSearch


# starting point of warehouse worker
starting_point = [27, 9]
# position of shelves (x, y) for calculate the best path
shelves_coordinates = {}

starting_distances = DataGenerator.calculate_starting_distances(starting_point, shelves_coordinates)
shelves_distances = DataGenerator.calculate_shelves_distances(shelves_coordinates)

while True:
    print("---------------------------------------------")
    print("1. Print distances from start point")
    print("2. Print distances from each point to other points")
    print("3. Calculate best trace using Random Search")
    print("4. Calculate best trace using Brute Force")
    print("5. Calculate trace using Nearest Neighbour")
    print("6. Calculate trace using Tabu Search")
    print("7. Calculate trace using Greedy")
    print("8. Choose number of shelves")
    choice = input("Your choice: ")

    if choice == '1':
        print(starting_distances)
    elif choice == '2':
        print(shelves_distances)
    elif choice == '3':
        number_of_iterations = int(input("Enter number of iterations:"))
        time_before_algorithm = datetime.datetime.now()
        RandomSearch.find_distances(starting_distances, shelves_distances, number_of_iterations)
        duration = datetime.datetime.now() - time_before_algorithm
        print(f"Algorithm duration: {duration.seconds}s {duration.microseconds/1000}ms")
    elif choice == '4':
        time_before_algorithm = datetime.datetime.now()
        BruteForce.find_distances(starting_distances, shelves_distances)
        duration = datetime.datetime.now() - time_before_algorithm
        print(f"Algorithm duration: {duration.seconds}s {duration.microseconds/1000}ms")
    elif choice == '5':
        time_before_algorithm = datetime.datetime.now()
        NearestNeighbour.find_distance(starting_distances, shelves_distances)
        duration = datetime.datetime.now() - time_before_algorithm
        print(f"Algorithm duration: {duration.seconds}s {duration.microseconds/1000}ms")
    elif choice == '6':
        number_of_iterations = int(input("Enter number of iterations:"))
        time_before_algorithm = datetime.datetime.now()
        TabuSearch.find_distance(starting_distances, shelves_distances, number_of_iterations)
        duration = datetime.datetime.now() - time_before_algorithm
        print(f"Algorithm duration: {duration.seconds}s {duration.microseconds / 1000}ms")
    elif choice == '8':
        choice = input("Choose: 3, 5, 15, 30 or 45 shelves?: ")
        shelves_coordinates = DataGenerator.get_shelves_set(int(choice))
        starting_distances = DataGenerator.calculate_starting_distances(starting_point, shelves_coordinates)
        shelves_distances = DataGenerator.calculate_shelves_distances(shelves_coordinates)
        print(shelves_coordinates)
    else:
        print("Invalid choice!")
