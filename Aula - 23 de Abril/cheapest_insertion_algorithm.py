import numpy as np

def cheapest_insertion(distance_matrix):
    n = len(distance_matrix)
    
    start_cities = list(np.random.choice(n, size=2, replace=False))
    citie_1, citie_2 = start_cities

    tour = [citie_1, citie_2, citie_1]
    cities_unvisited = [i for i in range(n) if i not in start_cities]

    while cities_unvisited:
        best_increase = float('inf')
        best_city = None
        best_position = None

        for city in cities_unvisited:
            for position in range(len(tour) - 1):
                a = tour[position]
                b = tour[position + 1]
                increase = (
                    distance_matrix[a][city] + distance_matrix[city][b] - distance_matrix[a][b]
                )

                if increase < best_increase:
                    best_increase = increase
                    best_city = city
                    best_position = position + 1

        tour.insert(best_position, best_city)
        cities_unvisited.remove(best_city)

    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance_matrix[tour[i]][tour[i + 1]]

    return total_distance, tour