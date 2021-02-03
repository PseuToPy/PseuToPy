from tests.utils import check_ast


class TestParenthesisCalcul:
    def test_simple(self, pseutopy):
        pseudo_str = """
        set a to (3)
        set a to (-3)
        set a to (var)
        """
        python_str = """
a = (3)
a = (-3)
a = (var)
        """
        assert check_ast(pseutopy, python_str, pseudo_str)

    def test_addition(self, pseutopy):
        pseudo_str = """
        set a to (1+2)
        set a to (2-1)
        set a to (1+2+3)
        set a to (2-3+4)
        set a to (3 + var)
        """
        python_str = """
a = (1+2)
a = (2-1)
a = (1+2+3)
a = (2-3+4)
a = (3 + var)
        """
        assert check_ast(pseutopy, python_str, pseudo_str)

    def test_multiplication(self, pseutopy):
        pseudo_str = """
        set a to (1*2)
        set a to (2*3*4)
        set a to (5 * var)
        """
        python_str = """
a = (1*2)
a = (2*3*4)
a = (5 * var)
        """
        assert check_ast(pseutopy, python_str, pseudo_str)

    def test_addition_outside(self, pseutopy):
        pseudo_str = """
        set a to (1+2)+3
        set a to 3+(2-1)
        set a to 1+(3+4)+2
        set a to (1+2)+(3+4)
        """
        python_str = """
a = (1+2)+3
a = 3+(2-1)
a = 1+(3+4)+2
a = (1+2)+(3+4)
        """
        assert check_ast(pseutopy, python_str, pseudo_str)

    def test_multiplication_additions(self, pseutopy):
        pseudo_str = """
        set a to (1+2)*3
        set a to 3*(2-1)
        set a to (1+2) * (3+4)
        set a to ((2*3)+4)*5
        """
        python_str = """
a = (1+2)*3
a = 3*(2-1)
a = (1+2) * (3+4)
a = ((2*3)+4)*5
        """
        assert check_ast(pseutopy, python_str, pseudo_str)

    def test_operators(self, pseutopy):
        pseudo_str = """
        set a to (1+2) % 3
        set a to 3 //(2-1)
        set a to (1+2) / (3+4)
        set a to ((2*3) <= 4)*5
        """
        python_str = """
a = (1+2) % 3
a = 3 //(2-1)
a = (1+2) / (3+4)
a = ((2*3) <= 4)*5
        """
        assert check_ast(pseutopy, python_str, pseudo_str)
