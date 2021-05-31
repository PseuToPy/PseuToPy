"""
Current state of the `arith_expr` rule (plus any rules that the `arith_expr` rule is based
on:)

?arith_expr: term (_add_op term)*
?term: factor (_mul_op factor)*
?factor: factor_op factor | power


Note:
    - Unnecessary parentheses in PseuToPy will not be rendered when translated into Python
    - Quotes will always be translated into double quotes when handling Strings
"""


def test_arith_expr(pseutopy):
    python_code = ["a = 1 + 2", "a = 1 - 2", 'a = "Hello" + "world"']
    pseutopy_code = ["a = 1 plus 2", "a = 1 minus 2", "a = 'Hello' plus 'world'"]
    for python, pseudocode in zip(python_code, pseutopy_code):
        assert pseutopy.convert_from_string(pseudocode) == python + "\n"


def test_arith_expr_multiple_operations(pseutopy):
    python_code = "a = 1 + 2 + 3 - 4 - 5 + (1 + 2) - b + c - my_var"
    pseutopy_code = "a = 1 plus 2 plus 3 minus 4 minus 5 plus (1 plus 2) minus b + c minus my_var"
    assert pseutopy.convert_from_string(pseutopy_code) == python_code + "\n"


def test_term(pseutopy):
    python_code = ["a = 1 * 2", "a = 1 / 2", "a = 1 // 2", "a = 1 % 2"]
    pseutopy_code = ["a = 1 times 2", "a = 1 divided by 2", "a = 1 // 2", "a = 1 modulo 2"]
    for python, pseudocode in zip(python_code, pseutopy_code):
        assert pseutopy.convert_from_string(pseudocode) == python + "\n"


def test_term_multiple_operations(pseutopy):
    python_code = "a = b * c / (2 % 1) // 3"
    pseutopy_code = "a = b times c divided by (2 modulo 1) // 3"
    assert pseutopy.convert_from_string(pseutopy_code) == python_code + "\n"


def test_power(pseutopy):
    python_code = "a = b ** c"
    pseutopy_code = "a = b to the power of c"
    assert pseutopy.convert_from_string(pseutopy_code) == python_code + "\n"


def test_longer_bin_op(pseutopy):
    python_code = "a = 1 + 2 * (3 - 4) % 2 ** c / d - (5 // e + 2)"
    pseutopy_code = "a = 1 plus 2 times (3 minus 4) modulo 2 to the power of c divided by d minus (5 // e + 2)"
    assert pseutopy.convert_from_string(pseutopy_code) == python_code + "\n"
