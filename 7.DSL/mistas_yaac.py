import ply.yacc as yacc
import sys

from mistas_lex import tokens

#def p_mistas_grammar(p):
#	"""
#	LIST : LPAREN ELS RPAREN
#	ELS : ELS VIRG EL
#	ELS : EL
#	EL : NUM
#	EL : BOOL
#	EL : WORD
#	"""

def p_list(p):
	"LIST : LPAREN ELS RPAREN" 
	print(p[2])

def p_els_varias(p):
	"ELS : ELS VIRG EL"
	parser.conta += 1
	p[0] = p[1] 
	p[0].append(p[3])

def p_els_uma(p):
	"ELS : EL"
	parser.conta = 1
	p[0] = p[1]

def p_el_num(p):
	"EL : NUM"
	parser.soma += p[1]
	p[0] = []

def p_el_bool(p):
	"EL : BOOL"
	p[0] = p[1]

def p_el_word(p):
	"EL : WORD"
	parser.pals.append(p[1])	
	p[0] = []

def p_error(p):
	print("Syntax error!")
	parser.exito = False


parser = yacc.yacc()
parser.exito = True
parser.soma = 0
parser.conta = 0
parser.pals = []

fonte = ""

for linha in sys.stdin:
	fonte += linha


parser.parse(fonte)

if parser.exito:
	print("Parsing realizado com sucesso!")
	print("Numerero de Elementos:", parser.conta)
	print("Soma:", parser.soma)
	print("As palvaras são:", parser.pals)
