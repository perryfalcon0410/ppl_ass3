// My ID: 1953096

grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: class_decl+ EOF; // class_program? class_decl* EOF ;

// Normal class declaration
class_decl              : class_type;
class_type              : CLASS ID (COLON ID)? class_block;
class_block             : LP class_stmt* RP;
class_stmt              : attr_decl
                       | method_decl
                       | constructor
                       | destructor;

// Attribute and method declaration together with constructor - destructor
attr_decl               : (VAR | VAL) (attr_decl_1 | attr_decl_2);
method_decl             : (DOLLAR_ID | ID) LB list_param? RB stmt_block;
constructor             : CONSTRUCTOR LB list_param? RB stmt_block;
destructor              : DESTRUCTOR LB RB stmt_block;

// Parser associate with attr_decl
attr_decl_1             : idList COLON typeDeclaration SEMI;
attr_decl_2             : id_type extend_1 expr SEMI;
extend_1                : COMMA id_type extend_1 expr COMMA | COLON typeDeclaration EQ;

id_type                 : DOLLAR_ID | ID;
idList                  : id_type (COMMA id_type)*;

nor_id_type             : ID;
nor_idList              : nor_id_type (COMMA nor_id_type)*;

vari_decl_1             : nor_idList COLON typeDeclaration SEMI;
vari_decl_2             : nor_id_type extend_2 expr SEMI;
extend_2                : COMMA nor_id_type extend_2 expr COMMA | COLON typeDeclaration EQ;

typeDeclaration         : (K_BOOLEAN | K_INT | K_FLOAT | K_STRING | array_type | ID);
typeDeclaration2        : (K_BOOLEAN | K_INT | K_FLOAT | K_STRING | array_type);
array_type              : KARRAY LEFTB (typeDeclaration2 COMMA INT2)? RIGHTB;

// Parser associate with method_decl
list_param              : param_decl (SEMI param_decl)*;
param_decl              : nor_idList COLON typeDeclaration;

// Statement block
stmt_block              : LP stmt* RP;
stmt_block_ret          : LP stmt* RP;

stmt                    : assign_stmt
                       | if_stmt
                       | continue_stmt
                       | break_stmt
                       | for_each_stmt
                       | return_stmt
                       | method_inv_stmt
                       | stmt_block_ret
                       | vari_decl;

/*--------------------------------Begin set of statements-------------------------------------------------------------*/
// Variable and Constant Declaration statement
vari_decl               : (VAR | VAL) (vari_decl_1 | vari_decl_2);

// Assignment Statement
assign_stmt             : (expr8 index_op | ID | member_access_attribute) EQ expr SEMI;

// If statement
if_stmt                 : IF condition_block elseif_blocks;
condition_block         : expr stmt_block;
elseif_block            : ELSEIF expr stmt_block;
elseif_blocks           : elseif_block elseif_blocks | else_block?;
else_block              : ELSE stmt_block;

// For/In statment
for_each_stmt           : FOREACH LB (expr8 index_op | ID | member_access_attribute)
                       IN expr DOTDOT expr (BY expr)? RB stmt_block; // TODO: bring the scalar var

// Break statement
break_stmt              : BREAK SEMI;

// Continue statement
continue_stmt           : CONTINUE SEMI;

// Return statement
return_stmt             : RETURN expr? SEMI;

// Method Invocation statement
method_inv_stmt         : member_access_method SEMI;

// New statement
new_stmt                : NEW ID LB list_expr? RB SEMI; // TODO
/*--------------------------------End set of statements---------------------------------------------------------------*/

expr                    : expr1 (ADD_STRING | EQ_STRING) expr1 | expr1;
expr1                   : expr2 (EQ_COMPARE | NOT_EQ_COMPARE | SMALLER | GREATER | SM_OR_EQ | GR_OR_EQ) expr2 | expr2;
expr2                   : expr2 (AND_ | OR_) expr3 | expr3;
expr3                   : expr3 (ADD_ | MINUS_) expr4 | expr4;
expr4                   : expr4 (MUL_ | DIV_ | MOD_ ) expr5 | expr5;
expr5                   : <assoc=right> EXCLAMATION_ expr5 | expr6;
expr6                   : <assoc=right> MINUS_ expr6 | expr7;
expr7                   : expr8 index_op | expr8;
expr8                   : expr8 DOT ID (LB list_expr? RB)? | expr9;
expr9                   : ID COLONCOLON DOLLAR_ID (LB list_expr? RB)? | expr10;
expr10                  : NEW ID LB list_expr? RB | primary;

primary                 : ID
                       | SELF
                       | literal
                       | INT2
                       | LB expr RB
                       | TRUE
                       | FALSE
                       | NULL;

list_expr               : expr (COMMA expr)*;

// Index operation of array: array[1][2]
index_op                : (LEFTB expr RIGHTB)+;

// Member access from outer class: Shape::?getArea()
member_access_attribute : expr8 DOT ID
                       | ID COLONCOLON DOLLAR_ID;
member_access_method    : expr8 DOT ID LB list_expr? RB
                       | ID COLONCOLON DOLLAR_ID LB list_expr? RB;

// Literal: 1 --> INT. "asd" --> STRING
literal                 : INT
                       | BOOLEAN
                       | FLOAT
                       | STRING
                       | iarray; // TODO: literal

