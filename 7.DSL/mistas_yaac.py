import ply.yacc as yacc
import sys

from mistas_lex import tokens

def p_mistas_grammar(p):
	"""
	LIST : LPAREN ELS RPAREN
	ELS : ELS VIRG EL
	ELS : EL
	EL : NUM
	EL : BOOL
	EL : WORD
	"""

def p_error(p):
	print("Syntax error!")
	parser.exito = False

parser = yacc.yacc()

parser.exito = True

fonte = ""

for linha in sys.stdin:
	fonte += linha

parser.parse(fonte)

if parser.exito:
	print("Parsing realizado com sucesso!")
