grammar Expr;
root : (meth)* EOF                          #Main
;

expr :                          
	<assoc=right> expr POW expr             #Power
    	| expr (MULT|DIV) expr              #Mult
        | expr MES expr                     #Suma
    	| <assoc=right> expr SUB expr       #Resta
    	| NUM                               #Valor
        | llista                            #Array
    	| VAR                               #Var
        | VAR OV expr CV                    #Acces
        | HASHTG VAR                        #Length
        | PARAULA                           #Paraula
    ;

    
llista : OC (NUM|VAR)* CC  ;  

meth : HEADER (VAR)* body                   #Method
    ;

body : OB (instr)* CB                       #ExecuteBody
    ;


instr : WRITE expr                          #Escriu
    | READ VAR                              #Llegeix
    | IF cond body                          #Bool
    | IF cond body ELSE body                #ElseBool
    | WHILE cond body                       #While
    | VAR ASSIG expr                        #Assig
    | HEADER (VAR)*                         #Invoke
    | VAR APPEND expr                       #Append
    | VAR CUT expr                          #Cut
    ;

cond : expr EQ expr                         #Equal
    |  expr NEQ expr                        #NotEqual
    |  expr GT expr                         #More
    |  expr LT expr                         #Less
    ;


OP : '(';
CP : ')';
OV : '[';
CV : ']';
OC : '{';
CC : '}';
OB : '|:';
CB : ':|';
IDENT : '   ';
IF : 'if';
ELSE : 'else';
WHILE : 'while';
READ : '<?>';
GT : '>';
LT : '<';
EQ : '=';
NEQ : '/=';
APPEND : '<<';
THEN : 'then';
END : 'end'; 
WRITE : '<!>';
ASSIG : '<-';
VAR : [a-z]+;
NUM : [0-9]+ ;
HEADER : [A-Z][a-z]*;
COMMENT : '~~~' .*? '~~~' -> skip ;
PARAULA : '"' ([a-z]|[A-Z]|' ')* '"' ;
HASHTG : '#' ;
CUT : '8<' ;

MES : '+' ;
SUB : '-';
MULT : '*';
DIV : '/';
POW : '^';
WS : [ \n]+ -> skip ;
SPACE : ' '-> skip;
