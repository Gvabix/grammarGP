import time
from biblioteki import Node, GrammarGP

class Interpreter:
    def __init__(self, max_iterations: int, max_time: int, input_data: list = None):
        self.max_iterations = max_iterations  # Maksymalna liczba iteracji
        self.max_time = max_time  # Maksymalny czas wykonania w sekundach
        self.variables = {}  # Przechowuje zmienne
        self.output = []  # Zbiera wyniki wykonania programu
        self.input_data = input_data if input_data else []  # Dane wejściowe (lista wartości)
        self.time_taken = 0  # Czas wykonania
        self.iterations = 0  # Liczba iteracji
        self.input_index = 0  # Indeks, który wskazuje, który element z listy input_data jest aktualnie przetwarzany

    def execute(self, node: Node):
        """ Funkcja wykonująca program (przechodzimy po drzewie AST) """
        start_time = time.time()  # Startujemy licznik czasu
        self.iterations = 0  # Reset iteracji

        self._execute_program(node)

        self.time_taken = time.time() - start_time  # Zliczamy czas wykonania
        return self.output

    def _execute_program(self, node: Node):
        """ Funkcja pomocnicza do wykonania programu (rekursywnie przechodzimy po drzewie AST) """
        if self.iterations >= self.max_iterations:
            return  # Przerywamy bez dodatkowego komunikatu

        if self.time_taken >= self.max_time:
            return  # Przerywamy bez dodatkowego komunikatu

        # Sprawdzamy, czy node jest krotką
        if isinstance(node, tuple):
            for sub_node in node:  # Iterujemy po każdym elemencie krotki
                self._execute_program(sub_node)  # Rekursywnie wywołujemy funkcję dla każdego elementu
            return

        # Obsługuje różne typy węzłów (instrukcji) w programie
        if node.type == 'program':
            for child in node.children:
                self._execute_statement(child)
        else:
            self._execute_statement(node)


    def _execute_statement(self, node: Node):
        """ Funkcja pomocnicza do wykonania pojedynczej instrukcji """
        if node.type == 'assignmentStatement':
            self._execute_assignment(node)
        elif node.type == 'ifStatement':
            self._execute_if(node)
        elif node.type == 'loopStatement':
            self._execute_loop(node)
        elif node.type == 'write':
            self._execute_write(node)
        elif node.type == 'read':
            self._execute_read(node)
        elif node.type == 'breakStatement':
            return 'break'
        elif node.type == 'continueStatement':
            return 'continue'

    def _execute_assignment(self, node: Node):
        """ Wykonanie przypisania (zmienna = wartość) """
        var_name = node.children[0].value  # Zmienna, do której przypisujemy wartość
        value = self._evaluate_expression(node.children[1])  # Obliczenie wartości
        self.variables[var_name] = value  # Przypisanie do zmiennej

    def _execute_if(self, node: Node):
        """ Wykonanie instrukcji warunkowej (if) """
        condition = self._evaluate_expression(node.children[0])  # Sprawdzamy warunek
        if condition:
            # Jeśli warunek jest prawdziwy, wykonujemy blok if
            self._execute_program(node.children[1])
        elif len(node.children) > 2:
            # Jeśli jest blok else, wykonujemy go
            self._execute_program(node.children[2])

    def _execute_loop(self, node: Node):
        """ Wykonanie instrukcji pętli (while) """
        condition = node.children[0]  # Warunek pętli
        block = node.children[1]  # Blok do wykonania w pętli

        loop_counter = 0
        while self._evaluate_expression(condition):
            if loop_counter >= self.max_iterations:
                break  # Po prostu przerywamy pętlę bez dodatkowego komunikatu
            self._execute_program(block)  # Wykonanie bloku
            loop_counter += 1

    def _execute_write(self, node: Node):
        """ Wykonanie instrukcji write (wypisanie na ekran) """
        value = self._evaluate_expression(node.children[0])  # Obliczamy wartość do wypisania
        self.output.append(value)  # Dodajemy do wyników

    def _execute_read(self, node: Node):
        """ Wykonanie instrukcji read (wczytanie danych z input_data) """
        var_name = node.children[0].value  # Zmienna, do której przypisujemy wartość
        if self.input_index < len(self.input_data):
            self.variables[var_name] = self.input_data[self.input_index]  # Przypisanie z input_data
            self.input_index += 1  # Przesunięcie wskaźnika do następnego elementu
        else:
            self.variables[var_name] = 0  # Jeśli lista input_data jest pusta lub nie ma więcej danych, przypisujemy 0

    def _evaluate_expression(self, node: Node):
        """ Obliczenie wartości wyrażenia """
        if node.type == 'literal':
            return self._convert_to_number(node.value)
        elif node.type == 'identifier':
            return self.variables.get(node.value, 0)
        elif node.type == 'expression':
            left = self._evaluate_expression(node.children[0])
            right = self._evaluate_expression(node.children[1])
            operator = node.value

            return self._apply_operator(left, right, operator)

        return 0

    def _convert_to_number(self, value: str):
        """ Przekształcenie wartości do liczby (obsługuje int i float) """
        try:
            if '.' in value:
                return float(value)
            else:
                return int(value)
        except ValueError:
            return 0  # Jeśli nie uda się przekonwertować, zwracamy 0

    def _apply_operator(self, left, right, operator):
        """ Zastosowanie operatora na dwóch operandach """
        try:
            if operator == '+':
                return left + right
            elif operator == '-':
                return left - right
            elif operator == '*':
                return left * right
            elif operator == '/':
                if right == 0:
                    return 0  # Obsługa dzielenia przez zero
                return left / right
            elif operator == '==':
                return int(left == right)
            elif operator == '!=':
                return int(left != right)
            elif operator == '<':
                return int(left < right)
            elif operator == '>':
                return int(left > right)
            elif operator == '<=':
                return int(left <= right)
            elif operator == '>=':
                return int(left >= right)
            elif operator == '&&':
                return int(bool(left) and bool(right))
            elif operator == '||':
                return int(bool(left) or bool(right))
        except Exception as e:
            print(f"Error applying operator {operator}: {e}")
            return 0  # Zwracamy 0 w przypadku błędu

