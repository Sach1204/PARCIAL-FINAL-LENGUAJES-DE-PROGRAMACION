# ejemplo_uso.py

from gramatica_crud import construir_gramatica_sql

def mostrar():
    g = construir_gramatica_sql()

    print("\n=== Símbolo inicial ===")
    print(g.start)

    print("\n=== No terminales ===")
    for x in g.nonterms:
        print("  •", x)

    print("\n=== Terminales ===")
    for t in g.terms:
        print("  •", t)

    print("\n=== Producciones ===")
    for p in g.prods:
        rhs = " ".join(p.rhs) if p.rhs else "ε"
        print(f"  {p.lhs}  ->  {rhs}")

    print("\n=== Reglas Semánticas ===")
    for r in g.semantic:
        print(f"  {r.encabezado}")
        print(f"     {r.accion}")

    print("\n=== Atributos ===")
    for simb, lista in g.attr.items():
        print(f"  {simb}: {lista}")


# Ejecución directa
mostrar()
