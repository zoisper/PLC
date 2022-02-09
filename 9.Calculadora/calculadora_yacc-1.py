# ------------------------------------------------------------
# calculador-yacc.py
#   
#   Calc -> ...
# ------------------------------------------------------------
import sys
import ply.yacc as yacc
from calculadora_lex_1 import tokens

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

def p_Factor_id(p):
    "Factor : id"
    if p[1] in parser.registers:
        p[0] = parser.registers[p[1]]
    else:
        p[0] = 0

def p_Factor_number(p):
    "Factor : number"
    p[0] = p[1]

def p_Factor_group(p):
    "Factor : '(' Exp ')'"
    p[0] = p[2]

#----------------------------------------
def p_error(p):
    print('Syntax error: ', p)
    parser.success = False

#----------------------------------------
#inicio do Parser e Calculadora
parser = yacc.yacc()
parser.registers = {}
print("Tabela de Identificadores predefinidos")
parser.registers.update({'a' : 1, 'b' : 2, 'c' : 3})
parser.registers['a'] = (1, 'int', 1)
parser.registers.update({'b' : 2})
parser.registers.update({'c' : 3})
parser.registers.update({'d' : 4})
parser.registers.update({'e' : 5})
parser.registers.update({'f' : 6})
parser.registers.update({'g' : 7})
parser.registers.update({'h' : 8})
for key in parser.registers:
    print(key,'  ',parser.registers[key])
print("Calculadora pronta para ser usada")
  
for line in sys.stdin:
    parser.success = True
    result = parser.parse(line)
    if parser.success:
        print('Valor: ', result)
        
        



