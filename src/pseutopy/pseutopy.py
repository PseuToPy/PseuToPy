import ast

import astor
from textx import metamodel_from_file

from src.pseutopy.generators.expressions import Factor, UnaryOp, NotTest, \
    BinaryOp, OrTest, AndTest, Comparison, TestList, Expr, XorExpr, AndExpr, \
    ShiftExpr, ArithExpr, Term, Power, TestListStarExpr, AtomExpr, Atom, \
    Parameters, TypedArgsList
from src.pseutopy.generators.statements import Statement, ExprStmt, \
    InputStmt, FuncCallStmt, DeclareStmt, PrintStmt, DelStmt, IfStmt, \
    WhileStmt, ForStmt, FuncDef, ReturnStmt
from src.pseutopy.generators.values import Number, Name, String, NoneType, \
    Boolean


class PseuToPy(object):
    def __init__(self):
        self.python_ast = ast.Module(body=[])
        self.variables = []
        self.meta_model = metamodel_from_file('src/pseutopy/pseudocode.tx',
                                              debug=False,
                                              classes={DeclareStmt, InputStmt,
                                                       PrintStmt, DelStmt,
                                                       FuncCallStmt, IfStmt,
                                                       WhileStmt, ForStmt,
                                                       FuncDef, Parameters,
                                                       TypedArgsList,
                                                       ReturnStmt,
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
                                                       NoneType, Boolean})
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
    set a, b to 1 + 2 - True * a < b, 3
    set c to ()

    input("Hello")

    set foo to None
    a = 1
    declare bix

    for i in range(0):
        for j in range(0, 10):
            for k in range(0, 10, 1):
                set a to None
                declare b
                declare c
                declare d
                print(1, "Hello", True)
                print(1 + True)
                print "Hello" + "world"
                print "Hello" followed by a followed by "my friend" + "Bob"
                if a == b:
                    set a to b
                end
            end
        end
    end

    if a is greater than b then
        if b is lower than c then:
            if d is lower than e then     :
                set f to the result of input integer ("Hi")
                set b to the result of input number("hello")
                set a to the result of input("hello")
                if e is equal to f:
                    a = 2
                    b = 3
                end
            end
        end
    end

    if True:
        a = 1
    else if True:
        b = 2
    elif True:
        c = 3
    else if True:
        d = 4
    else:
        e = 5 to the power of 2
    end

    def fizz(a):
        return None
    end
    def fizz():
        return 1
    end
    def fizz with no parameter to do:
        print("Hello")
    end
    define function fizz with a as parameter to do:
        return a
    end
    define function fizzbuzz with a, b as parameters:
        return b
    end
    define function fizzbuzz with (a,b,c) as parameters to do  :
        return 1
    end

    call function fizzbuzz
    call function fizzbuzz with parameter a
    call function fizzbuzz with parameters a, b
    set a to (a, b, c)
    set a to the result of call function fizzbuzz with parameters a, b
    """)
    print(astor.to_source(model))


if __name__ == '__main__':
    main()
