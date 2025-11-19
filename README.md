# PARCIAL-FINAL-LENGUAJES-DE-PROGRAMACION

## Punto 2

## GRAMÁTICA

```
Prog     → DeclList StmtList

DeclList → Decl DeclList
DeclList → ε

Decl     → mat id '[' num ',' num ']' ';'

StmtList → Stmt StmtList
StmtList → ε

Stmt     → Assign ';'

Assign   → id '=' Expr

Expr     → Expr '+' Term
Expr     → Expr '-' Term
Expr     → Term

Term     → Term '*' Factor
Term     → Factor

Factor   → id
Factor   → '(' Expr ')'
```
## CÓDIGO PYTHON
### **main.py** - Implementación del Compilador

#### **Sección 1: Clase Token**

```python
class Token:
    def __init__(self, tipo, lexema, pos):
        self.tipo = tipo
        self.lexema = lexema
        self.pos = pos
```

Representa un token con tres atributos:
- **tipo**: Clasificación del token (MAT, ID, NUM, símbolo)
- **lexema**: Texto literal del token
- **pos**: Posición en el código fuente (para mensajes de error)

---

#### **Sección 2: Clase Lexer (Análisis Léxico)**

```python
class Lexer:
    KEYWORDS = {"mat"}
    SYMBOLS = {'[', ']', ',', ';', '=', '+', '-', '*', '(', ')'}

    def __init__(self, text):
        self.text = text
        self.i = 0
        self.n = len(text)
```

**Métodos principales:**

1. **`_peek()`**: Retorna el carácter actual sin avanzar
2. **`_advance()`**: Avanza al siguiente carácter
3. **`tokens()`**: Tokeniza todo el texto de entrada

**Funcionamiento del Lexer:**

```python
def tokens(self):
    tokens = []
    while self.i < self.n:
        c = self._peek()
        
        # Ignorar espacios
        if c.isspace():
            self._advance()
            continue
        
        # Números
        if c.isdigit():
            start = self.i
            while self._peek() and self._peek().isdigit():
                self._advance()
            lex = self.text[start:self.i]
            tokens.append(Token("NUM", lex, start))
            continue
        
        # Identificadores y palabra clave 'mat'
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
        
        # Símbolos
        if c in self.SYMBOLS:
            pos = self.i
            self._advance()
            tokens.append(Token(c, c, pos))
            continue
        
        raise SyntaxError(f"Carácter inesperado '{c}' en posición {self.i}")
    
    tokens.append(Token("EOF", "", self.n))
    return tokens
```

**Tipos de tokens reconocidos:**
- `MAT`: Palabra reservada `mat`
- `ID`: Identificadores (nombres de variables)
- `NUM`: Números enteros
- Símbolos individuales: `[`, `]`, `,`, `;`, `=`, `+`, `-`, `*`, `(`, `)`
- `EOF`: Fin del archivo

---

#### **Sección 3: Clase Parser (Análisis Sintáctico)**

```python
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
```

**Métodos auxiliares:**

```python
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
```

**Métodos de parsing (uno por regla de la gramática):**

##### **1. parse_program()** - Prog → DeclList StmtList

```python
def parse_program(self):
    self._DeclList()
    self._StmtList()
    self._match("EOF")
```

Procesa el programa completo: primero todas las declaraciones, luego todas las sentencias.

---

##### **2. _DeclList()** - DeclList → Decl DeclList | ε

```python
def _DeclList(self):
    while self._check("MAT"):
        self._Decl()
```

Procesa todas las declaraciones de matrices. Se detiene cuando ya no hay más tokens `MAT`.

---

##### **3. _Decl()** - Decl → mat id '[' num ',' num ']' ';'

```python
def _Decl(self):
    self._match("MAT")
    self._match("ID")
    self._match('[')
    self._match("NUM")
    self._match(',')
    self._match("NUM")
    self._match(']')
    self._match(';')
```

Valida la sintaxis de una declaración de matriz:
```
mat A[2,3];
```

---

##### **4. _StmtList()** - StmtList → Stmt StmtList | ε

```python
def _StmtList(self):
    while self._check("ID"):
        self._Stmt()
```

Procesa todas las sentencias (asignaciones). Se detiene cuando no hay más identificadores.

---

##### **5. _Stmt()** - Stmt → Assign ';'

```python
def _Stmt(self):
    self._Assign()
    self._match(';')
```

Valida que una sentencia sea una asignación seguida de punto y coma.

---

##### **6. _Assign()** - Assign → id '=' Expr

```python
def _Assign(self):
    self._match("ID")
    self._match('=')
    self._Expr()
```

Valida una asignación: identificador, signo igual, expresión.

---

##### **7. _Expr()** - Expr → Term ((+|-) Term)*

```python
def _Expr(self):
    self._Term()
    while self._check('+') or self._check('-'):
        self._match(self._peek().tipo)  # + o -
        self._Term()
```

Procesa expresiones con suma y resta. Asociatividad: izquierda a derecha.

**Ejemplo:** `A + B - C` se procesa como `(A + B) - C`

---

##### **8. _Term()** - Term → Factor ('*' Factor)*

```python
def _Term(self):
    self._Factor()
    while self._check('*'):
        self._match('*')
        self._Factor()
```

Procesa términos con multiplicación. Asociatividad: izquierda a derecha.

**Ejemplo:** `A * B * C` se procesa como `(A * B) * C`

---

##### **9. _Factor()** - Factor → id | '(' Expr ')'

```python
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
```

Procesa factores: pueden ser variables o expresiones entre paréntesis.

---

#### **Sección 4: Función Main**

```python
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

main()
```

**Flujo de ejecución:**
1. Lee el código fuente desde el archivo
2. Ejecuta el análisis léxico (genera tokens)
3. Ejecuta el análisis sintáctico (valida gramática)
4. Imprime resultado: éxito o error

