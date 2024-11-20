// Generated from C:/Users/emili/Desktop/gene2/genetic_programming/grammar/grammarGP.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link grammarGPParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface grammarGPVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(grammarGPParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#block}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBlock(grammarGPParser.BlockContext ctx);
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatement(grammarGPParser.StatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#assignmentStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignmentStatement(grammarGPParser.AssignmentStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#ifStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfStatement(grammarGPParser.IfStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#loopStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLoopStatement(grammarGPParser.LoopStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#read}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRead(grammarGPParser.ReadContext ctx);
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#write}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWrite(grammarGPParser.WriteContext ctx);
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#primaryExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrimaryExpression(grammarGPParser.PrimaryExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#unaryExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnaryExpression(grammarGPParser.UnaryExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#multiplicativeExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMultiplicativeExpression(grammarGPParser.MultiplicativeExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#additiveExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAdditiveExpression(grammarGPParser.AdditiveExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#relationalExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRelationalExpression(grammarGPParser.RelationalExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#equalityExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEqualityExpression(grammarGPParser.EqualityExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#logicalAndExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLogicalAndExpression(grammarGPParser.LogicalAndExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#logicalOrExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLogicalOrExpression(grammarGPParser.LogicalOrExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(grammarGPParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#castExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCastExpression(grammarGPParser.CastExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#relation}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRelation(grammarGPParser.RelationContext ctx);
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#equalityRelation}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEqualityRelation(grammarGPParser.EqualityRelationContext ctx);
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#unaryOperator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnaryOperator(grammarGPParser.UnaryOperatorContext ctx);
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#literal}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLiteral(grammarGPParser.LiteralContext ctx);
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#identifier}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIdentifier(grammarGPParser.IdentifierContext ctx);
	/**
	 * Visit a parse tree produced by {@link grammarGPParser#typeSpecifier}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypeSpecifier(grammarGPParser.TypeSpecifierContext ctx);
}