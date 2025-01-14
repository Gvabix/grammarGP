import json
from biblioteki import GrammarGP
from fitnessy import (
    fitness_1_1_A,
    fitness_1_1_B,
    fitness_1_1_C,
    fitness_1_1_D,
    fitness_1_1_E,
    fitness_1_1_F
)
from interpreter import Interpreter


def evolutionary_loop():
    max_generations = 100
    population_size = 100
    tournament_size = 3
    stagnation_threshold = 3  # Liczba generacji bez poprawy fitnessu
    restart_ratio = 0.5  # Procent populacji do restartu
    read_values = [10, 300, 18, -5, 16, 37, 0, 780]  # List of values for reading

    gp = GrammarGP(max_depth=6, min_depth=1, mutation_rate=0.2)
    interpreter = Interpreter(max_iterations=1000, max_time=10, input_data=read_values)

    # Generate initial population
    population = [gp.generate_program() for _ in range(population_size)]

    best_overall_fitness = 0.0
    best_overall_program = None
    best_generation_found = None

    generation_logs = []
    stagnation_counter = 0  # Licznik stagnacji

    for generation in range(max_generations):
        print(f"Generation {generation + 1}")

        # Evaluate fitness for each program
        fitness_scores = [fitness_1_1_D(program, interpreter) for program in population]

        # Identify the best program
        best_fitness = max(fitness_scores)
        best_program = population[fitness_scores.index(best_fitness)]
        best_program_code = gp.to_code(best_program)
        average_fitness = sum(fitness_scores) / len(fitness_scores)

        print(f"  Best Fitness: {best_fitness}")
        print(f"  Average Fitness: {average_fitness}")

        # Log generation details
        generation_logs.append({
            "generation": generation + 1,
            "best_fitness": best_fitness,
            "average_fitness": average_fitness,
            "best_program_code": best_program_code
        })

        # Update overall best solution
        if best_fitness > best_overall_fitness:
            best_overall_fitness = best_fitness
            best_overall_program = best_program
            best_generation_found = generation + 1
            stagnation_counter = 0  # Reset stagnation counter
        else:
            stagnation_counter += 1

        # Stop if a perfect solution is found
        if best_fitness == 1.0:
            print("  Perfect solution found!")
            print(best_program_code)
            break

        # Handle stagnation
        if stagnation_counter >= stagnation_threshold:
            print(f"  Stagnation detected for {stagnation_counter} generations. Restarting population...")
            num_to_restart = int(restart_ratio * population_size)
            new_population = [gp.generate_program() for _ in range(num_to_restart)]
            population = population[:population_size - num_to_restart] + new_population
            stagnation_counter = 0  # Reset stagnation counter
        else:
            # Generate new population through selection, crossover, and mutation
            new_population = []

            while len(new_population) < population_size:
                parent1 = gp.tournament_selection(population, fitness_scores, tournament_size)
                parent2 = gp.tournament_selection(population, fitness_scores, tournament_size)

                child = gp.subtree_crossover(parent1, parent2)
                child = gp.mutate(child)

                new_population.append(child)

            population = new_population

    # Save results to a JSON file
    results = {
        "best_program_code": gp.to_code(best_overall_program),
        "best_fitness": best_overall_fitness,
        "generation_found": best_generation_found,
        "generations": generation_logs
    }

    with open("task_1.1.D.json", "w") as json_file:
        json.dump(results, json_file, indent=4)

    print("Results saved to task_1.1.D.json")
    print("Final Best Program:")
    print(gp.to_code(best_overall_program))


if __name__ == "__main__":
    evolutionary_loop()
