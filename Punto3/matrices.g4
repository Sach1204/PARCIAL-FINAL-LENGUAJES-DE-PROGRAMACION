grammar matrices;

// -------------- Reglas de parser (minúsculas) --------------

prog
    : declList stmtList EOF
    ;

declList
    : decl*
    ;

decl
    : MAT ID '[' NUM ',' NUM ']' ';'
    ;

stmtList
    : stmt*
    ;

stmt
    : assign ';'
    ;

assign
    : ID '=' expr
    ;

expr
    : term (('+' | '-') term)*
    ;

term
    : factor ('*' factor)*
    ;

factor
    : ID
    | '(' expr ')'
    ;

// -------------- Reglas léxicas (MAYÚSCULAS) --------------

MAT : 'mat';

ID  : [a-zA-Z_] [a-zA-Z_0-9]* ;

NUM : [0-9]+ ;

WS  : [ \t\r\n]+ -> skip ;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

