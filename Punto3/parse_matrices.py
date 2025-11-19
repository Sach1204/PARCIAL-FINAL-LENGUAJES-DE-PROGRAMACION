from antlr4 import FileStream, CommonTokenStream
from matricesLexer import matricesLexer
from matricesParser import matricesParser

def main():
    # Lee el programa de ejemplo
    input_stream = FileStream("programa_ejemplo.txt", encoding="utf-8")

    # Lexer y parser generados por ANTLR
    lexer = matricesLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = matricesParser(token_stream)

    # Regla inicial de la gramática
    tree = parser.prog()

    # Si no hubo errores de sintaxis, llega aquí
    print("El programa ES válido según la gramática (ANTLR).")

# Se ejecuta siempre, sin if __name__ == '__main__':
main()
