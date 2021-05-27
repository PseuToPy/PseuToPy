"""
This module contains lots of classes that represent each rule that can be parsed by Lark.
To organize this module a little bit, we will try to:
- Keep token classes before tree classes
- Keep atom classes before expression classes
- Keep expression classes before statement classes
"""
import ast
from lark.tree import Tree


class ConstTrue:
    @staticmethod
    def to_node(token):
        return ast.Constant(value=True)


class ConstFalse:
    @staticmethod
    def to_node(token):
        return ast.Constant(value=False)


class ConstNone:
    @staticmethod
    def to_node(token):
        return ast.Constant(value=None)


class Decimal:
    @staticmethod
    def to_node(token):
        return ast.Constant(value=int(token.value))


class Float:
    @staticmethod
    def to_node(token):
        return ast.Constant(value=float(token.value))


class String:
    @staticmethod
    def to_node(token):
        return ast.Constant(value=token.value)


class Name:
    @staticmethod
    def to_node(token):
        return ast.Name(id=token.value, ctx=ast.Store())


class Number:
    @staticmethod
    def to_node(token):
        return read_node(token[0].type).to_node(token[0])


class Var:
    @staticmethod
    def to_node(token):
        return read_node(token[0].type).to_node(token[0])


class TestlistStarExpr:
    @staticmethod
    def to_node(tree):
        elts = [read_node(child.data).to_node(child.children) for child in tree]
        return ast.Tuple(elts=elts)


class Assign:
    @staticmethod
    def to_node(children):
        """
        Assign rule can match multiple things:
        - a = 1
        - a, b = 1, 2
        :param children: The list that belongs to the Assign Tree
        :return: The ast.Assign node to be inserted into the ast.Module
        """
        left, right = children
        targets = [read_node(left.data).to_node(left.children)]
        value = read_node(right.data).to_node(right.children)
        return ast.Assign(targets=targets, value=value)


def parse_ast_to_python(tree):
    ast_module = ast.Module()
    ast_module.body = []
    for child in tree.children:
        if child.__class__ is Tree:
            ast_module.body.append(read_node(child.data).to_node(child.children))
    return ast_module


def read_node(node):
    """
    index: Either 'data' or 'value'
    """
    mapping = {
        'const_true': ConstTrue,
        'const_false': ConstFalse,
        'const_none': ConstNone,
        'DEC_NUMBER': Decimal,
        'FLOAT_NUMBER': Float,
        'STRING': String,
        'NAME': Name,
        'number': Number,
        'var': Var,
        'testlist_star_expr': TestlistStarExpr,
        'assign': Assign
    }
    return mapping[node]
