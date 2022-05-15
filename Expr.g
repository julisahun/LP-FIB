grammar Expr;
root : (meth)* EOF ;

expr :                          
	<assoc=right> expr POW expr             #Power
    	| expr (MULT|DIV) expr              #Mult
        | expr MES expr                     #Suma
    	| <assoc=right> expr SUB expr       #Resta
    	| NUM                               #Valor
        | list                              #Llista
    	| VAR                               #Var
    ;

list : OP NUM* CP
;
meth : VAR (VAR)* body                      #Method
    ;

body : OB (instr)* CB                       #ExecuteBody
    ;

instr : WRITE expr                          #Escriu
    | READ VAR                              #Llegeix
    | IF cond body                          #Bool
    | IF cond body ELSE body                #ElseBool
    | WHILE cond body                       #While
    | VAR ASSIG expr                        #Assig
    | VAR (VAR)*                            #Invoke
    ;

cond : expr EQ expr                         #Equal
    |  expr NEQ expr                        #NotEqual
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
WHILE : '<!>';
READ : '<?>';
GT : '>';
LT : '<';
EQ : '=';
NEQ : '/=';
THEN : 'then';
END : 'end'; 
WRITE : 'write';
ASSIG : '<-';
VAR : [a-z]+;
NUM : [0-9]+ ;
LLISTA : '{' ([0-9]',')* [0-9] '}' ;
COMMENT : '~~~' .*? '~~~' -> skip ;
ANYCHAR : [^~]*;

MES : '+' ;
SUB : '-';
MULT : '*';
DIV : '/';
POW : '^';
WS : [ \n]+ -> skip ;
