import ast
from lark.tree import Tree

class Number:
    """
    This class is used for both DEC_NUMBER and FLOAT_NUMBER (and maybe some other rules)
    Because we need to force the type of the value we insert in the ast.Constant node
    """
    @staticmethod
    def to_node(tree):
        return ast.Expr(
                value=switcher(tree.children[0].data).to_node(tree.children[0]))

class Assign:
    @staticmethod
    def to_node(children):
        # ast.Assign(targets=[ast.Name(id=''), ast.Constant(value=)])
        # Assign rule can match multiple things:
        #   - a = 1 (ast.Assign(targets=[ast.Name(value='a', ctx=ast.Store), ast.Constant(value=1)]))
        #   - a, b = 1, 2 (ast.Assign(targets))

        # children ==> [Tree('var', [Token('NAME', 'a')]), Tree('number', [Token('DEC_NUMBER', '1')])]
       
        left, right = children[0], children[1]
        if len(left.children) == 1:
            return ast.Assign(
                targets=[switcher(left.children[0].type).to_node(left.children[0])],
                value=switcher(right.children[0].type).to_node(right.children[0])
            )
        else:
            return None # ast.Assign(targets=[])

class Var:
    @staticmethod
    def to_node(token):
        return ast.Name(id=token.value, ctx=ast.Store())

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

def switcher(index):
    """
    index: Either 'data' or 'value'
    children: Children of the tree (if tree)
    """
    mapping = {
        'assign': Assign,
        'number': Number,
        'var': Var,
        'DEC_NUMBER': Decimal,
        'FLOAT_NUMBER': Float,
        'STRING': String,
        'NAME': Name,
        #'testlist_star_expr': _testlist_star_expr   # Used for --> 1, 2, 3 without parentheses
    }
    return mapping[index]

def parse_ast_to_python(tree):
    ast_module = ast.Module()
    ast_module.body = []
    for child in tree.children:
        if child.__class__ is Tree:
            ast_module.body.append(switcher(child.data).to_node(child.children))
    return ast_module