import ast
import os

from inspect import getmembers

from textx import metamodel_from_file, exceptions

from pseutopy.generators.expressions import Factor, UnaryOp, NotTest, \
    BinaryOp, OrTest, AndTest, Comparison, TestList, Expr, XorExpr, AndExpr, \
    ShiftExpr, ArithExpr, Term, Power, TestListStarExpr, AtomExpr, Atom, \
    Parameters, TypedArgsList
from pseutopy.generators.statements import Statement, ExprStmt, \
    InputStmt, FuncCallStmt, DeclareStmt, PrintStmt, DelStmt, IfStmt, \
    WhileStmt, ForStmt, FuncDef, ReturnStmt
from pseutopy.generators.values import Number, Name, String, NoneType, \
    Boolean
from src.pseutopy.exceptions import ExceptionHandler


class PseuToPy(object):
    def __init__(self):
        self.python_ast = ast.Module(body=[])
        self.variables = []
        self.meta_model = metamodel_from_file(os.path.dirname(__file__) + "/pseudocode.tx",
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
        pseudocode_formatted = " ".join(pseudocode_string.split())
        # HERE
        try:
            self.meta_model.model_from_str(pseudocode_formatted)
            #for k, v in self.meta_model.__dict__.get('user_classes').get():
            #    print(k)

            #print(self.python_ast._fields.__str__())
        except exceptions.TextXSyntaxError as SE:
            handler = ExceptionHandler(pseudocode_formatted, SE, self.meta_model)
            handler.analyze_error()
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
