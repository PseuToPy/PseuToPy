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

from src.pseutopy.pseutopy import PseuToPy

def test_is_lower_than(pseutopy):
    python_code = ['1 < 2', '2 < 1', '1**2 < 1 + 2*3']
    pseutopy_code = ['1 < 2', '1 is lower than 2', '2 < 1', '2 is lower than 1', '1**2 < 1 + 2*3', '1**2 is lower than 1 + 2*3']
    assert pseutopy.convert_from_string(python_code[0]) == pseutopy.convert_from_string(pseutopy_code[0])
    assert pseutopy.convert_from_string(python_code[0]) == pseutopy.convert_from_string(pseutopy_code[1])
    assert pseutopy.convert_from_string(python_code[1]) == pseutopy.convert_from_string(pseutopy_code[2])
    assert pseutopy.convert_from_string(python_code[1]) == pseutopy.convert_from_string(pseutopy_code[3])
    assert pseutopy.convert_from_string(python_code[2]) == pseutopy.convert_from_string(pseutopy_code[4])
    assert pseutopy.convert_from_string(python_code[2]) == pseutopy.convert_from_string(pseutopy_code[5])

def test_is_greater_than(pseutopy):
    python_code = ['2 > 0', '0 > 2', '1 - 1 > -2 + 1']
    pseutopy_code = ['2 > 0', '2 is greater than 0', '0 > 2', '0 is greater than 2', '1 - 1 > -2 + 1', '1 - 1 is greater than -2 + 1']
    assert pseutopy.convert_from_string(python_code[0]) == pseutopy.convert_from_string(pseutopy_code[0])
    assert pseutopy.convert_from_string(python_code[0]) == pseutopy.convert_from_string(pseutopy_code[1])
    assert pseutopy.convert_from_string(python_code[1]) == pseutopy.convert_from_string(pseutopy_code[2])
    assert pseutopy.convert_from_string(python_code[1]) == pseutopy.convert_from_string(pseutopy_code[3])
    assert pseutopy.convert_from_string(python_code[2]) == pseutopy.convert_from_string(pseutopy_code[4])
    assert pseutopy.convert_from_string(python_code[2]) == pseutopy.convert_from_string(pseutopy_code[5])

def test_is_equal_to(pseutopy):
    python_code = ['3 == 3', '2 == 3', '-1 == 2 - 3']
    pseutopy_code = ['3 == 3', '3 is equal to 3', '2 == 3', '2 is equal to 3', '-1 == 2 - 3', '-1 is equal to 2 - 3']
    assert pseutopy.convert_from_string(python_code[0]) == pseutopy.convert_from_string(pseutopy_code[0])
    assert pseutopy.convert_from_string(python_code[0]) == pseutopy.convert_from_string(pseutopy_code[1])
    assert pseutopy.convert_from_string(python_code[1]) == pseutopy.convert_from_string(pseutopy_code[2])
    assert pseutopy.convert_from_string(python_code[1]) == pseutopy.convert_from_string(pseutopy_code[3])
    assert pseutopy.convert_from_string(python_code[2]) == pseutopy.convert_from_string(pseutopy_code[4])
    assert pseutopy.convert_from_string(python_code[2]) == pseutopy.convert_from_string(pseutopy_code[5])

def test_is_lower_or_equal_to(pseutopy):
    python_code = ['2 <= 3', '3 <= 2', '2 <= 3*0 / 2']
    pseutopy_code = ['2 <= 3', '2 is lower or equal to 3', '3 <= 2', '3 is lower or equal to 2', '2 <= 3*0 / 2', '2 is lower or equal to 3*0 / 2']
    assert pseutopy.convert_from_string(python_code[0]) == pseutopy.convert_from_string(pseutopy_code[0])
    assert pseutopy.convert_from_string(python_code[0]) == pseutopy.convert_from_string(pseutopy_code[1])
    assert pseutopy.convert_from_string(python_code[1]) == pseutopy.convert_from_string(pseutopy_code[2])
    assert pseutopy.convert_from_string(python_code[1]) == pseutopy.convert_from_string(pseutopy_code[3])
    assert pseutopy.convert_from_string(python_code[2]) == pseutopy.convert_from_string(pseutopy_code[4])
    assert pseutopy.convert_from_string(python_code[2]) == pseutopy.convert_from_string(pseutopy_code[5])

