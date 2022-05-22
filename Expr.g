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
        | NOTA                              #Nota
    ;

    
llista : OC (NUM|VAR|NOTA)* CC  ;  

meth : HEADER (VAR)* body                   #Method
    ;

body : OB (instr)* CB                       #ExecuteBody
    ;


instr : WRITE (expr)+                       #Escriu
    | READ VAR                              #Llegeix
    | PLAY expr                             #Play
    | IF cond body                          #If
    | IF cond body ELSE body                #ElseIf
    | WHILE cond body                       #While
    | VAR ASSIG expr                        #Assig
    | HEADER (VAR)*                         #Invoke
    | VAR APPEND expr                       #Append
    | VAR CUT expr                          #Cut
    
    ;

cond : expr EQ expr                         #Equal
    |  expr NEQ expr                        #NotEqual
    |  expr GT expr                         #Greater
    |  expr LT expr                         #Less
    |  expr GE expr                         #GreaterEqual
    |  expr LE expr                         #LessEqual
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

GT : '>';
GE : '>=' ;
LT : '<';
LE : '<=' ;
EQ : '=';
NEQ : '/=';
APPEND : '<<';
THEN : 'then';
END : 'end'; 
WRITE : '<!>';
READ : '<?>';
PLAY : '<:>' ;
ASSIG : '<-';
VAR : [a-z]([a-z]|[A-Z])*;
NUM : [0-9]+ ;
NOTA : [A-G][0-8] ;
BOOLEAN : ('true'| 'false') ;
HEADER : [A-Z]([a-z]|[A-Z])*;
COMMENT : '~~~' .*? '~~~' -> skip ;
PARAULA : '"' .*? '"' ;
HASHTG : '#' ;
CUT : '8<' ;

MES : '+' ;
SUB : '-';
MULT : '*';
DIV : '/';
POW : '^';
WS : [ \n]+ -> skip ;
SPACE : ' '-> skip;
