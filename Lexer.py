import ply.lex as lex

tokens = {'NUMBER', 'PLUS', 'MINUS','TIMES','DIVIDE','LPAREN','RPAREN'}

t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDES = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    pass

def t_error(t):
    print("Illegal character '%s" %t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = "3+4*10+-20*2"

lexer.input(data)

while True:
    tok=lexer.token()
    if not tok:
        break
    print(tok)


