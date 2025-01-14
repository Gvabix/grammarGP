import json
import random
from interpreter import Interpreter
from biblioteki import GrammarGP, Node

# Inicjalizacja obiektu GrammarGP
lang = GrammarGP(max_depth=3, min_depth=1, mutation_rate=0.3)

# Generowanie populacji programów
population = lang.generate_population(size=2)

# Iteracja przez populację i wyświetlanie informacji o programach
for individual in range(len(population)):
    print("Program numer: ", individual + 1)
    print(lang.to_code(population[individual]))  # Generowanie kodu z drzewa



# Tworzenie mutanta
newbaby1 = lang.mutate(population[0])
newbaby2 = lang.mutate(population[1])

# Wyświetlanie mutacji
print("mutant 1")
print(lang.to_code(newbaby1))  # Generowanie kodu z mutowanego drzewa

print("mutant 2")
print(lang.to_code(newbaby2))  # Generowanie kodu z mutowanego drzewa

interpreter = Interpreter(1000,100)
print("\nWykonywanie programu 1:")
interpreter.execute(population[0])
print("\nZmiennie:")
print(interpreter.variables)
print("\nWyniki:")
print(interpreter.output)

int = Interpreter(1000,100)
print("\nWykonywanie programu 2:")
int.execute(population[1])
print("\nZmiennie:")
print(int.variables)
print("\nWyniki:")
print(int.output)