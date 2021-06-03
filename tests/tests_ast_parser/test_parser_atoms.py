"""
Current state of the `atom` rule:

?atom: "(" [yield_expr|tuplelist_comp] ")" -> tuple
     | "[" [testlist_comp] "]"  -> list
     | "{" [dict_comp] "}" -> dict
     | "{" set_comp "}" -> set
     | NAME -> var
     | number | string+
     | "(" test ")"
     | "..." -> ellipsis
     | ("None" | "none")    -> const_none
     | ("True" | "true")    -> const_true
     | ("False" | "false")    -> const_false
"""


def test_const_none(pseutopy):
    pseudo_code = ["a = none", "a = None", "set a to none", "set a to None"]
    python_code = "a = None"
    for i in pseudo_code:
        assert pseutopy.convert_from_string(i) == python_code + '\n'


def test_const_true(pseutopy):
    pseudo_code = ["isTrue = true", "isTrue = True", "set isTrue to true", "set isTrue to True"]
    python_code = "isTrue = True"
    for i in pseudo_code:
        assert pseutopy.convert_from_string(i) == python_code + '\n'


def test_const_false(pseutopy):
    pseudo_code = ["isFalse = false", "isFalse = False", "set isFalse to false", "set isFalse to False"]
    python_code = "isFalse = False"
    for i in pseudo_code:
        assert pseutopy.convert_from_string(i) == python_code + '\n'


def test_decimal_number(pseutopy):
    pseudo_code = ["a = 1", "set a to 1"]
    python_code = "a = 1"
    for i in pseudo_code:
        assert pseutopy.convert_from_string(i) == python_code + '\n'


def test_float_number(pseutopy):
    pseudo_code = ["a = 1.05", "set a to 1.05"]
    python_code = "a = 1.05"
    for i in pseudo_code:
        assert pseutopy.convert_from_string(i) == python_code + '\n'


def test_name(pseutopy):
    pseudo_code = ["my_var = a", "set my_var to a"]
    python_code = "my_var = a"
    for i in pseudo_code:
        assert pseutopy.convert_from_string(i) == python_code + '\n'


def test_set(pseutopy):
    pseudo_code = ['primes = {1, 3, b, 7, "11"}', "primes = {1, 3, b, 7, '11'}"]
    python_code = 'primes = {1, 3, b, 7, "11"}'
    for i in pseudo_code:
        assert pseutopy.convert_from_string(i) == python_code + '\n'

def test_dict(pseutopy):
    pseudo_code = 'dict = {1: "11", "1": 11, 2: a, "s": {1, 2, "3"}}'
    python_code = 'dict = {1: "11", "1": 11, 2: a, "s": {1, 2, "3"}}'
    assert pseutopy.convert_from_string(pseudo_code) == python_code + '\n'

def test_list(pseutopy):
    pseudo_code = 'list = [1, 2, "test", a, false]'
    python_code = 'list = [1, 2, "test", a, False]'
    assert pseutopy.convert_from_string(pseudo_code) == python_code + '\n'


def test_tuple(pseutopy):
    pseudo_code = 'tuple = (1, true, "test", a)'
    python_code = 'tuple = (1, True, "test", a)'
    assert pseutopy.convert_from_string(pseudo_code) == python_code + '\n'