from src.pseutopy.pseutopy import PseuToPy as pseutopy
import ast

test = 'a = 1 + 2'

mapping = {

}
tree_ast = pseutopy().parser.parse(test + '\n')

print(tree_ast.pretty())