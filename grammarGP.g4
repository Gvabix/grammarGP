grammar grammarGP;

program     :  statement* EOF;

statement   : assignmentStatement
            | loopStatement
            | ifStatement
            | read
            | write
            ;

block : LBRACE loopStatementContent* RBRACE ;

assignmentStatement
            : typeSpecifier? identifier ASSIGN expression SEMI;

ifStatement : IF LPAREN expression RPAREN block (ELSE LBRACE loopStatementContent* RBRACE)?;

loopStatement
            : WHILE LPAREN expression RPAREN block;


loopStatementContent
            : assignmentStatement
            | ifStatement
            | read
            | write
            | breakStatement
            | continueStatement
            | loopStatement
            ;

breakStatement : BREAK SEMI;

continueStatement : CONTINUE SEMI;

read        : READ LPAREN identifier RPAREN SEMI;

write       : WRITE LPAREN expression RPAREN SEMI;

primaryExpression
            : literal
            | identifier
            | castExpression
            | LPAREN expression RPAREN
            ;

unaryExpression
            : unaryOperator primaryExpression
            | primaryExpression;

multiplicativeExpression
            : unaryExpression ((TIMES | DIV) unaryExpression)*
            ;

additiveExpression
            : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*
            ;

relationalExpression
            : additiveExpression (relation additiveExpression)?
            ;

equalityExpression
            : relationalExpression (equalityRelation relationalExpression)?
            ;

logicalAndExpression
            : equalityExpression (AND equalityExpression)?
            ;

logicalOrExpression
            : logicalAndExpression (OR logicalAndExpression)?
            ;

expression  : logicalOrExpression;

castExpression
            : typeSpecifier LPAREN expression RPAREN;

relation    : LT | LE | GT | GE;

equalityRelation
            : EQ | NE;

unaryOperator
            : PLUS | MINUS | NOT;

literal     : INTEGER_LITERAL
            | FLOAT_LITERAL
            ;

identifier  : IDENTIFIER;

typeSpecifier
            : INT
            | FLOAT
            ;

COMMA: ',';
DOT: '.';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';

PLUS: '+';
MINUS: '-';
TIMES: '*';
DIV: '/';

ASSIGN: '=';
SEMI: ';';

INTEGER_LITERAL : DEC_DIGIT+;
FLOAT_LITERAL   : INTEGER_LITERAL DOT INTEGER_LITERAL;

IF: 'if';
ELSE: 'else';
WHILE: 'while';
READ: 'read';
WRITE: 'write';
BREAK: 'break';
CONTINUE: 'continue';

AND: '&&';
OR: '||';

INT: 'int';
FLOAT: 'float';

EQ: '==';
NE: '!=';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
NOT: '!';

IDENTIFIER
    : LETTER (LETTER | DIGIT)*
    ;
WS          : [ \t\r\n]+ -> skip;
DIGIT       : [0-9]+;
LETTER      : [a-zA-Z_]+;

fragment DEC_DIGIT: [0-9];
