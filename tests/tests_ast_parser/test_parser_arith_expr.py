"""
Current state of the `arith_expr` rule (plus any rules that the `arith_expr` rule is based
on:)

?arith_expr: term (_add_op term)*
?term: factor (_mul_op factor)*
?factor: factor_op factor | power
"""


def test_add(pseutopy):
    python_code = ["a = 1 + 2\n", "a = 1 - 2\n"]
    pseutopy_code = ["a = 1 plus 2", "a = 1 minus 2"]
    for python, pseudocode in zip(python_code, pseutopy_code):
        assert pseutopy.convert_from_string(pseudocode) == python

def test_add_multiple_operations(pseutopy):
    python_code = "a = 1 + 2 + 3 - 4 - 5 + (1 + 2) - b + c - my_var\n"
    pseutopy_code = "a = 1 plus 2 plus 3 minus 4 minus 5 plus (1 plus 2) minus b + c minus my_var"
    assert pseutopy.convert_from_string(pseutopy_code) == python_code