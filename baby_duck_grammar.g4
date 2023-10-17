grammar baby_duck_grammar;

// Lexer rules
ID: [a-zA-Z]+;
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;

// Parser rules
program: 'program' ID ';' vars? funcs;

funcs_list: funcs funcs_list?;

body: '{' statement* '}';

statement_list: statement statement_list?;

statement: assign | condition | cycle | f_call | print;

type: 'int' | 'float';

assign: ID '=' expression ';';

expression: exp | exp rel_op exp;

rel_op: '<' | '>' | '!=';
cte: INT | 'float';

exp: term (('+' | '-') term)*;

f_param_list: '(' f_param_list_helper ')';

f_param_list_helper:
	ID ':' type
	| ID ':' type ',' f_param_list_helper;

funcs:
	'void' ID '(' f_param_list ')' '[' vars? body ']' ';';

vars: 'var' ID (',' ID)* ':' type ';';


print: 'print' '(' print_helper ')' ';';

STRING: '"' .*? '"';

print_arg: expression | STRING;

print_helper: print_arg print_helper_inner?;

print_helper_inner: ',' print_arg print_helper_inner?;

cycle: 'while' body 'do' '(' expression ')' ';';

condition: 'if' '(' expression ')' body condition_else? ';';

condition_else: 'else' body;

term: factor term_helper?;

term_helper: '*' term | '/' term;

factor: factor_expr | factor_op;

factor_expr: '(' expression ')';

factor_op: '+' ID | '+' cte | '-' ID | '-' cte;

f_call: '(' f_call_helper ')' ';';

f_call_helper: expression_list;

expression_list: expression expression_list_helper?;

expression_list_helper: ',' expression expression_list_helper?;