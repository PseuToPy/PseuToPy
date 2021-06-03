"""
    Current state of the `power` rule (plus any non-obvious rules that the `power` rule is
    based on):

    ?power: await_expr (("**" | "to the power of") factor)?
    ?factor: _factor_op factor | power
    ?await_expr: AWAIT? atom_expr
"""


def test_power_1(pseutopy):
    python_code = 'a ** b'
    pseutopy_code = ['a**b', 'a to the power of b']
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code[0])
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code[1])

def test_power_2(pseutopy):
    python_code = '1 ** 2 ** 3'
    pseutopy_code = ['1 ** 2 ** 3', '1 to the power of 2 to the power of 3']
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code[0])
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code[1])

def test_power_3(pseutopy):
    python_code = '1 ** (2 ** 3)'
    pseutopy_code = ['1 ** (2 ** 3)', '1 to the power of (2 to the power of 3)']
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code[0])
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code[1])

def test_power_4(pseutopy):
    python_code = '1 ** a ** 2'
    pseutopy_code = ['1 ** a ** 2', '1 to the power of a to the power of 2']
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code[0])
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code[1])

def test_power_5(pseutopy):
    python_code = 'a ** -b'
    pseutopy_code = ['a ** -b', 'a to the power of minus b']
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code[0])
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code[1])

def test_power_6(pseutopy):
    python_code = '1 ** +2'
    pseutopy_code = ['1 ** +2', '1 to the power of plus 2']
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code[0])
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code[1])