def test_is_greater_or_equal_to(pseutopy):
    python_code = ['4 >= 3', '2 >= 3', '1 / (2*4 - 3) >= 9']
    pseutopy_code = ['4 >= 3', '4 is greater or equal to 3', '2 >= 3', '2 is greater or equal to 3', '1 / (2*4 - 3) >= 9', '1 / (2*4 - 3) is greater or equal to 9']
    assert pseutopy.convert_from_string(python_code[0]) == pseutopy.convert_from_string(pseutopy_code[0])
    assert pseutopy.convert_from_string(python_code[0]) == pseutopy.convert_from_string(pseutopy_code[1])
    assert pseutopy.convert_from_string(python_code[1]) == pseutopy.convert_from_string(pseutopy_code[2])
    assert pseutopy.convert_from_string(python_code[1]) == pseutopy.convert_from_string(pseutopy_code[3])
    assert pseutopy.convert_from_string(python_code[2]) == pseutopy.convert_from_string(pseutopy_code[4])
    assert pseutopy.convert_from_string(python_code[2]) == pseutopy.convert_from_string(pseutopy_code[5])

def test_is_greater_or_equal_to(pseutopy):
    python_code = ['4 != 3', '3**-2 != (5 - 2) / 2']
    pseutopy_code = ['4 != 3', '4 is not equal to 3', '4 is different from 3', '3**-2 != (5 - 2) / 2', '3**-2 is not equal to (5 - 2) / 2', '3**-2 is different from (5 - 2) / 2']
    assert pseutopy.convert_from_string(python_code[0]) == pseutopy.convert_from_string(pseutopy_code[0])
    assert pseutopy.convert_from_string(python_code[0]) == pseutopy.convert_from_string(pseutopy_code[1])
    assert pseutopy.convert_from_string(python_code[0]) == pseutopy.convert_from_string(pseutopy_code[2])
    assert pseutopy.convert_from_string(python_code[1]) == pseutopy.convert_from_string(pseutopy_code[3])
    assert pseutopy.convert_from_string(python_code[1]) == pseutopy.convert_from_string(pseutopy_code[4])
    assert pseutopy.convert_from_string(python_code[1]) == pseutopy.convert_from_string(pseutopy_code[5])

def test_in(pseutopy):
    python_code = ['2 in range(4)', '3 in range(len(tab))']
    pseutopy_code = ['2 in range(4)', '3 in range(len(tab))']
    assert pseutopy.convert_from_string(python_code[0]) == pseutopy.convert_from_string(pseutopy_code[0])
    assert pseutopy.convert_from_string(python_code[1]) == pseutopy.convert_from_string(pseutopy_code[1])

def test_not_in(pseutopy):
    python_code = ['2 not in range(1)', '3**n not in range(b)']
    pseutopy_code = ['2 not in range(1)', '3**n not in range(b)']
    assert pseutopy.convert_from_string(python_code[0]) == pseutopy.convert_from_string(pseutopy_code[0])
    assert pseutopy.convert_from_string(python_code[1]) == pseutopy.convert_from_string(pseutopy_code[1])

def test_is(pseutopy):
    python_code = 'var is var'
    pseutopy_code = 'var is var'
    assert pseutopy.convert_from_string(python_code) == pseutopy.convert_from_string(pseutopy_code)

def test_is_not(pseutopy):
    python_code = 'var_x is not var_y'
    pseutopy_code = 'var_x is not var_y'
    assert pseutopy.convert_from_string(python_code) == pseutopy.convert_from_string(pseutopy_code)