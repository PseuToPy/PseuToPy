import ast

import astor
from textx import metamodel_from_file

from generators.expressions import Factor, UnaryOp, NotTest, BinaryOp, \
    OrTest, AndTest, Comparison, TestList, Expr, XorExpr, AndExpr, ShiftExpr, \
    ArithExpr, Term, Power, TestListStarExpr, AtomExpr, Atom
from generators.statements import Statement, ExprStmt, InputStmt, \
    FuncCallStmt, DeclareStmt, PrintStmt, DelStmt, IfStmt, WhileStmt, ForStmt
from generators.values import Number, Name, String, NoneType


class PseuToPy(object):
    def __init__(self):
        self.python_ast = ast.Module(body=[])
        self.variables = []
        self.meta_model = metamodel_from_file('pseudocode.tx', debug=False,
                                              classes={DeclareStmt, InputStmt,
                                                       PrintStmt, DelStmt,
                                                       FuncCallStmt, IfStmt,
                                                       WhileStmt, ForStmt,
                                                       BinaryOp, OrTest,
                                                       AndTest, Comparison,
                                                       Expr, XorExpr,
                                                       AndExpr, ShiftExpr,
                                                       ArithExpr, Term, Power,
                                                       UnaryOp, Factor,
                                                       NotTest, Statement,
                                                       ExprStmt,
                                                       TestListStarExpr,
                                                       TestList, AtomExpr,
                                                       Atom,
                                                       Number, Name, String,
                                                       NoneType})
        self.meta_model.register_obj_processors({
            'Stmt': self.convert,
        })

    def convert_from_file(self, file_name):
        self.reset_ast()
        self.meta_model.model_from_file(file_name)
        return self.python_ast

    def convert_from_string(self, pseudocode_string):
        self.reset_ast()
        self.meta_model.model_from_str(pseudocode_string)
        return self.python_ast

    def reset_ast(self):
        self.python_ast = ast.Module(body=[])
        self.variables = []

    def convert(self, root_statement):
        self.add_to_ast(self.to_node(root_statement))

    def add_to_ast(self, node):
        self.python_ast.body.append(node)
        return node

    def to_node(self, stmt):
        if isinstance(stmt, Statement):
            return stmt.to_node()
        if stmt == 'pass':
            return ast.Pass()
        if stmt == 'break':
            return ast.Break()
        if stmt == 'continue':
            return ast.Continue()


def main():
    pseutopy = PseuToPy()
    model = pseutopy.convert_from_string("""
    for i in range(0, 10, 1) do:
    print a followed by b, c
    input "Hello"
    call function foo
    set a to i
    for j in a do:
    print "test"
    for k in [1, 2, 3] do:
    print k
    end
    while True do:
    print "Hello"
    end
    end
    else do:
    set b to 1
    end
    """)
    print(astor.to_source(model))


if __name__ == '__main__':
    main()
