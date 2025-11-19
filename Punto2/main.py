class Token:
    def __init__(self, tipo, lexema, pos):
        self.tipo = tipo
        self.lexema = lexema
        self.pos = pos
class Lexer:
    KEYWORDS = {"mat"}
    SYMBOLS = {'[', ']', ',', ';', '=', '+', '-', '*', '(', ')'}

    def __init__(self, text):
        self.text = text
        self.i = 0
        self.n = len(text)

    def _peek(self):
        return self.text[self.i] if self.i < self.n else None

    def _advance(self):
        c = self._peek()
        self.i += 1
        return c

    def tokens(self):
        tokens = []
        while self.i < self.n:
            c = self._peek()

            # ignorar espacios
            if c.isspace():
                self._advance()
                continue

            # números
            if c.isdigit():
                start = self.i
                while self._peek() and self._peek().isdigit():
                    self._advance()
                lex = self.text[start:self.i]
                tokens.append(Token("NUM", lex, start))
                continue

            # IDs y palabra clave 'mat'
            if c.isalpha():
                start = self.i
                while self._peek() and (self._peek().isalnum() or self._peek() == '_'):
                    self._advance()
                lex = self.text[start:self.i]
                if lex in self.KEYWORDS:
                    tokens.append(Token("MAT", lex, start))
                else:
                    tokens.append(Token("ID", lex, start))
                continue

            # símbolos
            if c in self.SYMBOLS:
                pos = self.i
                self._advance()
                tokens.append(Token(c, c, pos))
                continue

            raise SyntaxError(f"Carácter inesperado '{c}' en posición {self.i}")

        tokens.append(Token("EOF", "", self.n))
        return tokens
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def _peek(self):
        return self.tokens[self.pos]

    def _match(self, tipo):
        tok = self._peek()
        if tok.tipo == tipo:
            self.pos += 1
            return tok
        raise SyntaxError(
            f"Se esperaba '{tipo}' pero llegó '{tok.lexema}' en posición {tok.pos}"
        )

    def _check(self, tipo):
        return self._peek().tipo == tipo

    # Prog → DeclList StmtList
    def parse_program(self):
        self._DeclList()
        self._StmtList()
        self._match("EOF")

    # DeclList → Decl DeclList | ε
    def _DeclList(self):
        while self._check("MAT"):
            self._Decl()

    # Decl → mat id '[' num ',' num ']' ';'
    def _Decl(self):
        self._match("MAT")
        self._match("ID")
        self._match('[')
        self._match("NUM")
        self._match(',')
        self._match("NUM")
        self._match(']')
        self._match(';')

    # StmtList → Stmt StmtList | ε
    def _StmtList(self):
        while self._check("ID"):
            self._Stmt()

    # Stmt → Assign ';'
    def _Stmt(self):
        self._Assign()
        self._match(';')

    # Assign → id '=' Expr
    def _Assign(self):
        self._match("ID")
        self._match('=')
        self._Expr()

    # Expr → Term ((+|-) Term)*
    def _Expr(self):
        self._Term()
        while self._check('+') or self._check('-'):
            self._match(self._peek().tipo)  # + o -
            self._Term()

    # Term → Factor ('*' Factor)*
    def _Term(self):
        self._Factor()
        while self._check('*'):
            self._match('*')
            self._Factor()

    # Factor → id | '(' Expr ')'
    def _Factor(self):
        if self._check("ID"):
            self._match("ID")
        elif self._check('('):
            self._match('(')
            self._Expr()
            self._match(')')
        else:
            tok = self._peek()
            raise SyntaxError(
                f"Se esperaba ID o '(' pero llegó '{tok.lexema}' en posición {tok.pos}"
            )

def leer_archivo(nombre):
    with open(nombre, "r", encoding="utf-8") as f:
        return f.read()

def main():
    try:
        codigo = leer_archivo("programa_error.txt")

        lexer = Lexer(codigo)
        tokens = lexer.tokens()

        parser = Parser(tokens)
        parser.parse_program()

        print("\nEl programa ES válido según la gramática.\n")
    except Exception as e:
        print("\nERROR DE SINTAXIS:")
        print(e)
        print()

# Se ejecuta siempre sin if __name__ == "__main__":
main()
