# Generated from matrices.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .matricesParser import matricesParser
else:
    from matricesParser import matricesParser

# This class defines a complete listener for a parse tree produced by matricesParser.
class matricesListener(ParseTreeListener):

    # Enter a parse tree produced by matricesParser#prog.
    def enterProg(self, ctx:matricesParser.ProgContext):
        pass

    # Exit a parse tree produced by matricesParser#prog.
    def exitProg(self, ctx:matricesParser.ProgContext):
        pass


    # Enter a parse tree produced by matricesParser#declList.
    def enterDeclList(self, ctx:matricesParser.DeclListContext):
        pass

    # Exit a parse tree produced by matricesParser#declList.
    def exitDeclList(self, ctx:matricesParser.DeclListContext):
        pass


    # Enter a parse tree produced by matricesParser#decl.
    def enterDecl(self, ctx:matricesParser.DeclContext):
        pass

    # Exit a parse tree produced by matricesParser#decl.
    def exitDecl(self, ctx:matricesParser.DeclContext):
        pass


    # Enter a parse tree produced by matricesParser#stmtList.
    def enterStmtList(self, ctx:matricesParser.StmtListContext):
        pass

    # Exit a parse tree produced by matricesParser#stmtList.
    def exitStmtList(self, ctx:matricesParser.StmtListContext):
        pass


    # Enter a parse tree produced by matricesParser#stmt.
    def enterStmt(self, ctx:matricesParser.StmtContext):
        pass

    # Exit a parse tree produced by matricesParser#stmt.
    def exitStmt(self, ctx:matricesParser.StmtContext):
        pass


    # Enter a parse tree produced by matricesParser#assign.
    def enterAssign(self, ctx:matricesParser.AssignContext):
        pass

    # Exit a parse tree produced by matricesParser#assign.
    def exitAssign(self, ctx:matricesParser.AssignContext):
        pass


    # Enter a parse tree produced by matricesParser#expr.
    def enterExpr(self, ctx:matricesParser.ExprContext):
        pass

    # Exit a parse tree produced by matricesParser#expr.
    def exitExpr(self, ctx:matricesParser.ExprContext):
        pass


    # Enter a parse tree produced by matricesParser#term.
    def enterTerm(self, ctx:matricesParser.TermContext):
        pass

    # Exit a parse tree produced by matricesParser#term.
    def exitTerm(self, ctx:matricesParser.TermContext):
        pass


    # Enter a parse tree produced by matricesParser#factor.
    def enterFactor(self, ctx:matricesParser.FactorContext):
        pass

    # Exit a parse tree produced by matricesParser#factor.
    def exitFactor(self, ctx:matricesParser.FactorContext):
        pass



del matricesParser