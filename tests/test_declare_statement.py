""" Test module for DeclareStmt """

import ast
import astor


class TestDeclareStatement:
    """ Test class for DeclareStmt.
    A DeclareStmt is of the following form: "declare my_var"
    The corresponding Python instruction should be: "my_var = None"
    """

    def test_declare_statement_in_pseudocode(self, pseutopy):
        """ Test method for a DeclareStmt written in pseudocode"""
        # Given:
        pseudocode_str = "declare my_var"
        python_str = "my_var = None"

        # Do:
        pseudocode_ast = pseutopy.convert_from_string(pseudocode_str)
        python_ast = ast.parse(python_str)

        # Then:
        assert astor.to_source(pseudocode_ast) == astor.to_source(python_ast)

    def test_declare_statement_in_python(self, pseutopy):
        """ Test method for what could be a DeclareStmt in Python"""
        # Given:
        pseudocode_str = "my_var = None"
        python_str = "my_var = None"

        # Do:
        pseudocode_ast = pseutopy.convert_from_string(pseudocode_str)
        python_ast = ast.parse(python_str)

        # Then:
        assert astor.to_source(pseudocode_ast) == astor.to_source(python_ast)
