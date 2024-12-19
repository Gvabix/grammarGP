import sys
from antlr4 import *
from interpreter import InterpreterVisitor
from gen.grammarGPLexer import grammarGPLexer
from gen.grammarGPParser import grammarGPParser


def main():
    input_file = "in.txt"
    output_file = "out.txt"

    lexer = grammarGPLexer(FileStream(input_file))
    stream = CommonTokenStream(lexer)
    parser = grammarGPParser(stream)
    tree = parser.program()

    visitor = InterpreterVisitor(input_file, output_file, max_instructions=1000)
    try:
        visitor.visit(tree)
        print(f"Interpretacja zakończona. Wynik zapisany w {output_file}.")
    except Exception as e:
        print(f"Błąd wykonania: {e}")


if __name__ == "__main__":
    main()
