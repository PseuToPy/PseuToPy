from tests.utils import check_ast
from src.pseutopy.pseutopy import PseuToPy

class TestChainedAssignment:

    def test_assign_a_value_to_a_variable(self, pseutopy):
        frenchPseutopy = PseuToPy("fr")
        pseudo_str = """
        mettre my_var à 1
        mettre my_var à 2
        """
        python_str = """
my_var = 1
my_var = 2
        """
        assert check_ast(frenchPseutopy, python_str, pseudo_str)


    def test_chained_assignment_set_none(self, pseutopy):
        frenchPseutopy = PseuToPy("fr")
        pseudo_str = """
        mettre my_var à 1
        """
        python_str = """
my_var = 1
        """
        assert check_ast(frenchPseutopy, python_str, pseudo_str)