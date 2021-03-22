"""
Module that parses the pseudocode instructions
"""

from lark.indenter import Indenter


class PythonIndenter(Indenter):
    """
    Class that defines tokens used when parsing Python instructions
    """
    NL_type = '_NEWLINE'
    OPEN_PAREN_types = ['LPAR', 'LSQB', 'LBRACE']
    CLOSE_PAREN_types = ['RPAR', 'RSQB', 'RBRACE']
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 8
