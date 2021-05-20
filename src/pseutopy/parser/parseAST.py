from src.pseutopy.pseutopy import PseuToPy as pseutopy
import ast

test = 'a = 1'


def switcher(index, children):
    mapping = {
        'file_input': parser(children[0]),
        'assign': ast.Assign(parser(children[0]), parser(children[1])),
        'var': ast.Name(children[0].val),
        'number': ast.Num(children[0].val),
    }
    return mapping[index]


def parser(tree):
    return switcher(tree.data, tree.children)


tree_ast = pseutopy().parser.parse(test + '\n').children[0]
parser(tree_ast)

print(tree_ast.pretty())