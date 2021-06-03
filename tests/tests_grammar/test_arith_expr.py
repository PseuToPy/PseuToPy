"""
    Current state of the `arith_expr` rule (plus any rules that the `arith_expr` rule is based
    on:)

    ?arith_expr: term (_add_op term)*
    ?term: factor (_mul_op factor)*
    ?factor: factor_op factor | power
"""


def test_addition(pseutopy):
    python_code = ['a + b', '1 + 2', 'a + 1.2', '"Hello" + "world"', 'True + False']
    pseutopy_code = ['a plus b', '1 plus 2', 'a plus 1.2', '"Hello" plus "world"', 'true plus false']
    for i in range(len(python_code)):
        assert pseutopy.convert_to_ast(python_code[i]) == pseutopy.convert_to_ast(pseutopy_code[i])


def test_subtraction(pseutopy):
    python_code = ['a - b', '1 - 2', 'a - 1.2', 'True - False']
    pseutopy_code = ['a minus b', '1 minus 2', 'a minus 1.2', 'true minus false']
    for i in range(len(python_code)):
        assert pseutopy.convert_to_ast(python_code[i]) == pseutopy.convert_to_ast(pseutopy_code[i])

def test_multiplication(pseutopy):
    python_code = ['a * b', '1 * 2', 'a * 1.2', 'True * False']
    pseutopy_code = ['a times b', '1 times 2', 'a times 1.2', 'true times false']
    for i in range(len(python_code)):
        assert pseutopy.convert_to_ast(python_code[i]) == pseutopy.convert_to_ast(pseutopy_code[i])


def test_division(pseutopy):
    python_code = ['a / b', '1 / 2', 'a / 1.2', 'True / False']
    pseutopy_code = ['a divided by b', '1 divided by 2', 'a divided by 1.2', 'true divided by false']
    for i in range(len(python_code)):
        assert pseutopy.convert_to_ast(python_code[i]) == pseutopy.convert_to_ast(pseutopy_code[i])


def test_modulo(pseutopy):
    python_code = ['a % b', '1 % 2', 'a % 1.2', 'True % False']
    pseutopy_code = ['a modulo b', '1 modulo 2', 'a modulo 1.2', 'true modulo false']
    for i in range(len(python_code)):
        assert pseutopy.convert_to_ast(python_code[i]) == pseutopy.convert_to_ast(pseutopy_code[i])


def test_longer_arith_expr(pseutopy):
    python_code = ['a + (2 - 3) * 1.2 / 3 % a ** 2', 'True * True + (1.2 / 2) - 4 ** (2+3)']
    pseutopy_code = ['a plus (2 minus 3) times 1.2 divided by 3 modulo a to the power of 2', 'true times true plus (1.2 divided by 2) minus 4 to the power of (2 plus 3)']
    for i in range(len(python_code)):
        assert pseutopy.convert_to_ast(python_code[i]) == pseutopy.convert_to_ast(pseutopy_code[i])
