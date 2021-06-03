"""
    Current state of all the boolean rules (and any other rules that are also required)

    ?or_test: and_test ("or" and_test)*
    ?and_test: not_test ("and" not_test)*
    ?not_test: "not" not_test -> not
            | comparison
    ?comparison: expr (_comp_op expr)*
"""


def test_or_with_expr_expr(pseutopy):
    """
    or_test: expr "or" expr
    """
    python_code = "True or False"
    pseutopy_code = "true or false"
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code)


def test_or_with_and_expr(pseutopy):
    """
    or_test: and_test "or" expr
    """
    python_code = "True and True or 1 == 0"
    pseutopy_code = "true and true or 1 is equal to 0"
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code)


def test_or_with_expr_and(pseutopy):
    """
    or_test: expr "or" and_test
    """
    python_code = "1 < 2 or True and False"
    pseutopy_code = "1 is lower than 2 or true and false"
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code)


def test_or_with_and_and(pseutopy):
    """
    or_test: and_test ("or" and_test)*
    """
    python_code = ["True and False or True and True", "True and False or True and False or True and False"]
    pseutopy_code = ["true and false or true and true", "true and false or true and false or true and false"]
    for python, pseuto in zip(python_code, pseutopy_code):
        assert pseutopy.convert_to_ast(python) == pseutopy.convert_to_ast(pseuto)


def test_and_with_expr_expr(pseutopy):
    """
    ?and_test: expr "and" expr
    """
    python_code = "True and False"
    pseutopy_code = "true and false"
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code)

def test_and_with_not_expr(pseutopy):
    """
    and_test: not_test "and" expr
    """
    python_code = "not True and 1 == 0"
    pseutopy_code = "not true and 1 is equal to 0"
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code)


def test_and_with_expr_not(pseutopy):
    """
    and_test: expr "and" not_test
    """
    python_code = "1 < 2 and not False"
    pseutopy_code = "1 is lower than 2 and not false"
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code)


def test_and_with_and_and(pseutopy):
    """
    and_test: not_test ("and" not_test)*
    """
    python_code = ["not True and False and not True", "not True and not False and not 1 < 2"]
    pseutopy_code = ["not true and false and not true", "not true and not false and not 1 is lower than 2"]
    for python, pseuto in zip(python_code, pseutopy_code):
        assert pseutopy.convert_to_ast(python) == pseutopy.convert_to_ast(pseuto)


def test_not_simple(pseutopy):
    """
    ?not_test: "not" not_test -> not
         | comparison
    """
    python_code = "not 1 < 2"
    pseutopy_code = "not 1 is lower than 2"
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code)


def test_not_multiple(pseutopy):
    """
    ?not_test: "not" not_test -> not
         | comparison
    """
    python_code = "not not not not not (1 < 2 or False)"
    pseutopy_code = "not not not not not (1 is lower than 2 or false)"
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code)
