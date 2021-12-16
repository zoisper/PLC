import ply.lex as lex
import sys


tokens = ('LPAREN','RPAREN','NUM','WORD','BOOL','VIRG')

t_VIRG = ','

def t_LPAREN(t):
	r'\('
	return t

def t_RPAREN(t):
	r'\)'
	return t

def t_NUM(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_BOOL(t):
	r'True|False'
	return t

def t_WORD(t):
	r'\w+'
	return t



def t_error(t):
	print("Illegal Character:", t.value[0])
	t.lexer.skip(1)

t_ignore = ' \r\n\t'

lexer = lex.lex()

#for linha in sys.stdin:
#	lexer.input(linha) 
#	for tok in lexer:
#		print(tok)
#		pass