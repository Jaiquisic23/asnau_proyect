import ply.lex as Lexer
import ply.yacc as Parser

class BasicLexer(Lexer):
    tokens = { NAME, NUMBER, STRING, IF, WHILE, ARROW, EQEQ}
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

    # Define tokens
    IF = r'IF'
    FOR = r'FOR'
    ARROW = r'->'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'

    EQEQ = r'=='

    (r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    (r'#.*')
    def COMMENT(self, t):
        pass

    (r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')

class BasicParser(Parser):
    tokens = BasicLexer.tokens

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS'),
        )

    def __init__(self):
        self.env = { }
    ('')
    def statement(self, p):
        pass

    ('FOR var_assign TO expr THEN statement')
    def statement(self, p):
        return ('for_loop', ('for_loop_setup', p.var_assign, p.expr), p.statement)


    ('NAME "(" ")"')
    def statement(self, p):
        return ('fun_call', p.NAME)

    ('expr EQEQ expr')
    def condition(self, p):
        return ('condition_eqeq', p.expr0, p.expr1)

    ('var_assign')
    def statement(self, p):
        return p.var_assign

    ('NAME "=" expr')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.expr)

    ('NAME "=" STRING')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.STRING)

    ('expr')
    def statement(self, p):
        return (p.expr)

    ('expr "+" expr')
    def expr(self, p):
        return ('add', p.expr0, p.expr1)

    ('expr "-" expr')
    def expr(self, p):
        return ('sub', p.expr0, p.expr1)

    ('expr "*" expr')
    def expr(self, p):
        return ('mul', p.expr0, p.expr1)

    ('expr "/" expr')
    def expr(self, p):
        return ('div', p.expr0, p.expr1)

    ('"-" expr %prec UMINUS')
    def expr(self, p):
        return p.expr

    ('NAME')
    def expr(self, p):
        return ('var', p.NAME)

    ('NUMBER')
    def expr(self, p):
        return ('num', p.NUMBER)

if __name__ == '__main__':
    lexer = BasicLexer()
    parser = BasicParser()
    env = {}
    while True:
        try:
            text = input('basic > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            print(tree)