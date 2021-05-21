from src.pseutopy.pseutopy import PseuToPy as pseutopy
import ast
import astunparse
import astor
from lark.lexer import Token
from lark.tree import Tree

test = 'a = 1'


def switcher(index, children):
    mapping = {
        #'file_input': parser(**children[0]),
        # 'assign': ast.Assign(parser(children[0]), parser(children[1])),
        'var': ast.Name(id=children.value, ctx=ast.Store),
        'number': ast.Constant(value=children.value),
    }
    return mapping[index]


def parser(tree):
    if tree.__class__ is Tree:
        
        if 'file_input' == tree.data:
            return parser(tree.children[0])
        elif 'assign' == tree.data:
            return ast.Assign(parser(tree.children[0]), parser(tree.children[1]))
        else: 
            return switcher(tree.data, tree.children[0])
    #     return switcher(tree.data, tree.children)
    # elif tree.__class__ is Token:
    #     print('Token')
    #     print(tree.type)
    #     print(tree.value)
    # else: print('none')

tree_ast = pseutopy().parser.parse(test + '\n')#.children[0]

print(tree_ast.pretty())
python_ast = parser(tree_ast)

print(astor.to_source(astunparse.dump(python_ast)))
print(astor.to_source(python_ast))