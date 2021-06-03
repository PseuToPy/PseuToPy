"""
    Current state of all the boolean rules (and any other rules that are also required)

    ?or_test: and_test ("or" and_test)*
    ?and_test: not_test ("and" not_test)*
    ?not_test: "not" not_test -> not
            | comparison
    ?comparison: expr (_comp_op expr)*
"""


def test_parser_and(pseutopy):
    python_code = ["a = True and False", "a = 1 and 2 and c"]
    pseutopy_code = ["a = true and false", "a = 1 and 2 and c"]
    for python, pseudocode in zip(python_code, pseutopy_code):
        assert pseutopy.convert_from_string(pseudocode) == python + "\n"


def test_parser_or(pseutopy):
    python_code = ["a = True or False", "a = 1 or 2 or c"]
    pseutopy_code = ["a = true or false", "a = 1 or 2 or c"]
    for python, pseudocode in zip(python_code, pseutopy_code):
        assert pseutopy.convert_from_string(pseudocode) == python + "\n"


def test_parser_not(pseutopy):
    python_code = ["a = not True", "a = not False"]
    pseutopy_code = ["a = not true", "a = not false"]
    for python, pseudocode in zip(python_code, pseutopy_code):
        assert pseutopy.convert_from_string(pseudocode) == python + "\n"


def test_bool_op(pseutopy):
    python_code = "a = True and False or (not True or False) and False or not True"
    pseutopy_code = "a = true and false or (not true or false) and false or not true"
    assert pseutopy.convert_from_string(pseutopy_code) == python_code + "\n"
