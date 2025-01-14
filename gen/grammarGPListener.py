# Generated from grammarGP.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .grammarGPParser import grammarGPParser
else:
    from grammarGPParser import grammarGPParser

# This class defines a complete listener for a parse tree produced by grammarGPParser.
class grammarGPListener(ParseTreeListener):

    # Enter a parse tree produced by grammarGPParser#program.
    def enterProgram(self, ctx:grammarGPParser.ProgramContext):
        pass

    # Exit a parse tree produced by grammarGPParser#program.
    def exitProgram(self, ctx:grammarGPParser.ProgramContext):
        pass


    # Enter a parse tree produced by grammarGPParser#statement.
    def enterStatement(self, ctx:grammarGPParser.StatementContext):
        pass

    # Exit a parse tree produced by grammarGPParser#statement.
    def exitStatement(self, ctx:grammarGPParser.StatementContext):
        pass


    # Enter a parse tree produced by grammarGPParser#block.
    def enterBlock(self, ctx:grammarGPParser.BlockContext):
        pass

    # Exit a parse tree produced by grammarGPParser#block.
    def exitBlock(self, ctx:grammarGPParser.BlockContext):
        pass


    # Enter a parse tree produced by grammarGPParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:grammarGPParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by grammarGPParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:grammarGPParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by grammarGPParser#ifStatement.
    def enterIfStatement(self, ctx:grammarGPParser.IfStatementContext):
        pass

    # Exit a parse tree produced by grammarGPParser#ifStatement.
    def exitIfStatement(self, ctx:grammarGPParser.IfStatementContext):
        pass


    # Enter a parse tree produced by grammarGPParser#loopStatement.
    def enterLoopStatement(self, ctx:grammarGPParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by grammarGPParser#loopStatement.
    def exitLoopStatement(self, ctx:grammarGPParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by grammarGPParser#loopStatementContent.
    def enterLoopStatementContent(self, ctx:grammarGPParser.LoopStatementContentContext):
        pass

    # Exit a parse tree produced by grammarGPParser#loopStatementContent.
    def exitLoopStatementContent(self, ctx:grammarGPParser.LoopStatementContentContext):
        pass


    # Enter a parse tree produced by grammarGPParser#breakStatement.
    def enterBreakStatement(self, ctx:grammarGPParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by grammarGPParser#breakStatement.
    def exitBreakStatement(self, ctx:grammarGPParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by grammarGPParser#continueStatement.
    def enterContinueStatement(self, ctx:grammarGPParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by grammarGPParser#continueStatement.
    def exitContinueStatement(self, ctx:grammarGPParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by grammarGPParser#read.
    def enterRead(self, ctx:grammarGPParser.ReadContext):
        pass

    # Exit a parse tree produced by grammarGPParser#read.
    def exitRead(self, ctx:grammarGPParser.ReadContext):
        pass


    # Enter a parse tree produced by grammarGPParser#write.
    def enterWrite(self, ctx:grammarGPParser.WriteContext):
        pass

    # Exit a parse tree produced by grammarGPParser#write.
    def exitWrite(self, ctx:grammarGPParser.WriteContext):
        pass


    # Enter a parse tree produced by grammarGPParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:grammarGPParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by grammarGPParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:grammarGPParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by grammarGPParser#unaryExpression.
    def enterUnaryExpression(self, ctx:grammarGPParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by grammarGPParser#unaryExpression.
    def exitUnaryExpression(self, ctx:grammarGPParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by grammarGPParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:grammarGPParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by grammarGPParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:grammarGPParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by grammarGPParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:grammarGPParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by grammarGPParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:grammarGPParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by grammarGPParser#relationalExpression.
    def enterRelationalExpression(self, ctx:grammarGPParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by grammarGPParser#relationalExpression.
    def exitRelationalExpression(self, ctx:grammarGPParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by grammarGPParser#equalityExpression.
    def enterEqualityExpression(self, ctx:grammarGPParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by grammarGPParser#equalityExpression.
    def exitEqualityExpression(self, ctx:grammarGPParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by grammarGPParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:grammarGPParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by grammarGPParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:grammarGPParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by grammarGPParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:grammarGPParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by grammarGPParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:grammarGPParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by grammarGPParser#expression.
    def enterExpression(self, ctx:grammarGPParser.ExpressionContext):
        pass

    # Exit a parse tree produced by grammarGPParser#expression.
    def exitExpression(self, ctx:grammarGPParser.ExpressionContext):
        pass


    # Enter a parse tree produced by grammarGPParser#castExpression.
    def enterCastExpression(self, ctx:grammarGPParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by grammarGPParser#castExpression.
    def exitCastExpression(self, ctx:grammarGPParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by grammarGPParser#relation.
    def enterRelation(self, ctx:grammarGPParser.RelationContext):
        pass

    # Exit a parse tree produced by grammarGPParser#relation.
    def exitRelation(self, ctx:grammarGPParser.RelationContext):
        pass


    # Enter a parse tree produced by grammarGPParser#equalityRelation.
    def enterEqualityRelation(self, ctx:grammarGPParser.EqualityRelationContext):
        pass

    # Exit a parse tree produced by grammarGPParser#equalityRelation.
    def exitEqualityRelation(self, ctx:grammarGPParser.EqualityRelationContext):
        pass


    # Enter a parse tree produced by grammarGPParser#unaryOperator.
    def enterUnaryOperator(self, ctx:grammarGPParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by grammarGPParser#unaryOperator.
    def exitUnaryOperator(self, ctx:grammarGPParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by grammarGPParser#literal.
    def enterLiteral(self, ctx:grammarGPParser.LiteralContext):
        pass

    # Exit a parse tree produced by grammarGPParser#literal.
    def exitLiteral(self, ctx:grammarGPParser.LiteralContext):
        pass


    # Enter a parse tree produced by grammarGPParser#identifier.
    def enterIdentifier(self, ctx:grammarGPParser.IdentifierContext):
        pass

    # Exit a parse tree produced by grammarGPParser#identifier.
    def exitIdentifier(self, ctx:grammarGPParser.IdentifierContext):
        pass


    # Enter a parse tree produced by grammarGPParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:grammarGPParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by grammarGPParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:grammarGPParser.TypeSpecifierContext):
        pass



del grammarGPParser