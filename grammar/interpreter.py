import sys
from antlr4 import *
from grammarGPLexer import grammarGPLexer
from grammarGPParser import grammarGPParser
from grammarGPVisitor import grammarGPVisitor

class RuntimeEnvironment:
    def __init__(self):
        self.variables = {}
        self.loop_control = None  # Tracks 'break' or 'continue' signals

    def set_variable(self, name, value):
        self.variables[name] = value

    def get_variable(self, name):
        if name in self.variables:
            return self.variables[name]
        else:
            raise Exception(f"Variable '{name}' is not defined.")

class Interpreter(grammarGPVisitor):
    def __init__(self):
        self.env = RuntimeEnvironment()

    def visitProgram(self, ctx):
        for statement in ctx.statement():
            self.visit(statement)

    def visitAssignmentStatement(self, ctx):
        name = ctx.identifier().getText()
        value = self.visit(ctx.expression())
        self.env.set_variable(name, value)

    def visitIfStatement(self, ctx):
        condition = self.visit(ctx.expression())
        if condition:
            self.visit(ctx.statement(0))
        elif ctx.ELSE():
            self.visit(ctx.statement(1))

    def visitLoopStatement(self, ctx):
        while self.visit(ctx.expression()):
            self.visit(ctx.block())
            if self.env.loop_control == 'break':
                self.env.loop_control = None
                break
            elif self.env.loop_control == 'continue':
                self.env.loop_control = None
                continue

    def visitBreakStatement(self, ctx):
        self.env.loop_control = 'break'

    def visitContinueStatement(self, ctx):
        self.env.loop_control = 'continue'

    def visitRead(self, ctx):
        var_name = ctx.identifier().getText()
        value = int(input(f"Enter value for {var_name}: "))
        self.env.set_variable(var_name, value)

    def visitWrite(self, ctx):
        value = self.visit(ctx.expression())
        print(value)

    def visitExpression(self, ctx):
        return self.visit(ctx.logicalOrExpression())

    def visitLogicalOrExpression(self, ctx):
        if ctx.OR():
            return self.visit(ctx.logicalAndExpression(0)) or self.visit(ctx.logicalAndExpression(1))
        else:
            return self.visit(ctx.logicalAndExpression(0))

    def visitLogicalAndExpression(self, ctx):
        if ctx.AND():
            return self.visit(ctx.equalityExpression(0)) and self.visit(ctx.equalityExpression(1))
        else:
            return self.visit(ctx.equalityExpression(0))

    def visitEqualityExpression(self, ctx):
        left = self.visit(ctx.relationalExpression(0))
        right = self.visit(ctx.relationalExpression(1))
        if ctx.EQ():
            return left == right
        elif ctx.NE():
            return left != right

    def visitRelationalExpression(self, ctx):
        left = self.visit(ctx.additiveExpression(0))
        right = self.visit(ctx.additiveExpression(1))
        if ctx.LT():
            return left < right
        elif ctx.GT():
            return left > right
        elif ctx.LE():
            return left <= right
        elif ctx.GE():
            return left >= right

    def visitAdditiveExpression(self, ctx):
        left = self.visit(ctx.multiplicativeExpression(0))
        if ctx.PLUS():
            return left + self.visit(ctx.multiplicativeExpression(1))
        elif ctx.MINUS():
            return left - self.visit(ctx.multiplicativeExpression(1))

    def visitMultiplicativeExpression(self, ctx):
        left = self.visit(ctx.unaryExpression(0))
        if ctx.TIMES():
            return left * self.visit(ctx.unaryExpression(1))
        elif ctx.DIV():
            return left // self.visit(ctx.unaryExpression(1))

    def visitUnaryExpression(self, ctx):
        if ctx.unaryOperator():
            if ctx.unaryOperator().PLUS():
                return self.visit(ctx.primaryExpression())
            elif ctx.unaryOperator().MINUS():
                return -self.visit(ctx.primaryExpression())
        else:
            return self.visit(ctx.primaryExpression())

    def visitPrimaryExpression(self, ctx):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.identifier():
            return self.env.get_variable(ctx.identifier().getText())

    def visitLiteral(self, ctx):
        if ctx.INTEGER_LITERAL():
            return int(ctx.INTEGER_LITERAL().getText())
        elif ctx.FLOAT_LITERAL():
            return float(ctx.FLOAT_LITERAL().getText())

def main():
    input_stream = FileStream(sys.argv[1])
    lexer = grammarGPLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = grammarGPParser(stream)
    tree = parser.program()

    interpreter = Interpreter()
    interpreter.visit(tree)

if __name__ == "__main__":
    main()
