grammar baby_duck_grammar;
// Francisco Zamora Treviño A01570484
ID: [a-zA-Z] ([a-zA-Z] | [0-9])*;
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;
FLOAT: [0-9]+ '.' [0-9]+;
string: '"'*?'"';

program: 'program' ID ';' vars? program_post_var;

program_post_var: funcs* 'main' body 'end';

body: '{' statement* '}';

statement: assign | condition | cycle | f_call | print;

type: 'int' | 'float' | 'bool' | 'void';

assign: ID '=' expression ';';

expression: exp (rel_op expression)?;

rel_op: '<' | '>' | '!=' | '==' | '<=' | '>=c';

cte: INT | FLOAT;

print: 'print' '(' print_helper ')' ';';

print_helper: (expression | string) (',' (expression | string))*;

f_param_list: (f_param_list_helper (',' f_param_list_helper)*)?;

f_param_list_helper: (ID ':' type);

funcs: function_id '(' f_param_list ')' '[' vars? body ']' ';';

function_id: type ID;

vars: 'var' vars_declarations+;

vars_declarations: (ID (',' ID)* ':' type ';');

cycle:   'do' body 'while' '(' expression ')' ';';

while_keyword: 'while';

condition: 'if' '(' expression ')' body condition_else? ';';

condition_else: 'else' body;

operator: ('+' | '-');

exp: term (operator exp)?;

term: factor (term_operator term)?;

term_operator: ('*' | '/');

factor: parenthesized_expression | (factor_operator? (ID | cte));

factor_operator: ('+' | '-');

parenthesized_expression: '(' expression ')';

f_call: ID '(' f_call_helper? ')' ';';

f_call_helper: expression (',' expression)*;