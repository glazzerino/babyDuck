grammar baby_duck_grammar;
// Francisco Zamora Treviño A01570484
ID: [a-zA-Z] ([a-zA-Z] | [0-9])*;
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"';

program: 'program' ID ';' vars? program_post_var;

program_post_var: funcs* 'main' body 'end';

body: '{' statement* '}';

statement: assign | condition | cycle | f_call | print;

type: 'int' | 'float' | 'bool' | 'void';

assign: ID '=' expression ';';

expression: exp (rel_op exp)?;

rel_op: '<' | '>' | '!=';

cte: INT | FLOAT;

exp: term (('+' | '-') term)*;

print: 'print' '(' print_helper? ')' ';';

print_helper: (expression | STRING) (',' (expression | STRING))*;

f_param_list: (f_param_list_helper (',' f_param_list_helper)*)?;

f_param_list_helper: (ID ':' type);

funcs: type ID '(' f_param_list ')' '[' vars? body ']' ';';

vars: 'var' vars_declarations+;

vars_declarations: (ID (',' ID)* ':' type ';');

cycle: 'while' body 'do' '(' expression ')' ';';

condition: 'if' '(' expression ')' body condition_else? ';';

condition_else: 'else' body;

term: factor (('*' | '/') factor)?;

factor: '(' expression ')' | (('+' | '-')? (ID | cte));

f_call: ID '(' f_call_helper? ')' ';';

f_call_helper: expression (',' expression)*;