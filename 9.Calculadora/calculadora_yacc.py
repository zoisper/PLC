# ------------------------------------------------------------
# calculador-yacc.py
#   
#   Calc -> ...
# ------------------------------------------------------------
import sys
import ply.yacc as yacc
from calculadora_lex import tokens

def p_Calculadora(p):
    "Calc : Exp "
    print('A Expressão introduzida vale: ' , p[1])
    
def p_Exp_add(p):
    "Exp : Exp '+' Term"
    p[0] = p[1] + p[3]

def p_Exp_sub(p):
    "Exp : Exp '-' Term"
    p[0] = p[1] - p[3]

def p_Exp_term(p):
    "Exp : Term"
    p[0] = p[1]

def p_Term_mul(p):
    "Term : Term '*' Factor"
    p[0] = p[1] * p[3]

def p_Term_div(p):
    "Term : Term '/' Factor"
    p[0] = p[1] / p[3]

def p_Term_factor(p):
    "Term : Factor"
    p[0] = p[1]

def p_Factor_number(p):
    "Factor : number"
    p[0] = p[1]

def p_Factor_group(p):
    "Factor : '(' Exp ')'"
    p[0] = p[2]

def p_error(p):
    print('Syntax error: ', p)
    parser.success = False

#inicio do Parser e Calculadora
parser = yacc.yacc()

for line in sys.stdin:
    parser.success = True
    result = parser.parse(line)
    
        
        



