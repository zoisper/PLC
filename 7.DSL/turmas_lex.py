'''
TURMAS -> TURMAS TURMA | TURMA

TURMA -> Turma id ':' ALUNOS

ALUNOS -> ALUNOS ALUNO | ALUNO

ALUNO -> Aluno nome Notas NOTAS '.'

NOTAS -> NOTAS ',' | NOTAS

NOTA -> num

'''

import ply.lex as lex
import sys


tokens = ('TURMA','ID','DP','ALUNO', 'NOTAS', 'PF', 'VIRG', 'NUM')

t_DP = r':'
t_PF = r'\.'
t_VIRG = ','

def t_TURMA(t):
	r'(?i:Turma)'
	return t

def t_NOTAS(t):
	r'(?i:Notas)'
	return t

def t_ALUNO(t):
	r'(?i:ALUNO)'
	return t


def t_ID(t):
	r'\w+'
	return t


def t_NUM(t):
	r'\d+'
	return t

def t_error(t):
	print("Illegal Character:", t.value[0])
	t.lexer.skip(1)

t_ignore = '\r\n\t'

lexer = lex.lex()

for linha in sys.stdin:
    lexer.input(linha) 
    tok = lexer.token()
    while tok:
        print(tok)
        tok = lexer.token()