---

## ARCHIVOS DE ENTRADA

### **programa_ejemplo.txt** - Código Válido

```
mat A[2,3];
mat B[3,4];
mat C[2,4];

C = A * B;
C = A * B + C;
```

**Análisis línea por línea:**

1. `mat A[2,3];` → Declara matriz A de 2×3
2. `mat B[3,4];` → Declara matriz B de 3×4
3. `mat C[2,4];` → Declara matriz C de 2×4
4. `C = A * B;` → Asigna a C el producto de A y B
5. `C = A * B + C;` → Asigna a C la suma del producto A×B más C

**Resultado:** Programa VÁLIDO

---

### **programa_error.txt** - Código con Errores

```
mat A[2,3]
mat B[3,4];

A = A * ;
```

**Errores detectados:**

**Error 1 (línea 1):**
```
mat A[2,3]
         ^
```
**Falta punto y coma** después de la declaración

**Error 2 (línea 4):**
```
A = A * ;
        ^
```
**Expresión incompleta**: falta operando después del operador `*`

**Salida del programa:**
```
ERROR DE SINTAXIS:
Se esperaba ';' pero llegó 'mat' en posición 11
```

---

## CARACTERÍSTICAS DEL LENGUAJE

### **1. Declaraciones de Matrices**

Sintaxis:
```
mat identificador[filas, columnas];
```

Ejemplos válidos:
```
mat A[2,3];
mat matriz1[10,5];
mat M[1,1];
```

---

### **2. Operaciones Soportadas**

| Operador | Descripción | Precedencia | Ejemplo |
|----------|-------------|-------------|---------|
| `*` | Multiplicación de matrices | Alta (1) | `A * B` |
| `+` | Suma de matrices | Baja (2) | `A + B` |
| `-` | Resta de matrices | Baja (2) | `A - B` |
| `( )` | Paréntesis (agrupación) | Máxima | `(A + B)` |

---

### **3. Ejemplos de Expresiones Válidas**

```
C = A * B;
D = A + B;
E = A - B;
F = A * B + C;
G = (A + B) * C;
H = A * (B + C);
I = A + B - C + D;
J = A * B * C;
```

---

### **4. Asociatividad de Operadores**

**Suma y resta (izquierda a derecha):**
```
A + B - C   →   (A + B) - C
```

**Multiplicación (izquierda a derecha):**
```
A * B * C   →   (A * B) * C
```

---
### **Ejecución**

```bash
python main.py
```

---

### **Cambiar Archivo de Entrada**

Edita la función `main()` en `main.py`:

```python
codigo = leer_archivo("programa_ejemplo.txt")  # Cambiar aquí
```

---

### **Salidas del Programa**

**Programa válido:**
```
El programa ES válido según la gramática.
```

**Programa con error:**
```
ERROR DE SINTAXIS:
Se esperaba ';' pero llegó 'mat' en posición 11
```

---
# Punto 3

## GRAMÁTICA ANTLR

### **matrices.g4**

```antlr
grammar matrices;

// -------------- Reglas de parser (minúsculas) --------------

prog
    : declList stmtList EOF
    ;

declList
    : decl*
    ;

decl
    : MAT ID '[' NUM ',' NUM ']' ';'
    ;

stmtList
    : stmt*
    ;

stmt
    : assign ';'
    ;

assign
    : ID '=' expr
    ;

expr
    : term (('+' | '-') term)*
    ;

term
    : factor ('*' factor)*
    ;

factor
    : ID
    | '(' expr ')'
    ;

// -------------- Reglas léxicas (MAYÚSCULAS) --------------

MAT : 'mat';

ID  : [a-zA-Z_] [a-zA-Z_0-9]* ;

NUM : [0-9]+ ;

WS  : [ \t\r\n]+ -> skip ;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;
```

**Equivalencia con la gramática del Punto 2:**
```
prog      ≡ Prog → DeclList StmtList
declList  ≡ DeclList → Decl*
decl      ≡ Decl → mat id '[' num ',' num ']' ';'
stmtList  ≡ StmtList → Stmt*
stmt      ≡ Stmt → Assign ';'
assign    ≡ Assign → id '=' Expr
expr      ≡ Expr → Term ((+|-) Term)*
term      ≡ Term → Factor ('*' Factor)*
factor    ≡ Factor → id | '(' Expr ')'
```

---
## CÓDIGO PYTHON

### **parse_matrices.py**

```python
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

main()
```
## ARCHIVO DE ENTRADA

### **programa_ejemplo.txt**

```
mat A[2,3];
mat B[3,4];
mat C[2,4];

C = A * B;
C = A * B + C;
```

**Análisis:**

| Línea | Código | Descripción |
|-------|--------|-------------|
| 1 | `mat A[2,3];` | Declara matriz A de 2×3 |
| 2 | `mat B[3,4];` | Declara matriz B de 3×4 |
| 3 | `mat C[2,4];` | Declara matriz C de 2×4 |
| 5 | `C = A * B;` | Asigna a C el producto A×B |
| 6 | `C = A * B + C;` | Asigna a C la suma (A×B)+C |

**Resultado:** ✅ Programa VÁLIDO

---
## USO

### **Requisitos**

1. Python 

### **Paso 1: Generar el Parser**

```bash
antlr4 -Dlanguage=Python3 matrices.g4
```

**Archivos generados:**
- `matricesLexer.py`
- `matricesParser.py`
- `matricesListener.py`
- `matricesVisitor.py`

---

### **Paso 2: Ejecutar**

```bash
python parse_matrices.py
```

**Salida:**
```
El programa ES válido según la gramática (ANTLR).
```

---
