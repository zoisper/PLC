import ply.lex as lex

import sys

tokens = (
    'LPAREN',
    'RPAREN',
    'VIRG',
    'ID',
    'NUM',
    'BOOL'
)

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_VIRG   = r','

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_BOOL(t):
    r'True|False'
    return t
def t_ID(t):
    r'[a-zA-Z]+'
    return t

t_ignore = ' \r\n\t'

def t_error(t):
    print('Illegal character: ' + t.value[0])
    return

lexer = lex.lex() # cria um AnaLex especifico a partir da especificação acima usando o gerador 'lex' do objeto 'lex'


