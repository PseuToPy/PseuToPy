"""
Command-line utility to interact with the PseuToPy package. With this tool, it is possible
to convert PseuToPy instructions into the equivalent Python code, or to display the Lark
parse trees.
"""
import argparse


from src.pseutopy.pseutopy import PseuToPy

parser = argparse.ArgumentParser(description='A pseudocode to Python converter written in Python')
parser.add_argument('lang',
                    help="Choose the language of the grammar to use (default is English)")
parser.add_argument('input',
                    help="Pseudocode input to be converted into Python")
input_group = parser.add_mutually_exclusive_group()
input_group.add_argument('-f', '--file', action='store_true',
                         help="Input is now expected to be a file")
input_group.add_argument('-s', '--string', action='store_true',
                         help="Input is now expected to be a string (default)")
output_group = parser.add_mutually_exclusive_group()
output_group.add_argument('-a', '--ast', action='store_true',
                          help="Prints out the generated Lark AST")
output_group.add_argument('-p', '--pretty', action='store_true',
                          help="Prints out the pretty formatted Lark AST")
parser.add_argument('-q', '--quiet', action='store_true',
                    help="Don't print the generated Python code")
args = parser.parse_args()

if args.lang:
    try:
        pseutopy = PseuToPy(args.lang)
    except FileNotFoundError:
        pass
else:
    pseutopy = PseuToPy()

try:
    return_value = None
    if not args.file:
        if not args.ast and not args.pretty:
            return_value = pseutopy.convert_from_string(args.input)
        else:
            if args.ast:
                return_value = pseutopy.convert_to_ast(args.input)
            else:
                return_value = pseutopy.convert_to_pretty_ast(args.input)
    else:
        if not args.ast and not args.pretty:
            return_value = pseutopy.convert_from_file(args.input)
        else:
            if args.ast:
                return_value = pseutopy.convert_to_ast(args.input)
            else:
                return_value = pseutopy.convert_to_pretty_ast(args.input)
    print(return_value)
except NameError:
    print("An error occured: Invalid language name passed to the module.")
