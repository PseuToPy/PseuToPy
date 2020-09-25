import argparse
import ast
import astor


from src.pseutopy.pseutopy import PseuToPy

parser = argparse.ArgumentParser(description='A pseudocode to Python '
                                             'converter written in Python '
                                             'using textX.')
parser.add_argument('input',
                    help="Pseudocode input to be converted into Python")
input_group = parser.add_mutually_exclusive_group()
parser.add_argument('-type:', action='store', dest='type',
                    help='Input is now expected to be a "string" or "file"')
parser.add_argument('-language:', '-lg:', action='store', dest='language',
                    help='Input is now expected to be "fr" or "en"')
parser.add_argument('-a', '--ast', action='store_true',
                    help="Prints out the generated Python AST")
parser.add_argument('-q', '--quiet', action='store_true',
                    help="Don't print the generated Python code")
# TODO: Modify this CLI tool to define the language of the grammar
args = parser.parse_args()

if args.type in ['s', 'string']:
    pseutopy = PseuToPy(args.language)
    generated_ast = pseutopy.convert_from_string(args.input)
else:
    pseutopy = PseuToPy(args.language)
    generated_ast = pseutopy.convert_from_file(args.input)

generated_code = astor.to_source(generated_ast)

if args.ast:
    print(ast.dump(generated_ast))
if not args.quiet:
    print(generated_code)
# if args.exec:
#     exec(generated_code)