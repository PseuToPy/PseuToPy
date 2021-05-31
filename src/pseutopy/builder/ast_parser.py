"""
This module contains lots of classes that represent each rule that can be parsed by Lark.
To organize this module a little bit, we will try to:
- Keep token classes before tree classes
- Keep atom classes before expression classes
- Keep expression classes before statement classes
"""
import ast
from lark.tree import Tree


#####################
##  Token classes  ##
#####################

class Decimal:
    @staticmethod
    def to_node(token):
        return ast.Constant(value=int(token.value))


class Float:
    @staticmethod
    def to_node(token):
        return ast.Constant(value=float(token.value))


class StringToken:
    @staticmethod
    def to_node(token):
        return ast.Constant(value=token.value)


class Name:
    @staticmethod
    def to_node(token):
        return ast.Name(id=token.value, ctx=ast.Store())


####################
##  Tree classes  ##
####################

class Number:
    @staticmethod
    def to_node(token):
        return read_node(token[0].type).to_node(token[0])


class Var:
    @staticmethod
    def to_node(token):
        return read_node(token[0].type).to_node(token[0])


class String:
    @staticmethod
    def to_node(token):
        return read_node(token[0].type).to_node(token[0])


####################
##  Atom classes  ##
####################

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


class Set:
    @staticmethod
    def to_node(tree):
        return read_node(tree[0].data).to_node(tree[0].children)


class SetComp:
    @staticmethod
    def to_node(children):
        elts = [read_node(child.children[0].type).to_node(child.children[0]) for child in children]
        return ast.Set(elts=elts)


##########################
##  Expression classes  ##
##########################

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


class TestlistStarExpr:
    @staticmethod
    def to_node(tree):
        elts = [read_node(child.data).to_node(child.children) for child in tree]
        return ast.Tuple(elts=elts)


class BinOp:
    @staticmethod
    def to_node(tree):
        if len(tree) == 3:
            left, op, right = [read_node(child.data).to_node(child.children) for child in tree]
            return ast.BinOp(left=left, op=op, right=right)
        else:
            right = read_node(tree[-1].data).to_node(tree[-1].children)
            op = read_node(tree[-2].data).to_node(tree[-2].children)
            left = read_node('arith_expr').to_node(tree[:-2])
            return ast.BinOp(left=left, op=op, right=right)


class ArithPlus:
    @staticmethod
    def to_node(tree):
        return ast.Add()


class ArithMinus:
    @staticmethod
    def to_node(tree):
        return ast.Sub()


class Mult:
    @staticmethod
    def to_node(tree):
        return ast.Mult()


class Div:
    @staticmethod
    def to_node(tree):
        return ast.Div()


class Mod:
    @staticmethod
    def to_node(tree):
        return ast.Mod()


class FloorDiv:
    @staticmethod
    def to_node(tree):
        return ast.FloorDiv()


class Power:
    @staticmethod
    def to_node(tree):
        left, right = [read_node(child.data).to_node(child.children) for child in tree]
        return ast.BinOp(left=left, op=ast.Pow(), right=right)


class And:
    @staticmethod
    def to_node(tree):
        op = ast.And()
        values = [read_node(child.data).to_node(child.children) for child in tree]
        return ast.BoolOp(op=op, values=values)


class Or:
    @staticmethod
    def to_node(tree):
        op = ast.Or()
        values = [read_node(child.data).to_node(child.children) for child in tree]
        return ast.BoolOp(op=op, values=values)


class Not:
    @staticmethod
    def to_node(tree):
        op = ast.Not()
        operand = read_node(tree[0].data).to_node(tree[0].children)
        return ast.UnaryOp(op=op, operand=operand)


class Factor:
    @staticmethod
    def to_node(tree):
        op, operand = [read_node(child.data).to_node(child.children) for child in tree]
        return ast.UnaryOp(op=op, operand=operand)


class UnaryAdd:
    @staticmethod
    def to_node(tree):
        return ast.UAdd()


class UnarySub:
    @staticmethod
    def to_node(tree):
        return ast.USub()


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
        # Token
        'DEC_NUMBER': Decimal,
        'FLOAT_NUMBER': Float,
        'STRING': StringToken,
        'NAME': Name,
        #Token classes
        'number': Number,
        'var': Var,
        'string': String,
        # Atom classes
        'const_true': ConstTrue,
        'const_false': ConstFalse,
        'const_none': ConstNone,
        'set': Set,
        'set_comp': SetComp,
        # Expression classes
        'assign': Assign,
        'testlist_star_expr': TestlistStarExpr,
        'arith_expr': BinOp,
        'arith_plus': ArithPlus,
        'arith_minus': ArithMinus,
        'term': BinOp,
        'mult': Mult,
        'div': Div,
        'mod': Mod,
        'floor_div': FloorDiv,
        'power': Power,
        'and_test': And,
        'or_test': Or,
        'not': Not,
        'factor': Factor,
        'plus': UnaryAdd,
        'minus': UnarySub
        # Statement classes
        
    }
    return mapping[node]
