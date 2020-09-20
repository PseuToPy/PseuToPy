from tests.utils import check_ast


class TestChainedAssignment:
    def test_chained_assignment_set_none(self, enPseutopy):
        pseudo_str = """
        set myVar1, myVar2 to None, None
        set [myVar1, myVar2] to None, None
        """
        python_str = """
myVar1, myVar2 = None, None
[myVar1, myVar2] = None, None
        """
        assert check_ast(enPseutopy, python_str, pseudo_str)

    def test_chained_assignment_set_simple_value(self, enPseutopy):
        pseudo_str = """
        set myVar1, myVar2 to 1, 2
        set [myVar1, myVar2] to 1, 2
        """
        python_str = """
myVar1, myVar2 = 1, 2
[myVar1, myVar2] = 1, 2
        """
        assert check_ast(enPseutopy, python_str, pseudo_str)

    def test_chained_assignment_set_unary_value(self, enPseutopy):
        pseudo_str = """
        set myVar1, myVar2, myVar3 to (plus 1, minus 2, not False)
        set [myVar1, myVar2, myVar3] to plus 1, minus 2, not True
        """
        python_str = """
myVar1, myVar2, myVar3 = +1, -2, not False
[myVar1, myVar2, myVar3] = +1, -2, not True
        """
        assert check_ast(enPseutopy, python_str, pseudo_str)

    def test_chained_assignment_set_identifier(self, enPseutopy):
        pseudo_str = """
        set myVar1, myVar2 to a, b
        set [myVar1, myVar2] to a, b
        """
        python_str = """
myVar1, myVar2 = a, b
[myVar1, myVar2] = a, b
        """
        assert check_ast(enPseutopy, python_str, pseudo_str)

    def test_chained_assignment_set_tuple(self, enPseutopy):
        pseudo_str = """
        set myVar1, myVar2 to (1, 2), (3, 4)
        set [myVar1, myVar2] to (1, 2), (3, 4)
        """
        python_str = """
myVar1, myVar2 = (1, 2), (3, 4)       
[myVar1, myVar2] = (1, 2), (3, 4)
        """
        assert check_ast(enPseutopy, python_str, pseudo_str)

    def test_chained_assignment_set_list(self, enPseutopy):
        pseudo_str = """
        set myVar1, myVar2 to [1, 2], [3, 4, 5]
        set [myVar1, myVar2] to [1, 2], [3, 4, 5]
        """
        python_str = """
myVar1, myVar2 = [1, 2], [3, 4, 5]       
[myVar1, myVar2] = [1, 2], [3, 4, 5]
        """
        assert check_ast(enPseutopy, python_str, pseudo_str)

    def test_chained_assignment_set_dict(self, enPseutopy):
        pseudo_str = """
        set myVar1, myVar2 to {1: 'Hello', 2: 'Hi'}, {2: True}
        set [myVar1, myVar2] to {1: 'Hello', 2: 'Hi'}, {2: True}
        """
        python_str = """
myVar1, myVar2 = {1: 'Hello', 2: 'Hi'}, {2: True}       
[myVar1, myVar2] = {1: 'Hello', 2: 'Hi'}, {2: True}
        """
        assert check_ast(enPseutopy, python_str, pseudo_str)

    def test_chained_assignment_set_set(self, enPseutopy):
        pseudo_str = """
        set myVar1, myVar2 to {1, 2, 3}, {True, False}
        set [myVar1, myVar2] to {1, 2, 3}, {True, False}
        """
        python_str = """
myVar1, myVar2 = {1, 2, 3}, {True, False}
[myVar1, myVar2] = {1, 2, 3}, {True, False}
        """
        assert check_ast(enPseutopy, python_str, pseudo_str)

    def test_chained_assignment_set_arith_expr(self, enPseutopy):
        pseudo_str = """
        set myVar1, myVar2 to 1 + 2 - 3 % 8, 5 / 4 * 5
        set [myVar1, myVar2] to 1 + 2 - 3 % 8, 5 / 4 * 5
        """
        python_str = """
myVar1, myVar2 = 1 + 2 - 3 % 8, 5 / 4 * 5
[myVar1, myVar2] = 1 + 2 - 3 % 8, 5 / 4 * 5
        """
        assert check_ast(enPseutopy, python_str, pseudo_str)

    def test_chained_assignment_set_boolean(self, enPseutopy):
        pseudo_str = """
        set myVar1, myVar2 to True, False
        set [myVar1, myVar2] to True, False
        """
        python_str = """
myVar1, myVar2 = True, False
[myVar1, myVar2] = True, False
        """
        assert check_ast(enPseutopy, python_str, pseudo_str)

    def test_chained_assignment_bool_op(self, enPseutopy):
        pseudo_str = """
        set myVar1, myVar2 to True and False, False or False
        set [myVar1, myVar2] to True and False, False or False
        """
        python_str = """
myVar1, myVar2 = True and False, False or False
[myVar1, myVar2] = True and False, False or False
        """
        assert check_ast(enPseutopy, python_str, pseudo_str)

    def test_chained_assignment_comparison(self, enPseutopy):
        pseudo_str = """
        set myVar1, myVar2 to 3 is lower than 4, 3 is lower or equal to 4
        set [myVar1, myVar2] to 3 is greater than 4, 3 is greater or equal to 4
        """
        python_str = """
myVar1, myVar2 = 3 < 4, 3 <= 4
[myVar1, myVar2] = 3 > 4, 3 >= 4
        """
        assert check_ast(enPseutopy, python_str, pseudo_str)
