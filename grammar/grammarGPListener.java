// Generated from C:/Users/emili/Desktop/gene2/genetic_programming/grammar/grammarGP.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link grammarGPParser}.
 */
public interface grammarGPListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(grammarGPParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(grammarGPParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(grammarGPParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(grammarGPParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(grammarGPParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(grammarGPParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#assignmentStatement}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentStatement(grammarGPParser.AssignmentStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#assignmentStatement}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentStatement(grammarGPParser.AssignmentStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(grammarGPParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(grammarGPParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#loopStatement}.
	 * @param ctx the parse tree
	 */
	void enterLoopStatement(grammarGPParser.LoopStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#loopStatement}.
	 * @param ctx the parse tree
	 */
	void exitLoopStatement(grammarGPParser.LoopStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#read}.
	 * @param ctx the parse tree
	 */
	void enterRead(grammarGPParser.ReadContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#read}.
	 * @param ctx the parse tree
	 */
	void exitRead(grammarGPParser.ReadContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#write}.
	 * @param ctx the parse tree
	 */
	void enterWrite(grammarGPParser.WriteContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#write}.
	 * @param ctx the parse tree
	 */
	void exitWrite(grammarGPParser.WriteContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryExpression(grammarGPParser.PrimaryExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryExpression(grammarGPParser.PrimaryExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#unaryExpression}.
	 * @param ctx the parse tree
	 */
	void enterUnaryExpression(grammarGPParser.UnaryExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#unaryExpression}.
	 * @param ctx the parse tree
	 */
	void exitUnaryExpression(grammarGPParser.UnaryExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#multiplicativeExpression}.
	 * @param ctx the parse tree
	 */
	void enterMultiplicativeExpression(grammarGPParser.MultiplicativeExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#multiplicativeExpression}.
	 * @param ctx the parse tree
	 */
	void exitMultiplicativeExpression(grammarGPParser.MultiplicativeExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#additiveExpression}.
	 * @param ctx the parse tree
	 */
	void enterAdditiveExpression(grammarGPParser.AdditiveExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#additiveExpression}.
	 * @param ctx the parse tree
	 */
	void exitAdditiveExpression(grammarGPParser.AdditiveExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#relationalExpression}.
	 * @param ctx the parse tree
	 */
	void enterRelationalExpression(grammarGPParser.RelationalExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#relationalExpression}.
	 * @param ctx the parse tree
	 */
	void exitRelationalExpression(grammarGPParser.RelationalExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#equalityExpression}.
	 * @param ctx the parse tree
	 */
	void enterEqualityExpression(grammarGPParser.EqualityExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#equalityExpression}.
	 * @param ctx the parse tree
	 */
	void exitEqualityExpression(grammarGPParser.EqualityExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#logicalAndExpression}.
	 * @param ctx the parse tree
	 */
	void enterLogicalAndExpression(grammarGPParser.LogicalAndExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#logicalAndExpression}.
	 * @param ctx the parse tree
	 */
	void exitLogicalAndExpression(grammarGPParser.LogicalAndExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#logicalOrExpression}.
	 * @param ctx the parse tree
	 */
	void enterLogicalOrExpression(grammarGPParser.LogicalOrExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#logicalOrExpression}.
	 * @param ctx the parse tree
	 */
	void exitLogicalOrExpression(grammarGPParser.LogicalOrExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(grammarGPParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(grammarGPParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#castExpression}.
	 * @param ctx the parse tree
	 */
	void enterCastExpression(grammarGPParser.CastExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#castExpression}.
	 * @param ctx the parse tree
	 */
	void exitCastExpression(grammarGPParser.CastExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#relation}.
	 * @param ctx the parse tree
	 */
	void enterRelation(grammarGPParser.RelationContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#relation}.
	 * @param ctx the parse tree
	 */
	void exitRelation(grammarGPParser.RelationContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#equalityRelation}.
	 * @param ctx the parse tree
	 */
	void enterEqualityRelation(grammarGPParser.EqualityRelationContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#equalityRelation}.
	 * @param ctx the parse tree
	 */
	void exitEqualityRelation(grammarGPParser.EqualityRelationContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#unaryOperator}.
	 * @param ctx the parse tree
	 */
	void enterUnaryOperator(grammarGPParser.UnaryOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#unaryOperator}.
	 * @param ctx the parse tree
	 */
	void exitUnaryOperator(grammarGPParser.UnaryOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(grammarGPParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(grammarGPParser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#identifier}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(grammarGPParser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#identifier}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(grammarGPParser.IdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarGPParser#typeSpecifier}.
	 * @param ctx the parse tree
	 */
	void enterTypeSpecifier(grammarGPParser.TypeSpecifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarGPParser#typeSpecifier}.
	 * @param ctx the parse tree
	 */
	void exitTypeSpecifier(grammarGPParser.TypeSpecifierContext ctx);
}