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
parser.add_argument('-s-language:', '-string-language:', '-string-lg:', '-s-lg:', action='store', dest='string',
                    help='Input is now expected to be a string (default)')
parser.add_argument('-f-language:', '-file-language:', '-file-lg:', '-f-lg:', action='store', dest='file',
                    help='Input is now expected to be a file (default)')
parser.add_argument('-a', '--ast', action='store_true',
                    help="Prints out the generated Python AST")
parser.add_argument('-q', '--quiet', action='store_true',
                    help="Don't print the generated Python code")
# TODO: Modify this CLI tool to define the language of the grammar
args = parser.parse_args()

if not args.file:
    pseutopy = PseuToPy(args.string)
    generated_ast = pseutopy.convert_from_string(args.input)
else:
    pseutopy = PseuToPy(args.file)
    generated_ast = pseutopy.convert_from_file(args.input)

generated_code = astor.to_source(generated_ast)

if args.ast:
    print(ast.dump(generated_ast))
if not args.quiet:
    print(generated_code)
# if args.exec:
#     exec(generated_code)