"""
    Current state of unary operators rule:

    plus_op: ("+" | "plus") -> plus
    minus_op : ("-" | "minus") -> minus

    Unary ops are ast.UAdd() and ast.USub() operations
    Note that ast.Not() is also considered a ast.UnaryOp, but is tested in test_parser_bool_op
"""


def test_unary_add(pseutopy):
    python_code = ["a = +1", "a = +b"]
    pseutopy_code = ["a = plus 1", "a = plus b"]
    for python, pseudocode in zip(python_code, pseutopy_code):
        assert pseutopy.convert_from_string(pseudocode) == python + "\n"


def test_unary_sub(pseutopy):
    python_code = ["a = -1", "a = -b"]
    pseutopy_code = ["a = minus 1", "a = minus b"]
    for python, pseudocode in zip(python_code, pseutopy_code):
        assert pseutopy.convert_from_string(pseudocode) == python + "\n"


def test_arith_expr_with_unary_ops(pseutopy):
    python_code = "a = 1 + -3 * 2 ** -2"
    pseutopy_code = "a = 1 plus minus 3 times 2 to the power of minus 2"
    assert pseutopy.convert_from_string(pseutopy_code) == python_code + "\n"
