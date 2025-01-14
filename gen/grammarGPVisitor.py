# Generated from grammarGP.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from grammarGPParser import grammarGPParser
else:
    from grammarGPParser import grammarGPParser

# This class defines a complete generic visitor for a parse tree produced by grammarGPParser.

class grammarGPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by grammarGPParser#program.
    def visitProgram(self, ctx:grammarGPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#statement.
    def visitStatement(self, ctx:grammarGPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#block.
    def visitBlock(self, ctx:grammarGPParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:grammarGPParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#ifStatement.
    def visitIfStatement(self, ctx:grammarGPParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#loopStatement.
    def visitLoopStatement(self, ctx:grammarGPParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#loopStatementContent.
    def visitLoopStatementContent(self, ctx:grammarGPParser.LoopStatementContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#breakStatement.
    def visitBreakStatement(self, ctx:grammarGPParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#continueStatement.
    def visitContinueStatement(self, ctx:grammarGPParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#read.
    def visitRead(self, ctx:grammarGPParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#write.
    def visitWrite(self, ctx:grammarGPParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:grammarGPParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#unaryExpression.
    def visitUnaryExpression(self, ctx:grammarGPParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:grammarGPParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:grammarGPParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#relationalExpression.
    def visitRelationalExpression(self, ctx:grammarGPParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#equalityExpression.
    def visitEqualityExpression(self, ctx:grammarGPParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:grammarGPParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:grammarGPParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#expression.
    def visitExpression(self, ctx:grammarGPParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#castExpression.
    def visitCastExpression(self, ctx:grammarGPParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#relation.
    def visitRelation(self, ctx:grammarGPParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#equalityRelation.
    def visitEqualityRelation(self, ctx:grammarGPParser.EqualityRelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#unaryOperator.
    def visitUnaryOperator(self, ctx:grammarGPParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#literal.
    def visitLiteral(self, ctx:grammarGPParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#identifier.
    def visitIdentifier(self, ctx:grammarGPParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGPParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:grammarGPParser.TypeSpecifierContext):
        return self.visitChildren(ctx)



del grammarGPParser