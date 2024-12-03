import random
import json

# **1. Generator drzew**
class RandomTreeGenerator:
    def __init__(self, max_depth, grammar_rules):
        self.max_depth = max_depth
        self.grammar_rules = grammar_rules

    def generate_tree(self, depth=0):
        if depth >= self.max_depth:
            return random.choice(self.grammar_rules['terminals'])

        node_type = random.choice(['function', 'terminal'])
        if node_type == 'function':
            func = random.choice(self.grammar_rules['functions'])
            return (func['name'], [self.generate_tree(depth + 1) for _ in range(func['arity'])])
        else:
            return random.choice(self.grammar_rules['terminals'])

# **2. Funkcje dla krzyżowania i mutacji**
def crossover(tree1, tree2):
    def select_random_subtree(tree):
        if not isinstance(tree, tuple):  # Jeśli terminal
            return tree
        return random.choice(tree[1])  # Wybierz losowe dziecko

    subtree1 = select_random_subtree(tree1)
    subtree2 = select_random_subtree(tree2)

    # Zamień poddrzewa
    return replace_subtree(tree1, subtree1, subtree2), replace_subtree(tree2, subtree2, subtree1)

def replace_subtree(tree, old_subtree, new_subtree):
    if tree == old_subtree:
        return new_subtree
    if not isinstance(tree, tuple):
        return tree
    return (tree[0], [replace_subtree(child, old_subtree, new_subtree) for child in tree[1]])

def mutate(tree, generator):
    if random.random() < 0.1:  # Prawdopodobieństwo mutacji
        return generator.generate_tree()
    if not isinstance(tree, tuple):
        return tree
    return (tree[0], [mutate(child, generator) for child in tree[1]])

# **3. Funkcja oceny przystosowania (fitness function)**
def fitness_function(program):
    # Dane testowe
    test_data = [
        {'x': 1, 'y': 2},
        {'x': 2, 'y': 3},
        {'x': 3, 'y': 4},
    ]

    output_values = []  # Wyniki programu dla każdego zestawu danych testowych
    for data in test_data:
        try:
            output = evaluate_program(program, data)  # Oblicz wynik programu
            output_values.append(output)
        except Exception as e:
            # Jeśli program wywołuje błąd
            return float('inf')  # Maksymalna kara

    # Ocena przystosowania
    if 1 in output_values:
        fitness = len([v for v in output_values if v != 1])  # Licz inne liczby niż 1
    else:
        fitness = 1000 + len(output_values)  # Kara za brak 1

    return fitness

# **4. Ewaluacja programu (drzewa)**
def evaluate_program(tree, input_data):
    if not isinstance(tree, tuple):  # Terminal
        return input_data[tree] if tree in input_data else tree  # Zmienna lub stała
    operator = tree[0]
    args = [evaluate_program(child, input_data) for child in tree[1]]
    return apply_operator(operator, args)

def apply_operator(operator, args):
    if operator == '+': return args[0] + args[1]
    if operator == '*': return args[0] * args[1]
    if operator == '-': return args[0] - args[1]
    if operator == 'if': return args[1] if args[0] else args[2]
    raise ValueError(f"Nieznany operator: {operator}")

# **5. Serializacja i deserializacja drzew**
def serialize_tree(tree):
    return json.dumps(tree)

def deserialize_tree(serialized_tree):
    return json.loads(serialized_tree)

# **6. Algorytm Genetyczny**
class GeneticProgramming:
    def __init__(self, grammar_rules, max_depth, population_size):
        self.grammar_rules = grammar_rules
        self.generator = RandomTreeGenerator(max_depth, grammar_rules)
        self.population = [self.generator.generate_tree() for _ in range(population_size)]

    def evolve(self, generations, fitness_function, tournament_size):
        for generation in range(generations):
            new_population = []
            for _ in range(len(self.population)):
                parent1 = self.tournament_selection(fitness_function, tournament_size)
                parent2 = self.tournament_selection(fitness_function, tournament_size)
                offspring1, offspring2 = crossover(parent1, parent2)
                new_population.append(mutate(offspring1, self.generator))
                new_population.append(mutate(offspring2, self.generator))
            self.population = new_population[:len(self.population)]
            print(f"Pokolenie {generation}: najlepszy wynik fitness = {min(fitness_function(p) for p in self.population)}")

    def tournament_selection(self, fitness_function, tournament_size):
        tournament = random.sample(self.population, tournament_size)
        return min(tournament, key=fitness_function)

# **7. Definicja gramatyki mini-języka**
grammar_rules = {
    'functions': [
        {'name': '+', 'arity': 2},
        {'name': '*', 'arity': 2},
        {'name': '-', 'arity': 2},
        {'name': 'if', 'arity': 3},
    ],
    'terminals': ['x', 'y', 1, 2, 3, 0]  # Zmienne i stałe
}

# **8. Uruchomienie algorytmu**
if __name__ == "__main__":
    # Parametry
    max_depth = 3
    population_size = 10
    generations = 10
    tournament_size = 3

    # Tworzenie algorytmu genetycznego
    gp = GeneticProgramming(grammar_rules=grammar_rules, max_depth=max_depth, population_size=population_size)

    # Ewolucja
    gp.evolve(generations=generations, fitness_function=fitness_function, tournament_size=tournament_size)

    # Wyświetlenie wynikowej populacji
    print("\nOstateczna populacja:")
    for i, program in enumerate(gp.population):
        fitness = fitness_function(program)
        print(f"Program {i}: {program}, Przystosowanie: {fitness}")
