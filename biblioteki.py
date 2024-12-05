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
    def __init__(self, max_depth: int = 5, min_depth: int = 2, mutation_rate: float = 0.3):
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
        num_statements = random.randint(3, 6)
        for _ in range(num_statements):
            program.children.append(self.generate_statement(depth + 1))
        return program

    def generate_statement(self, depth: int) -> Node:
        if depth >= self.max_depth:
            return self.generate_assignment()

        statement_type = random.choice(['assignment', 'loop', 'if', 'read', 'write', 'break', 'continue', 'block'])

        if statement_type == 'assignment':
            return self.generate_assignment()
        elif statement_type == 'loop':
            return self.generate_loop(depth)
        elif statement_type == 'if':
            return self.generate_if(depth)
        elif statement_type == 'read':
            return self.generate_read()
        elif statement_type == 'write':
            return self.generate_write(depth)
        elif statement_type == 'break':
            return Node('breakStatement', 'break')
        elif statement_type == 'continue':
            return Node('continueStatement', 'continue')
        elif statement_type == 'block':
            return self.generate_block(depth)

    def generate_block(self, depth: int) -> Node:
        block = Node('block', '{')
        num_statements = random.randint(1, 3)
        for _ in range(num_statements):
            block.children.append(self.generate_statement(depth + 1))
        return block

    def generate_assignment(self) -> Node:
        return Node('assignmentStatement', '=', [
            Node('identifier', random.choice(self.variables)),
            self.generate_expression(0)
        ])

    def generate_if(self, depth: int) -> Node:
        node = Node('ifStatement', 'if', [
            self.generate_expression(depth + 1),
            self.generate_statement(depth + 1)
        ])
        if random.random() < 0.5:
            node.children.append(self.generate_statement(depth + 1))
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

    def generate_expression(self, depth: int) -> Node:
        if depth >= self.max_depth:
            return self.generate_literal_or_identifier()

        expr_type = random.choice(['arithmetic', 'logical', 'relational', 'equality'])
        operator = random.choice(self.operators[expr_type])
        left_expr = self.generate_expression(depth + 1)
        right_expr = self.generate_expression(depth + 1)
        return Node('expression', operator, [left_expr, right_expr])

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
        if random.random() < self.mutation_rate:  # Mutation based on rate
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
        indent_str = ' ' * (4 * indent)
        if node.type == 'program':
            return '\n'.join([self.to_code(child, indent) for child in node.children])
        elif node.type == 'block':
            inner = '\n'.join([self.to_code(child, indent + 1) for child in node.children])
            return f"{indent_str}{{\n{inner}\n{indent_str}}}"
        elif node.type == 'assignmentStatement':
            return f"{indent_str}{node.children[0].value} = {self.to_code(node.children[1], 0)};"
        elif node.type == 'ifStatement':
            condition = self.to_code(node.children[0], 0)
            if_body = self.to_code(node.children[1], indent)
            if len(node.children) > 2:
                else_body = self.to_code(node.children[2], indent)
                return f"{indent_str}if ({condition}) {if_body} else {else_body}"
            return f"{indent_str}if ({condition}) {if_body}"
        elif node.type == 'loopStatement':
            condition = self.to_code(node.children[0], 0)
            body = self.to_code(node.children[1], indent)
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
        # Perform subtree crossover by swapping subtrees between parents
        subtree1 = self.select_random_subtree(parent1)
        subtree2 = self.select_random_subtree(parent2)

        # Create a copy of the first parent and replace a subtree with the second parent’s subtree
        child = copy.deepcopy(parent1)
        self.replace_subtree(child, subtree1, subtree2)
        return child

    def select_random_subtree(self, node: Node) -> Node:
        # Randomly traverse the tree and return a random subtree
        all_nodes = self._get_all_nodes(node)
        return random.choice(all_nodes)

    def replace_subtree(self, parent: Node, old_subtree: Node, new_subtree: Node):
        # Find and replace the old subtree with the new one
        nodes = self._get_all_nodes(parent)
        for i, n in enumerate(nodes):
            if n == old_subtree:
                nodes[i] = new_subtree
                break

def main():
    gp = GrammarGP(max_depth=4, min_depth=2, mutation_rate=0.25)
    population_size = 100
    generations = 50
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

    with open('results3.json', 'w') as f:
        json.dump(results, f, indent=4)
    print("Zapisano wyniki do pliku results4.json")

if __name__ == "__main__":
    main()
