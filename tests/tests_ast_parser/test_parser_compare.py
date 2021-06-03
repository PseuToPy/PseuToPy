"""
    Current state of comparison operator :

    _comp_op: less_than_op
            | more_than_op
            | equal_to_op
            | less_or_equal_to_op
            | more_or_equal_to_op
            | "<>"
            | is_not_equal_to_op
            | in_op
            | not_in_op
            | is_op
            | is_not_op
    less_than_op: ("<" | "is" "lower" "than") -> less_than
    more_than_op: (">" | "is" "greater" "than") -> more_than
    equal_to_op: ("==" | "is" "equal" "to") -> equal_to
    less_or_equal_to_op: ("<=" | "is" "lower" "or" "equal" "to") -> less_or_equal_to
    more_or_equal_to_op: (">=" | "is" "greater" "or" "equal" "to") -> more_or_equal_to
    is_not_equal_to_op: ("!=" | "is" "not" "equal" "to" | "is" "different" "from") -> is_not_equal_to
    in_op: ("in") -> in
    not_in_op: ("not" "in") -> not_in
    is_op: ("is") -> is
    is_not_op: ("is" "not") -> is_not
"""


def test_lt_ltE(pseutopy):
    python_code = ["a = 1 < 2", "a = 1 < 2 < 3", "a = 1 <= 3", "a = 1 <= 3 < 4 <= 5"]
    pseutopy_code = ["a = 1 is lower than 2", "a = 1 is lower than 2 is lower than 3",
                     "a = 1 is lower or equal to 3",
                     "a = 1 is lower or equal to 3 is lower than 4 is lower or equal to 5"]
    for python, pseudocode in zip(python_code, pseutopy_code):
        assert pseutopy.convert_from_string(pseudocode) == python + "\n"


def test_gt_gtE(pseutopy):
    python_code = ["a = 1 > 2", "a = 1 > 2 > 3", "a = 1 >= 3", "a = 1 >= 3 > 4 >= 5"]
    pseutopy_code = ["a = 1 is greater than 2", "a = 1 is greater than 2 is greater than 3",
                     "a = 1 is greater or equal to 3",
                     "a = 1 is greater or equal to 3 is greater than 4 is greater or equal to 5"]
    for python, pseudocode in zip(python_code, pseutopy_code):
        assert pseutopy.convert_from_string(pseudocode) == python + "\n"


def test_equality_inequality(pseutopy):
    python_code = ["a = True == False", "a = True != False", "a = 1 == 2 != 3 == 4"]
    pseutopy_code = ["a = true is equal to false", "a = true is different from false",
                     "a = 1 is equal to 2 is not equal to 3 is equal to 4"]
    for python, pseudocode in zip(python_code, pseutopy_code):
        assert pseutopy.convert_from_string(pseudocode) == python + "\n"


def test_in(pseutopy):
    python_code = ["a = 1 in b", "a = 1 not in b"]
    pseutopy_code = ["a = 1 in b", "a = 1 not in b"]
    for python, pseudocode in zip(python_code, pseutopy_code):
        assert pseutopy.convert_from_string(pseudocode) == python + "\n"


def test_is(pseutopy):
    python_code = ["a = 1 is b", "a = 1 is not b"]
    pseutopy_code = ["a = 1 is b", "a = 1 is not b"]
    for python, pseudocode in zip(python_code, pseutopy_code):
        assert pseutopy.convert_from_string(pseudocode) == python + "\n"