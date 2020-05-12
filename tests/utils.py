import ast

import astor


def check_ast(pseutopy, python_str, pseudocode_str):
    expected_ast = ast.parse(python_str)
    generated_ast = pseutopy.convert_from_string(pseudocode_str)
    return astor.to_source(expected_ast) == astor.to_source(generated_ast)
