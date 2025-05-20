import numpy as np
import pandas as pd
import time

# Parâmetros variáveis para grid search
grid_population_size = [10, 100, 1000]
grid_mutation_rate = [0.05, 0.5, 0.1]
iterations = 5

# Constantes do problema
n = 8
max_generations = 1000
visualize_every = 100  # Pode aumentar para menos prints
resultados = []

# Funções do algoritmo genético (já fornecidas) — com pequenas modificações:
def EvaluateFitness(genes):
    non_attacking = 0
    for i in range(n):
        for j in range(i + 1, n):
            if genes[i] != genes[j] and abs(genes[i] - genes[j]) != abs(i - j):
                non_attacking += 1
    return non_attacking

def CreateIndividual():
    genes = np.random.randint(0, n, size=n)
    return genes, EvaluateFitness(genes)

def CreateIndividualFromGenes(genes):
    return genes, EvaluateFitness(genes)

def CreatePopulation(population_size):
    return [CreateIndividual() for _ in range(population_size)]

def SelectParent(population):
    candidates = [population[i] for i in np.random.choice(len(population), 5)]
    return max(candidates, key=lambda x: x[1])

def Crossover(parent1, parent2):
    crossover_point = np.random.randint(1, n - 1)
    genes1, _ = parent1
    genes2, _ = parent2
    child_genes = np.concatenate((genes1[:crossover_point], genes2[crossover_point:]))
    return CreateIndividualFromGenes(child_genes)

def Mutate(individual, mutation_rate):
    genes, _ = individual
    if np.random.rand() < mutation_rate:
        i = np.random.randint(0, n)
        genes[i] = np.random.randint(0, n)
    return genes, EvaluateFitness(genes)

def EvolvePopulation(population, population_size, mutation_rate):
    new_generation = []
    while len(new_generation) < population_size:
        parent1 = SelectParent(population)
        parent2 = SelectParent(population)
        child = Crossover(parent1, parent2)
        child = Mutate(child, mutation_rate)
        new_generation.append(child)
    return new_generation

def RunGeneticAlgorithm(population_size, mutation_rate):
    population = CreatePopulation(population_size)
    for generation in range(max_generations):
        population = sorted(population, key=lambda x: x[1], reverse=True)
        best_individual = population[0]
        if best_individual[1] == (n * (n - 1)) // 2:
            return generation, best_individual[1]
        population = EvolvePopulation(population, population_size, mutation_rate)
    return max_generations, best_individual[1]

# Executar testes
for i in range(iterations):
    for population_size in grid_population_size:
        for mutation_rate in grid_mutation_rate:
            start = time.time()
            generations, best_fitness = RunGeneticAlgorithm(population_size, mutation_rate)
            end = time.time()
            resultados.append({
                "Iteração": i + 1,
                "Population Size": population_size,
                "Mutation Rate": mutation_rate,
                "Gerações até solução ou fim": generations,
                "Fitness final": best_fitness,
                "Tempo (s)": round(end - start, 4)
            })

# Criar e salvar o DataFrame
df = pd.DataFrame(resultados)
print(df)
df.to_string(open("results.txt", "w"), index=False)
