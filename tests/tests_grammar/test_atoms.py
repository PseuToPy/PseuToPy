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

def test_name(pseutopy):
    python_code = 'my_var'
    pseutopy_code = 'my_var'
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code)


def test_integer(pseutopy):
    python_code = '1'
    pseutopy_code = '1'
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code)


def test_float(pseutopy):
    python_code = '1.2'
    pseutopy_code = '1.2'
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code)


def test_string(pseutopy):
    python_code = '"A string"'
    pseutopy_code = '"A string"'
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code)


def test_const_none(pseutopy):
    python_code = 'None'
    pseutopy_code = 'none'
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code)


def test_const_true(pseutopy):
    python_code = 'True'
    pseutopy_code = 'true'
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code)


def test_const_false(pseutopy):
    python_code = 'False'
    pseutopy_code = 'false'
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code)


def test_tuple(pseutopy):
    python_code = 'tasks = ("do", "the", test, 5)'
    pseutopy_code = 'tasks = ("do", "the", test, 5)'
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code)


def test_list(pseutopy):
    python_code = 'tasks = ["do", "the", test, 5]'
    pseutopy_code = 'tasks = ["do", "the", test, 5]'
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code)



def test_set(pseutopy):
    python_code = 'primes = {1, 3, b, 7, "11"}'
    pseutopy_code = 'primes = {1, 3, b, 7, "11"}'
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code)


def test_dict(pseutopy):
    template = '''
mydict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1954,
    0 : "Yes"
}
    '''
    python_code = template
    pseutopy_code = template
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code)

def test_atom_expr(pseutopy):
    template = '''
expression{}
    '''
    python_code = [template.format('()'), template.format('.getName()'), template.format(('.property'))]
    pseutopy_code = [template.format('()'), template.format('.getName()'), template.format(('.property'))]
    for py_code, ptp_code in zip(python_code,pseutopy_code):
        assert pseutopy.convert_to_ast(py_code) == pseutopy.convert_to_ast(ptp_code)

def test_test(pseutopy):
    """There is no need to test this rule, as it depends on the `test` rule that we will
    test later. As a reminder, the `test` rule is used for all types of operations."""
    pass
