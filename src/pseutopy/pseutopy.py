"""
PseuToPy parser that transforms pseudocode instructions into valid Python 3.8 instructions.
"""
from io import open

from src.pseutopy.grammar_parser import PythonIndenter
from lark import Lark


class PseuToPy():
    """
    Main module interface to PseuToPy. This module takes strings of pseudocode instructions and transpiles
    them into valid Python 3.8 instructions.
    """
    def __init__(self, lang="en"):
        self.kwargs = dict(rel_to=__file__, postlex=PythonIndenter(), start='file_input')
        self.parser = Lark.open('grammars/' + lang + '.lark', parser="lalr", **self.kwargs)

    def convert_from_file(self, file_name):
        tree = self.parser.parse(self.__read(file_name) + '\n')
        python_code = self.__construct_python(tree)
        return python_code

    def convert_from_string(self, instructions):
        tree = self.parser.parse(instructions + '\n')
        python_code = self.__construct_python(tree)
        return python_code

    def __read(self, file_name, *args):
        kwargs = {'encoding': 'utf-8'}
        with open(file_name, *args, **kwargs) as f:
            return f.read()

    def __construct_python(self, tree):
        return tree.pretty()
