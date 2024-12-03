import sys
from antlr4 import *
from interpreter import InterpreterVisitor
from gen.grammarGPLexer import grammarGPLexer
from gen.grammarGPParser import grammarGPParser


def main():
    # Ścieżki do plików wejściowego i wyjściowego
    input_file = "input.txt"
    output_file = "output.txt"

    # Wczytaj plik wejściowy
    input_stream = FileStream(input_file)

    # Stwórz lexer, parser i drzewo
    lexer = grammarGPLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = grammarGPParser(stream)
    tree = parser.program()

    # Uruchom interpreter
    visitor = InterpreterVisitor(input_file, output_file)
    visitor.visit(tree)

    print(f"Interpretacja zakończona. Wynik zapisany w {output_file}.")


if __name__ == "__main__":
    main()
