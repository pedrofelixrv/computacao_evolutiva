import numpy as np

def nearest_neighbor(distance_matrix):
    n = len(distance_matrix)
    total_distance = 0
    start = np.random.choice(n)
    visited_cities = [start]
    current_city = start

    while len(visited_cities) < n:
        next_city = None
        min_distance = float('inf')

        for city in range(n):
            if city not in visited_cities:
                if distance_matrix[current_city][city] < min_distance:
                    min_distance = distance_matrix[current_city][city]
                    next_city = city

        total_distance += min_distance
        visited_cities.append(next_city)
        current_city = next_city

    total_distance += distance_matrix[current_city][start]
    return total_distance, visited_cities