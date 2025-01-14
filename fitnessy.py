import random
from math import sqrt, log10
from biblioteki import GrammarGP
from interpreter import Interpreter

# Funkcja do obliczania podobieństwa między dwoma liczbami
def check_target(actual, target):
    """
    Sprawdzamy czy wartość jest równa oczekiwanej wartości, ewentualnie jak bliskie ma podobieństwo.
    Zwraca wartość [0, 1], gdzie 1 oznacza liczbę równą targetowi.
    """
    if actual == target:
        return 1.0

    actual = abs(actual)
    target = abs(target)

    if max(actual, target) > 1000:
        similarity = 1.0 / (1.0 + abs(log10(actual + 1) - log10(target + 1)))
    else:
        max_diff = max(target * 2, 100)
        diff = abs(actual - target)
        similarity = max(0, 1.0 - (diff / max_diff))

    return similarity

def check_position(output, target, desired_position=None):
    """
    Sprawdza pozycję dla której występuje nasz target w outpucie.
    Jeśli desired_position jest podane, sprawdza, czy wartość na tej pozycji
    jest równa target. Zwraca:
      - 1.0, jeśli wartość na desired_position jest równa target,
      - 0.4, jeśli target występuje gdzie indziej w output,
      - lub wagę podobieństwa, gdy nie ma targetu.
    """
    if not output:
        return 0.0

    # Jeśli celowa wartość jest dokładnie na żądanej pozycji
    if desired_position is not None and desired_position < len(output) and output[desired_position] == target:
        return 1.0

    # Jeśli celowa wartość występuje gdziekolwiek w output
    if target in output:
        return 0.4

    # Jeśli nie znaleziono targetu, można zwrócić część podobieństwa
    if desired_position is not None and desired_position < len(output):
        similarity = check_target(output[desired_position], target)
        return similarity * 0.5

    return 0.0

# Funkcja oceniająca długość outputu
def check_length(output, desired_length):
    """
    Sprawdzamy długość outputu.
    """
    if not output:
        return 0.0
    if len(output) == desired_length:
        return 1.0
    return max(0, 1.0 - abs(len(output) - desired_length) * 0.2)

# Funkcje oceny dla specyficznych zadań
def fitness_1_1_A(program, interpreter):
    '''
    Liczba 1 na wyjściu na jakiejkolwiek pozycji.
    Inne liczby na wyjściu dozwolone, długość wyjścia dowolna.
    '''
    output = interpreter.execute(program)
    print(f"Output for Task 1.1.A: {output}")
    if any(value == 1 for value in output):
        return 1.0
    elif output:
        return max(check_target(x, 1) for x in output)
    else:
        return 0.0

def fitness_1_1_B(program, interpreter):
    '''
    Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) liczbę 789.
    Poza liczbą 789 może też zwrócić inne liczby.
    '''
    output = interpreter.execute(program)
    print(f"Output for Task 1.1.B: {output}")
    if any(value == 789 for value in output):
        return 1.0
    elif output:
        return max(check_target(x, 789) for x in output)
    else:
        return 0.0

def fitness_1_1_C(program, interpreter):
    '''
    Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) liczbę 31415.
    Poza liczbą 31415 może też zwrócić inne liczby.
    '''
    output = interpreter.execute(program)
    print(f"Output for Task 1.1.C: {output}")
    if any(value == 31415 for value in output):
        return 1.0
    elif output:
        return max(check_target(x, 31415) for x in output)
    else:
        return 0.0

def fitness_1_1_D(program, interpreter):
    '''
    Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę 1.
    Poza liczbą 1 może też zwrócić inne liczby.
    '''
    output = interpreter.execute(program)
    print(f"Output for Task 1.1.D: {output}")
    return check_position(output, 1, 0)

def fitness_1_1_E(program, interpreter):
    '''
    Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę 789.
    Poza liczbą 789 może też zwrócić inne liczby.
    '''
    output = interpreter.execute(program)
    print(f"Output for Task 1.1.E: {output}")
    return check_position(output, 789, 0)

def fitness_1_1_F(program, interpreter):
    '''
    Program powinien wygenerować na wyjściu liczbę jako jedyną liczbę 1.
    Poza liczbą 1 NIE powinien nic więcej wygenerować.
    '''
    output = interpreter.execute(program)
    print(f"Output for Task 1.1.F: {output}")
    if len(output) == 1 and output[0] == 1:
        return 1.0
    return 0.0

# Function to evaluate programs
def evaluate_programs():
    input_file = "in.txt"
    output_file = "out.txt"
    read_values = [10, 3, 18, -5, 16, 37, 0, 1]  # List of values for reading

    # Initialize the interpreter with the list of values to be read
    interpreter = Interpreter(1000, 10, input_data=read_values)

    # Initialize GrammarGP for generating programs
    gp = GrammarGP(4, 2, mutation_rate=0.2)

    # Generate a test program using the grammar
    test_program = gp.generate_program()  # Adjusted to generate a single program

    # Optionally, you can replace the above line with a hardcoded test program, like this:
    # test_program = Node('program', '', [
    #     Node('write', 'write', [Node('literal', '1')])
    # ])

    # Convert the generated program to code (if needed)
    program_code = gp.to_code(test_program)
    print("Generated Program Code:")
    print(program_code)

    # Evaluate the fitness for different target values
    #print("Fitness for Task 1.1.A:", fitness_1_1_A(test_program, interpreter))
    #print("Fitness for Task 1.1.B:", fitness_1_1_B(test_program, interpreter))
    print("Fitness for Task 1.1.C:", fitness_1_1_C(test_program, interpreter))
    print("Fitness for Task 1.1.D:", fitness_1_1_D(test_program, interpreter))
    print("Fitness for Task 1.1.E:", fitness_1_1_E(test_program, interpreter))
    print("Fitness for Task 1.1.F:", fitness_1_1_F(test_program, interpreter))

# Entry point of the script
if __name__ == "__main__":
    evaluate_programs()

