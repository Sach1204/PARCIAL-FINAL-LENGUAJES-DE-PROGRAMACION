# estructuras_gramatica.py

class Produccion:
    """
    Representa una producción del tipo:
        LHS -> RHS
    donde RHS es una lista de símbolos.
    """
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs


class ReglaSemantica:
    """
    Describe una acción semántica asociada a una producción.
    Se almacena solo como texto simbólico.
    """
    def __init__(self, encabezado, accion):
        self.encabezado = encabezado   # Ej:  Exp → ID = Valor
        self.accion = accion           # Ej:  Exp.cod = ID.lex + Valor.cod


class EsquemaAtributos:
    """
    Contiene la descripción completa de una gramática de atributos:
      - símbolos no terminales
      - símbolos terminales
      - listado de producciones
      - reglas semánticas
      - conjunto de atributos por símbolo
    """
    def __init__(self):
        self.nonterms = []
        self.terms = []
        self.prods = []
        self.attr = {}
        self.semantic = []
        self.start = None
