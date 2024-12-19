import sys
import os
from antlr4 import *
from gen.grammarGPLexer import grammarGPLexer
from gen.grammarGPParser import grammarGPParser
from gen.grammarGPVisitor import grammarGPVisitor

sys.path.append(os.path.abspath(""))


class Variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    @staticmethod
    def create_and_assign(name, value):
        return Variable(name, value)

    def on_assign(self, new_value):
        self.value = new_value


class VariableMemory:
    def __init__(self):
        self.memory = {}

    def assign_variable(self, name, value):
        self.memory[name] = value

    def get_variable_value(self, name):
        if name in self.memory:
            return self.memory[name]
        else:
            raise Exception(f"Variable '{name}' is not defined.")


import random

class InterpreterVisitor(grammarGPVisitor):
    def __init__(self, in_path: str, out_path: str, max_instructions: int = 1000, max_output: int = 100):
        super().__init__()
        self.in_file = open(in_path, "r")
        self.out_file = open(out_path, "w+")
        self.variable_memory = VariableMemory()
        self.loop_control = None
        self.instruction_count = 0
        self.max_instructions = max_instructions
        self.output_count = 0
        self.max_output = max_output

    def visit(self, node):
        self.instruction_count += 1
        if self.instruction_count > self.max_instructions:
            raise Exception("Przekroczono maksymalną liczbę instrukcji!")
        return super().visit(node)

    def visitProgram(self, ctx: grammarGPParser.ProgramContext):
        self.visitChildren(ctx)

    def visitBlock(self, ctx: grammarGPParser.BlockContext):
        self.visitChildren(ctx)

    def visitStatement(self, ctx: grammarGPParser.StatementContext):
        for child in ctx.children:
            if self.loop_control:
                break
            self.visit(child)

    def visitAssignmentStatement(self, ctx: grammarGPParser.AssignmentStatementContext):
        identifier = ctx.identifier().getText()
        value = self.visit(ctx.expression())
        self.variable_memory.assign_variable(identifier, value)

    def visitIfStatement(self, ctx: grammarGPParser.IfStatementContext):
        condition = self.visit(ctx.expression())
        if condition:
            self.visit(ctx.statement(0))
        elif ctx.ELSE():
            self.visit(ctx.statement(1))

    def visitLoopStatement(self, ctx: grammarGPParser.LoopStatementContext):
        while self.visit(ctx.expression()):
            self.loop_control = None
            self.visit(ctx.block())
            if self.loop_control == "break":
                break
            if self.loop_control == "continue":
                continue

    def visitBreakStatement(self, ctx: grammarGPParser.BreakStatementContext):
        self.loop_control = "break"

    def visitContinueStatement(self, ctx: grammarGPParser.ContinueStatementContext):
        self.loop_control = "continue"

    def visitRead(self, ctx: grammarGPParser.ReadContext):
        identifier = ctx.identifier().getText()
        try:
            value = self.in_file.readline().strip()
            if not value:
                raise ValueError("Brak danych wejściowych w pliku!")
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    value = 0
        except ValueError as e:
            print(f"Błąd: {e}")
            value = 0
        self.variable_memory.assign_variable(identifier, value)

    def visitWrite(self, ctx: grammarGPParser.WriteContext):
        if self.output_count >= self.max_output:
            raise Exception("Przekroczono maksymalny limit danych wyjściowych!")
        value = self.visit(ctx.expression())
        self.out_file.write(str(value) + "\n")
        self.output_count += 1

    def visitExpression(self, ctx: grammarGPParser.ExpressionContext):
        return self.visit(ctx.logicalOrExpression())

    def visitPrimaryExpression(self, ctx: grammarGPParser.PrimaryExpressionContext):
        if ctx.identifier():
            identifier = ctx.identifier().getText()
            # Jeśli zmienna nie została zadeklarowana, przypisz jej losową wartość
            try:
                return self.variable_memory.get_variable_value(identifier)
            except Exception:
                # Losowa wartość w zakresie -100 do 100
                random_value = random.randint(-100, 100)
                self.variable_memory.assign_variable(identifier, random_value)
                return random_value
        elif ctx.literal():
            if ctx.literal().INTEGER_LITERAL():
                return int(ctx.literal().getText())
            elif ctx.literal().FLOAT_LITERAL():
                return float(ctx.literal().getText())
        elif ctx.LPAREN():
            return self.visit(ctx.expression())

    def visitUnaryExpression(self, ctx: grammarGPParser.UnaryExpressionContext):
        value = self.visit(ctx.primaryExpression())
        if ctx.unaryOperator():
            operator = ctx.unaryOperator().getText()
            if operator == "-":
                return -value
            elif operator == "!":
                return not value
        return value

    def visitMultiplicativeExpression(self, ctx: grammarGPParser.MultiplicativeExpressionContext):
        result = self.visit(ctx.unaryExpression(0))
        for i in range(1, len(ctx.unaryExpression())):
            operator = ctx.getChild(2 * i - 1).getText()
            value = self.visit(ctx.unaryExpression(i))
            if operator == "*":
                result *= value
            elif operator == "/":
                result /= value
        return result

    def visitAdditiveExpression(self, ctx: grammarGPParser.AdditiveExpressionContext):
        result = self.visit(ctx.multiplicativeExpression(0))
        for i in range(1, len(ctx.multiplicativeExpression())):
            operator = ctx.getChild(2 * i - 1).getText()
            value = self.visit(ctx.multiplicativeExpression(i))
            if operator == "+":
                result += value
            elif operator == "-":
                result -= value
        return result

    def visitRelationalExpression(self, ctx: grammarGPParser.RelationalExpressionContext):
        left = self.visit(ctx.additiveExpression(0))
        if ctx.relation():
            operator = ctx.relation().getText()
            right = self.visit(ctx.additiveExpression(1))
            if operator == "<":
                return left < right
            elif operator == "<=":
                return left <= right
            elif operator == ">":
                return left > right
            elif operator == ">=":
                return left >= right
        return left

    def visitEqualityExpression(self, ctx: grammarGPParser.EqualityExpressionContext):
        left = self.visit(ctx.relationalExpression(0))
        if ctx.equalityRelation():
            operator = ctx.equalityRelation().getText()
            right = self.visit(ctx.relationalExpression(1))
            if operator == "==":
                return left == right
            elif operator == "!=":
                return left != right
        return left

    def visitLogicalAndExpression(self, ctx: grammarGPParser.LogicalAndExpressionContext):
        result = self.visit(ctx.equalityExpression(0))
        for i in range(1, len(ctx.equalityExpression())):
            if not result:
                break
            result = result and self.visit(ctx.equalityExpression(i))
        return result

    def visitLogicalOrExpression(self, ctx: grammarGPParser.LogicalOrExpressionContext):
        result = self.visit(ctx.logicalAndExpression(0))
        for i in range(1, len(ctx.logicalAndExpression())):
            if result:
                break
            result = result or self.visit(ctx.logicalAndExpression(i))
        return result

    def visitCastExpression(self, ctx: grammarGPParser.CastExpressionContext):
        value = self.visit(ctx.expression())
        if ctx.typeSpecifier().INT():
            return int(value)
        elif ctx.typeSpecifier().FLOAT():
            return float(value)
        return value