// Indexed Array & Multi-dim Array
farray                  : int_array | float_array | string_array | boolean_array | expr_array;
expr_array              : KARRAY LB (expr (COMMA expr)*)? RB;
int_int2                : INT | INT2;
int_array               : KARRAY LB (int_int2 (COMMA int_int2)*)? RB;
float_array             : KARRAY LB (FLOAT (COMMA FLOAT)*)? RB;
string_array            : KARRAY LB (STRING (COMMA STRING)*)? RB;
boolean_array           : KARRAY LB (BOOLEAN (COMMA BOOLEAN)*)? RB;

iarray                  : farray | marray;

marray                  : KARRAY LB (iarray (COMMA iarray)*)? RB; // TODO

// Keyword
BREAK                   : 'Break';
CONTINUE                : 'Continue';
IF                      : 'If';
ELSEIF                  : 'Elseif';
ELSE                    : 'Else';
FOREACH                 : 'Foreach';
TRUE                    : 'True';
FALSE                   : 'False';
KARRAY                  : 'Array';
IN                      : 'In';
K_INT                   : 'Int';
K_FLOAT                 : 'Float';
K_BOOLEAN               : 'Boolean';
K_STRING                : 'String';
RETURN                  : 'Return';
NULL                    : 'Null';
CLASS                   : 'Class';
VAR                     : 'Var';
VAL                     : 'Val';
SELF                    : 'Self';
CONSTRUCTOR             : 'Constructor';
DESTRUCTOR              : 'Destructor';
BY                      : 'By';

// Also keyword and operator
NEW                     : 'New';

// Operator
ADD_                    : '+';
MINUS_                  : '-';
MUL_                    : '*';
DIV_                    : '/';
MOD_                    : '%';
EXCLAMATION_            : '!';
AND_                    : '&&';
OR_                     : '||';
EQ_COMPARE              : '==';
EQ                      : '=';
NOT_EQ_COMPARE          : '!=';
SMALLER                 : '<';
SM_OR_EQ                : '<=';
GREATER                 : '>';
GR_OR_EQ                : '>=';
EQ_STRING               : '==.';
ADD_STRING              : '+.';
COLONCOLON              : '::';

// Also operator and seperator
DOT                     : '.';

// Seperators
LB                      : '(';
RB                      : ')';
LP                      : '{';
RP                      : '}';
SEMI                    : ';';
COMMA                   : ',';
LEFTB                   : '[';
RIGHTB                  : ']';
COLON                   : ':';
DOTDOT                  :'..';

//  ===================================================================================================================
// Literals
/*--------------------------Boolean-----------------------------------------------------------------------------------*/
BOOLEAN                 : (TRUE | FALSE);

/*--------------------------String------------------------------------------------------------------------------------*/
STRING                  : '"'Char*'"' {self.text=self.text[1:-1]}; // TODO

/*--------------------------Float-------------------------------------------------------------------------------------*/
FLOAT                   : (IntPart DecPart? ExpPart | DecPart ExpPart
                       | IntPart DecPart) {self.text=self.text.replace('_','')};

/*--------------------------Integer-----------------------------------------------------------------------------------*/
INT2                    : (([1-9] (USCORE? Digit+)*)
                       | ('0' ([1-7]+ (USCORE? OctDig+)*))
                       | (('0x' | '0X') ([1-9A-F]+ (USCORE? HexDig+)*))
                       | (('0b' | '0B') ('1' (USCORE? [01]+)*)))
                       {self.text=self.text.replace("_","")};
INT                     : ((([1-9] (USCORE? Digit+)*) | '0')
                       | ('0' (([1-7]+ (USCORE? OctDig+)*) | '0'))
                       | (('0x' | '0X') (([1-9A-F]+ (USCORE? HexDig+)*) | '0'))
                       | (('0b' | '0B') (('1' (USCORE? [01]+)*) | '0')))
                       {self.text=self.text.replace("_","")};

// Identifier
DOLLAR_ID               : '$' (Lower | Upper | USCORE | Digit)+;
ID                      : (Lower | Upper | USCORE) (Lower | Upper | USCORE | Digit)*;

WS                      : [ \t\n\b\f\r]+ -> skip; // skip spaces, tabs, newlines
CMT                     : '##'.*?'##' -> skip; // skip comment

ERROR_CHAR              : . {raise ErrorToken(self.text)};
UNCLOSE_STRING          : '"' Char* ([\b\t\n\f\r\\] | EOF)
                       {
                           target = str(self.text)
                           end_with = ['\b', '\t', '\n', '\f', '\r', '"', '\\']
                           if target[-1] in end_with:
                               raise UncloseString(target[1:-1])
                           else:
                               raise UncloseString(target[1:])
                       };
ILLEGAL_ESCAPE          : '"' Char* '\\'~[bfrnt'\\]
                       {raise IllegalEscape(self.text[1:])};

// Fragment
fragment Lower          : [a-z];
fragment Upper          : [A-Z];
fragment Digit          : [0-9];
fragment HexDig         : [0-9A-F];
fragment OctDig         : [0-7];
fragment USCORE         : '_';
fragment Dec            : ([1-9] (USCORE? Digit+)* | '0');
fragment IntPart        : Dec;
fragment DecPart        : '.' Digit*;
fragment ExpPart        : [eE][+-]? Digit+;
fragment String_Escape  : '\\' ('b'|'f'|'r'|'n'|'t'|'\''|'\\');
fragment Char           : ('\'"' | ~[\b\t\n\f\r"\\] | String_Escape);