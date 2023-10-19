grammar baby_duck_grammar;

ID: [a-zA-Z] ([a-zA-Z] | [0-9])*;
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;
FLOAT: [0-9]+ '.' [0-9]+;


program: 'program' ID ';' vars? funcs* 'main' body 'end';

body: '{' statement* '}';

statement: assign | condition | cycle | f_call | print;

type: 'int' | 'float';

assign: ID '=' expression ';';

expression: exp (rel_op exp)?;

rel_op: '<' | '>' | '!=';

cte: INT | FLOAT;

exp: term ((('+' | '-') term)*);

print: 'print' '(' print_helper? ')' ';';

print_helper: (expression | STRING) (',' (expression | STRING))*;

f_param_list: (f_param_list_helper (',' f_param_list_helper)*)?;

f_param_list_helper: (ID ':' type);

funcs: 'void' ID '(' f_param_list ')' '[' vars? body ']' ';';

vars: 'var' (ID (',' ID)* ':' type ';')+;

STRING: '"' .*? '"';

cycle: 'while' body 'do' '(' expression ')' ';';

condition: 'if' '(' expression ')' body condition_else? ';';

condition_else: 'else' body;

term: factor term_helper?;

term_helper: '*' term | '/' term;

factor: '(' expression ')' | (('+' | '-')? (ID | cte));

f_call: ID '(' f_call_helper? ')' ';';

f_call_helper: expression (',' expression)*;