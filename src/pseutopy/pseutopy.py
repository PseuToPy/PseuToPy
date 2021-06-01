"""
PseuToPy parser that transforms pseudocode instructions into valid Python 3.8 instructions.
"""
from io import open

from src.pseutopy.grammar_parser import PythonIndenter
from src.pseutopy.builder.ast_parser import parse_ast_to_python
from lark import Lark, exceptions
import astor
import re

class PseuToPy:
    """
    Main module interface to PseuToPy. This module takes strings of pseudocode instructions and transpiles
    them into valid Python 3.8 instructions.
    """

    def __init__(self, lang="en"):
        self.kwargs = dict(rel_to=__file__, postlex=PythonIndenter(), start='file_input')
        self.parser = Lark.open('grammars/' + lang + '.lark', parser="lalr", **self.kwargs)

    def convert_from_file(self, file_name):
        try:
            lark_ast = self.parser.parse(self.__read(file_name) + '\n')
            return self.__construct_python(lark_ast)
        except exceptions.UnexpectedToken:
            return "An error occured: Unable to parse the input. Please check that your input is correct."
        except FileNotFoundError:
            return "An error occured: No such file or directory: " + file_name

    def convert_from_string(self, instructions):
        try:
            lark_ast = self.parser.parse(instructions + '\n')
            return self.__construct_python(lark_ast)
        except exceptions.UnexpectedToken:
            return "An error occured: Unable to parse the input. Please check that your input is correct."

    def convert_to_ast(self, instructions):
        try:
            return self.parser.parse(instructions + '\n')
        except exceptions.UnexpectedToken:
            return "An error occured: Unable to parse the input. Please check that your input is correct."

    def convert_to_pretty_ast(self, instructions):
        try:
            return self.parser.parse(instructions + '\n').pretty()
        except exceptions.UnexpectedToken:
            return "An error occured: Unable to parse the input. Please check that your input is correct."

    def __read(self, file_name, *args):
        kwargs = {'encoding': 'utf-8'}
        with open(file_name, *args, **kwargs) as f:
            return f.read()

    def __construct_python(self, tree):
        result = astor.to_source(parse_ast_to_python(tree))
        return self.__clean_python_result(result)

    def __clean_python_result(self, result):
        result = result.replace("\'\"", "\"")
        result = result.replace("\"\'", "\"")
        pattern = re.compile(r'\((\d+)\):')
        template = """({}):"""
        for match in re.findall(pattern, result):
            result = result.replace(template.format(match), match+":")
        return result

if __name__ == '__main__':
    ptp = PseuToPy()
    tmp = """
for i in [1, 2, 3]:
    print(i)
    print(i)
else: print("test")
    """
    tmp2 = """
while 1 is lower than 2 do:
    set a to 2
    b = 3
    print((a % 2) - b)
else do:
    b = 2
    set a to 3
    print(a + b)
"""
    tree = ptp.convert_from_string(tmp2)
    print(tree)