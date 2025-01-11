import json
import random
import copy
from typing import List
from dataclasses import dataclass

# Definicja węzła w drzewie
@dataclass
class Node:
    type: str
    value: str
    children: List['Node'] = None

    def __post_init__(self):
        if self.children is None:
            self.children = []

# Klasa główna dla GP
class GrammarGP:
    def __init__(self, max_depth: int = 4, min_depth: int = 2, mutation_rate: float = 0.3):
        self.max_depth = max_depth
        self.min_depth = min_depth
        self.mutation_rate = mutation_rate
        self.variables = [f"var_{i}" for i in range(6)]
        self.types = ["int", "float"]
        self.literals = [random.randint(0, 100), f"{random.uniform(0, 100):.2f}"]
        self.operators = {
            'arithmetic': ['+', '-', '*', '/'],
            'logical': ['&&', '||'],
            'relational': ['<', '>', '<=', '>='],
            'equality': ['==', '!='],
        }

    def generate_program(self, depth: int = 0) -> Node:
        program = Node('program', '')
        num_statements = random.randint(3, 6)  # Liczba pozostałych instrukcji
        for _ in range(num_statements - 1):
            statement = self.generate_statement(depth + 1)
            program.children.append(statement)

        return program

    def generate_block(self, depth: int) -> Node:
        # Jeśli osiągnięto max_depth, generujemy tylko przypisanie
        if depth >= self.max_depth:
            return self.generate_assignment(depth)

        block = Node('block', '{')
        # Liczba instrukcji w bloku
        num_statements = random.randint(1, 3)

        for _ in range(num_statements):
            statement_type = random.choice(['assignment', 'loop', 'if', 'read', 'write', 'break', 'continue'])

            if statement_type == 'assignment':
                block.children.append(self.generate_assignment(depth + 1))
            elif statement_type == 'loop':
                block.children.append(self.generate_loop(depth + 1))
            elif statement_type == 'if':
                block.children.append(self.generate_if(depth + 1))
            elif statement_type == 'read':
                block.children.append(self.generate_read())
            elif statement_type == 'write':
                block.children.append(self.generate_write(depth + 1))
            elif statement_type == 'break':
                block.children.append(self.generate_break())
            elif statement_type == 'continue':
                block.children.append(self.generate_continue())

        return block

    def generate_break(self) -> Node:
        return Node('breakStatement', 'break')

    def generate_continue(self) -> Node:
        return Node('continueStatement', 'continue')

    def generate_assignment(self, depth: int) -> Node:
        var = random.choice(self.variables)
        expression = self.generate_expression(depth + 1)
        return Node('assignmentStatement', '=', [
            Node('identifier', var),
            expression
        ])

    def generate_expression(self, depth: int) -> Node:
        # Kontrolowanie głębokości wyrażenia
        if depth >= self.max_depth:
            return self.generate_literal_or_identifier()

        expr_type = random.choice(['arithmetic', 'logical', 'relational', 'equality'])
        operator = random.choice(self.operators[expr_type])

        left_expr = self.generate_expression(depth + 1)
        right_expr = self.generate_expression(depth + 1)

        return Node('expression', operator, [left_expr, right_expr])

    def generate_statement(self, depth: int) -> Node:
        # Zapewnienie, że głębokość nie przekroczy max_depth
        if depth >= self.max_depth:
            return self.generate_assignment(depth)

        statement_type = random.choice(['assignment', 'loop', 'if', 'read', 'write'])

        if statement_type == 'assignment':
            return self.generate_assignment(depth)
        elif statement_type == 'loop':
            return self.generate_loop(depth)
        elif statement_type == 'if':
            return self.generate_if(depth)
        elif statement_type == 'read':
            return self.generate_read()
        elif statement_type == 'write':
            return self.generate_write(depth)

    def generate_if(self, depth: int) -> Node:
        node = Node('ifStatement', 'if', [
            self.generate_expression(depth + 1),
            self.generate_block(depth + 1)
        ])

        node.children.append(self.generate_block(depth + 1))
        return node

    def generate_loop(self, depth: int) -> Node:
        return Node('loopStatement', 'while', [
            self.generate_expression(depth + 1),
            self.generate_block(depth + 1)
        ])

    def generate_read(self) -> Node:
        return Node('read', 'read', [
            Node('identifier', random.choice(self.variables))
        ])

    def generate_write(self, depth: int) -> Node:
        return Node('write', 'write', [
            self.generate_expression(depth + 1)
        ])

    def generate_literal_or_identifier(self) -> Node:
        if random.random() < 0.5:
            return Node('literal', str(random.choice(self.literals)))
        else:
            return Node('identifier', random.choice(self.variables))

    def mutate(self, program: Node) -> Node:
        mutated = copy.deepcopy(program)
        nodes = self._get_all_nodes(mutated)
        if not nodes:
            return mutated
        node = random.choice(nodes)
        if random.random() < self.mutation_rate:
            if node.type == 'literal':
                node.value = str(random.choice(self.literals))
            elif node.type == 'identifier':
                node.value = random.choice(self.variables)
            elif node.type == 'expression':
                node.value = random.choice(random.choice(list(self.operators.values())))
                node.children[0] = self.generate_expression(0)
                node.children[1] = self.generate_expression(0)
        return mutated

    def _get_all_nodes(self, node: Node) -> List[Node]:
        nodes = [node]
        for child in node.children:
            nodes.extend(self._get_all_nodes(child))
        return nodes

    def to_code(self, node: Node, indent: int = 0) -> str:
        indent_str = ' ' * (4 * indent)  # 4 spacje dla każdego poziomu wcięcia
        if node.type == 'program':
            return '\n'.join([self.to_code(child, indent) for child in node.children])
        elif node.type == 'block':
            # Tworzenie bloku kodu, który będzie zaczynał się od '{' i kończył na '}'
            inner = '\n'.join([self.to_code(child, indent + 1) for child in node.children])
            return f"{indent_str}{{\n{inner}\n{indent_str}}}"
        elif node.type == 'assignmentStatement':
            return f"{indent_str}{node.children[0].value} = {self.to_code(node.children[1], 0)};"
        elif node.type == 'ifStatement':
            condition = self.to_code(node.children[0], 0)
            if_body = self.to_code(node.children[1], indent)

            # Dodanie nawiasów klamrowych wokół ciała if, ale tylko jeśli blok jest pusty lub nie zawiera nawiasów
            if not if_body.startswith("{"):
                if_body = f"{{\n{if_body}\n{indent_str}}}"

            if len(node.children) > 2:
                else_body = self.to_code(node.children[2], indent)
                # Dodanie nawiasów klamrowych wokół ciała else, ale tylko jeśli blok jest pusty lub nie zawiera nawiasów
                if not else_body.startswith("{"):
                    else_body = f"{{\n{else_body}\n{indent_str}}}"
                return f"{indent_str}if ({condition}) {if_body} else {else_body}"

            return f"{indent_str}if ({condition}) {if_body}"
        elif node.type == 'loopStatement':
            condition = self.to_code(node.children[0], 0)
            body = self.to_code(node.children[1], indent)

            # Sprawdzanie, czy ciało pętli wymaga nawiasów klamrowych
            if not body.startswith("{"):
                body = f"{{\n{body}\n{indent_str}}}"

            return f"{indent_str}while ({condition}) {body}"
        elif node.type == 'write':
            return f"{indent_str}write({self.to_code(node.children[0], 0)});"
        elif node.type == 'read':
            return f"{indent_str}read({node.children[0].value});"
        elif node.type == 'breakStatement':
            return f"{indent_str}break;"
        elif node.type == 'continueStatement':
            return f"{indent_str}continue;"
        elif node.type == 'expression':
            left = self.to_code(node.children[0], 0)
            right = self.to_code(node.children[1], 0)
            return f"({left} {node.value} {right})"
        elif node.type in ['literal', 'identifier']:
            return node.value
        return ''



    def tournament_selection(self, population: List[Node], fitness_scores: List[float], tournament_size: int) -> Node:
        selected = random.sample(list(zip(population, fitness_scores)), tournament_size)
        selected.sort(key=lambda x: x[1], reverse=True)
        return selected[0][0]

    def subtree_crossover(self, parent1: Node, parent2: Node) -> Node:
        subtree1 = self.select_random_subtree(parent1)
        subtree2 = self.select_random_subtree(parent2)
        child = copy.deepcopy(parent1)
        self.replace_subtree(child, subtree1, subtree2)
        return child

    def select_random_subtree(self, node: Node) -> Node:
        all_nodes = self._get_all_nodes(node)
        return random.choice(all_nodes)

    def replace_subtree(self, parent: Node, old_subtree: Node, new_subtree: Node):
        nodes = self._get_all_nodes(parent)
        for i, n in enumerate(nodes):
            if n == old_subtree:
                nodes[i] = new_subtree
                break

def main():
    gp = GrammarGP(max_depth=4, min_depth=1, mutation_rate=0.25)
    population_size = 10
    generations = 10
    tournament_size = 2

    population = [gp.generate_program() for _ in range(population_size)]
    results = []

    for generation in range(generations):
        fitness_scores = [random.random() for _ in population]
        new_population = []

        while len(new_population) < population_size:
            parent1 = gp.tournament_selection(population, fitness_scores, tournament_size)
            parent2 = gp.tournament_selection(population, fitness_scores, tournament_size)

            # Perform crossover
            offspring = gp.subtree_crossover(parent1, parent2)

            # Mutate the offspring
            offspring = gp.mutate(offspring)
            new_population.append(offspring)

        population = new_population

        best_program = max(population, key=lambda prog: fitness_scores[population.index(prog)])
        best_fitness = max(fitness_scores)
        avg_fitness = sum(fitness_scores) / len(fitness_scores)

        results.append({
            "generation": generation,
            "best_program": gp.to_code(best_program),
            "best_fitness": best_fitness,
            "average_fitness": avg_fitness,
        })

    with open('results1.json', 'w') as f:
        json.dump(results, f, indent=4)
    print("Zapisano wyniki do pliku results1.json")

if __name__ == "__main__":
    main()

