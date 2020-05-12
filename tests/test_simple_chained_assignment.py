from tests.utils import check_ast


class TestSimpleChainedAssignment:
    def test_simple_chained_assignment_declare_stmt(self, pseutopy):
        pseudo_str = "declare myVar"
        python_str = "myVar = None"
        assert check_ast(pseutopy, python_str, pseudo_str)

    def test_simple_chained_assignment_set_none(self, pseutopy):
        pseudo_str = "set myVar to None"
        python_str = "myVar = None"
        assert check_ast(pseutopy, python_str, pseudo_str)

    def test_simple_chained_assignment_set_simple_value(self, pseutopy):
        pseudo_str = "set myVar to 1"
        python_str = "myVar = 1"
        assert check_ast(pseutopy, python_str, pseudo_str)

    def test_simple_chained_assignment_set_unary_value(self, pseutopy):
        pseudo_str = """
        set myVar to plus 1
        set myVar to minus 2
        set myVar to not True
        """
        python_str = """
myVar = +1
myVar = -2
myVar = not True
        """
        assert check_ast(pseutopy, python_str, pseudo_str)

    def test_simple_chained_assignment_set_identifier(self, pseutopy):
        pseudo_str = "set myVar to a"
        python_str = "myVar = a"
        assert check_ast(pseutopy, python_str, pseudo_str)

    def test_simple_chained_assignment_set_tuple(self, pseutopy):
        pseudo_str = """
        set myVar to ()
        set myVar to (1,)
        set myVar to (1, 2, 3)
        """
        python_str = """
myVar = ()
myVar = (1,)
myVar = (1, 2, 3)
        """
        assert check_ast(pseutopy, python_str, pseudo_str)

    def test_simple_chained_assignment_set_list(self, pseutopy):
        pseudo_str = """
        set myVar to []
        set myVar to [1,]
        set myVar to [1, 2, 3]
        """
        python_str = """
myVar = []
myVar = [1]
myVar = [1, 2, 3]
        """
        assert check_ast(pseutopy, python_str, pseudo_str)

    def test_simple_chained_assignment_set_dict(self, pseutopy):
        pseudo_str = """
        set myVar to {}
        set myVar to {1: 1}
        set myVar to {1: a}
        set myVar to {1: "Hello", 2:"Hi"}
        """
        python_str = """
myVar = {}
myVar = {1: 1}
myVar = {1: a}
myVar = {1: "Hello", 2: "Hi"}
        """
        assert check_ast(pseutopy, python_str, pseudo_str)

    def test_simple_chained_assignment_set_set(self, pseutopy):
        pseudo_str = """
        set myVar to {}
        set myVar to {1,}
        set myVar to {1, a}
        """
        python_str = """
myVar = {}
myVar = {1}
myVar = {1, a}
        """
        assert check_ast(pseutopy, python_str, pseudo_str)

    def test_simple_chained_assignment_set_arith_expr(self, pseutopy):
        pseudo_str = """
        set myVar to 3 plus 4
        set myVar to 3 minus 4
        set myVar to 3 divided by 4
        set myVar to 3 times 4
        set myVar to 3 modulo 4
        set myVar to 3 to the power of 4
        set myVar to 1 plus 2 minus 3 times 4 divided by 5 modulo 6"""
        python_str = """
myVar = 3 + 4
myVar = 3 - 4
myVar = 3 / 4
myVar = 3 * 4
myVar = 3 % 4
myVar = 3 ** 4
myVar = 1 + 2 - 3 * 4 / 5 % 6
        """
        assert check_ast(pseutopy, python_str, pseudo_str)

    def test_simple_chained_assignment_set_boolean(self, pseutopy):
        pseudo_str = """
        set myVar to true
        set myVar to false"""
        python_str = """
myVar = True
myVar = False
        """
        assert check_ast(pseutopy, python_str, pseudo_str)

    def test_simple_chained_assignment_bool_op(self, pseutopy):
        pseudo_str = """
        set myVar to true and false
        set myVar to false or true"""
        python_str = """
myVar = True and False
myVar = False or True
        """
        assert check_ast(pseutopy, python_str, pseudo_str)

    def test_simple_chained_assignment_comparison(self, pseutopy):
        pseudo_str = """
        set myVar to 3 is lower than 4
        set myVar to 3 is lower or equal to 4
        set myVar to 3 is greater than 4
        set myVar to 3 is greater or equal to 4
        set myVar to 3 is equal to 4
        set myVar to 3 is different from 4
        set myVar to 3 is not equal to 4
        set myVar to 1 in 2
        set myVar to 1 not in 2
        set myVar to 1 is 2
        set myVar to 1 is not 2
        """
        py_str = """
myVar = 3 < 4
myVar = 3 <= 4
myVar = 3 > 4
myVar = 3 >= 4
myVar = 3 == 4
myVar = 3 != 4
myVar = 3 != 4
myVar = 1 in 2
myVar = 1 not in 2
myVar = 1 is 2
myVar = 1 is not 2
"""
        assert check_ast(pseutopy, py_str, pseudo_str)
