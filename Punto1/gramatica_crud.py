# gramatica_crud.py

from estructuras_gramatica import (
    Produccion,
    ReglaSemantica,
    EsquemaAtributos
)

def construir_gramatica_sql():
    """
    Construye un esquema de gramática de atributos
    para un subconjunto de SQL tipo CRUD.
    """

    g = EsquemaAtributos()
    g.start = "Programa"
    g.nonterms = [
        "Programa", "Instruccion",
        "Seleccion", "Insercion", "Actualizacion", "Eliminacion",
        "ListaCampos", "Campo", "TalVezCond",
        "Condicion", "Expr", "Dato"
    ]

    g.terms = [
        "SELECT", "INSERT", "UPDATE", "DELETE",
        "INTO", "VALUES", "SET", "FROM", "WHERE",
        "ID", "NUM", "CAD",
        "*", ",", ";", "(", ")", "=", "AND", "OR"
    ]
    g.prods.extend([
        Produccion("Programa", ["Instruccion", ";"]),
        Produccion("Instruccion", ["Seleccion"]),
        Produccion("Instruccion", ["Insercion"]),
        Produccion("Instruccion", ["Actualizacion"]),
        Produccion("Instruccion", ["Eliminacion"]),

        Produccion("Seleccion", ["SELECT", "ListaCampos", "FROM", "ID", "TalVezCond"]),
        Produccion("Insercion", ["INSERT", "INTO", "ID", "(", "ListaCampos", ")", "VALUES", "(", "Dato", ")"]),
        Produccion("Actualizacion", ["UPDATE", "ID", "SET", "ID", "=", "Dato", "TalVezCond"]),
        Produccion("Eliminacion", ["DELETE", "FROM", "ID", "TalVezCond"]),

        Produccion("TalVezCond", ["WHERE", "Condicion"]),
        Produccion("TalVezCond", []),

        Produccion("ListaCampos", ["ListaCampos", ",", "Campo"]),
        Produccion("ListaCampos", ["Campo"]),

        Produccion("Campo", ["ID"]),
        Produccion("Campo", ["*"]),

        Produccion("Condicion", ["Condicion", "AND", "Condicion"]),
        Produccion("Condicion", ["Condicion", "OR", "Condicion"]),
        Produccion("Condicion", ["Expr"]),

        Produccion("Expr", ["ID", "=", "Dato"]),

        Produccion("Dato", ["NUM"]),
        Produccion("Dato", ["CAD"]),
    ])
    g.attr = {
        "Programa": ["codigo"],
        "Instruccion": ["codigo"],
        "Seleccion": ["codigo"],
        "Insercion": ["codigo"],
        "Actualizacion": ["codigo"],
        "Eliminacion": ["codigo"],
        "ListaCampos": ["texto"],
        "Campo": ["texto"],
        "Expr": ["texto"],
        "Dato": ["texto"],
        "TalVezCond": ["texto"],
        "Condicion": ["texto"],
    }
    g.semantic.extend([
        ReglaSemantica(
            "Programa → Instruccion ;",
            "Programa.codigo = Instruccion.codigo"
        ),

        ReglaSemantica(
            "Seleccion → SELECT ListaCampos FROM ID TalVezCond",
            'Seleccion.codigo = "SELECT " + ListaCampos.texto + " FROM " + ID.lex + TalVezCond.texto'
        ),

        ReglaSemantica(
            "Insercion → INSERT INTO ID ( ListaCampos ) VALUES ( Dato )",
            'Insercion.codigo = "INSERT INTO " + ID.lex + "(" + ListaCampos.texto + ") VALUES (" + Dato.texto + ")"'
        ),

        ReglaSemantica(
            "Actualizacion → UPDATE ID SET ID = Dato TalVezCond",
            'Actualizacion.codigo = "UPDATE " + ID1.lex + " SET " + ID2.lex + " = " + Dato.texto + TalVezCond.texto'
        ),

        ReglaSemantica(
            "Eliminacion → DELETE FROM ID TalVezCond",
            'Eliminacion.codigo = "DELETE FROM " + ID.lex + TalVezCond.texto'
        ),

        ReglaSemantica(
            "ListaCampos → ListaCampos , Campo",
            "ListaCampos.texto = ListaCampos1.texto + ',' + Campo.texto"
        ),

        ReglaSemantica(
            "ListaCampos → Campo",
            "ListaCampos.texto = Campo.texto"
        ),

        ReglaSemantica(
            "Campo → ID",
            "Campo.texto = ID.lex"
        ),

        ReglaSemantica(
            "Campo → *",
            'Campo.texto = "*"'
        ),
    ])

    return g
