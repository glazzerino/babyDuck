grammar superduck;
program: expression*;
expression: equality;
equality: comparison ( ( '!=' | '==') comparison)*;
comparison: term ( ( '>' | '>=' | '<' | '<=') term)*;
term: factor ( ( '-' | '+') factor)*;
factor: unary ( ( '/' | '*') unary)*;
unary: ( '!' | '-') unary | primary;
primary:
	NUMBER
	| STRING
	| 'true'
	| 'false'
	| '(' expression ')';

NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING: '"' (~["])* '"';

WS: [ \t\r\n]+ -> skip;