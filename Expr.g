grammar Expr;
root : instr* EOF ;
expr :                          
	<assoc=right> expr POW expr             #Power
    	| expr (MULT|DIV) expr              #Mult
        | expr MES expr                     #Suma
    	| <assoc=right> expr SUB expr       #Resta
    	| NUM                               #Valor
    	| VAR                               #Var
    ;

meth : VAR params body                      #Method
    ;

body : OB (instr)* CB                       #ExecuteBody
    ;
params : (VAR)*
;

instr : WRITE expr                          #Escriu
    | IF cond body                          #Bool
    | IF cond body ELSE body                #ElseBool
    | WHILE cond body                       #While
    | VAR ASSIG expr                        #Assig
    | 
    ;
cond : expr EQ expr                         #Equal
    |  expr GT expr                         #More
    |  expr LT expr                         #Less
    ;




OP : '(';
CP : ')';
OB : '|:';
CB : ':|';
IDENT : '   ';
IF : 'if';
ELSE : 'else';
WHILE : 'while';
GT : '>';
LT : '<';
EQ : '=';
THEN : 'then';
END : 'end'; 
WRITE : 'write';
ASSIG : '<-';
VAR : [a-z][a-z]*;
NUM : [0-9]+ ;
MES : '+' ;
SUB : '-';
MULT : '*';
DIV : '/';
POW : '^';
WS : [ \n]+ -> skip ;
