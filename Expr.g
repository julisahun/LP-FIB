grammar Expr;
root : (meth)* EOF                          #Main
;

expr :                          
        OP expr CP                          #Parentized
	    | <assoc=right> expr POW expr       #Power
        | expr MOD expr                     #Mod
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

    
llista : OC (NUM|VAR|CHORD|NOTA)* CC  ;  

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
    | VAR ASSIG expr                        #Assign
    | HEADER (expr)*                        #Invoke
    | VAR APPEND expr                       #Append
    | CUT VAR OV expr CV                    #Cut
    | ARMADURA EQ TONO                      #Signature
    | VAR PEIXITU expr                      #Ñam

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
PEIXITU : '><((>';

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
NOTA : ('1'|'2'|'4'|'8'|'16')?[A-G]('#')?[0-8]? ;
CHORD : '<'((NOTA('M'|'m'))|(NOTA ' ')* NOTA)'>' ;
TONO : [A-G]MODO ;
MODO : ('M'|'m') ;
ARMADURA : 'Arm' ;
BOOLEAN : ('true'| 'false') ;
HEADER : [A-Z]([a-z]|[A-Z])*;
COMMENT : '~~~' ~( '\r' | '\n' )* '~~~' -> skip ;
PARAULA : '"' .*? '"' ;
HASHTG : '#' ;
CUT : '8<' ;

MES : '+' ;
SUB : '-';
MULT : '*';
DIV : '/';
POW : '^';
MOD : '%' ;
WS : [ \n]+ -> skip ;
SPACE : ' '-> skip;
