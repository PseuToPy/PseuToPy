from tests.utils import check_ast
from src.pseutopy.pseutopy import PseuToPy

class TestChainedAssignment:

    def test_assign_a_value_to_a_variable(self, pseutopy):
        frenchPseutopy = PseuToPy("fr")
        pseudo_str = """
        mettre my_var à 1
        mettre my_var1 à my_var2
        mettre my_var à 'Hello'
        mettre my_tuple à (1, my_var, 'Hi')
        mettre my_list à [1, my_var, 'Hi']
        mettre my_dict à {'key1': 1, 2: 'value'}
        mettre my_set à {1, 2, 3}
        """
        python_str = """
my_var = 1
my_var1 = my_var2
my_var = 'Hello'
my_tuple = (1, my_var, 'Hi')
my_list = [1, my_var, 'Hi']
my_dict = {'key1': 1, 2: 'value'}
my_set = {1, 2, 3}
        """
        assert check_ast(frenchPseutopy, python_str, pseudo_str)


    def test_arithmetic_operators(self, pseutopy):
        frenchPseutopy = PseuToPy("fr")
        pseudo_str = """
        mettre my_var à 1 plus 2
        mettre my_var à 1 moins 2
        mettre my_var à moins 4
        mettre my_var à 2 fois 3
        mettre my_var à 2 divisé par 3
        mettre my_var à 2 modulo 3
        mettre my_var à 2 à la puissance 3
        """
        python_str = """
my_var = 1 + 2
my_var = 1 - 2
my_var = -4
my_var = 2 * 3
my_var = 2 / 3
my_var = 2 % 3
my_var = 2 ** 3
        """
        assert check_ast(frenchPseutopy, python_str, pseudo_str)


    def test_comparison_operators(self, pseutopy):
        frenchPseutopy = PseuToPy("fr")
        pseudo_str = """
        mettre my_var à 2 est inférieur ou égal à 3
        mettre my_var à 2 est inférieur à 3
        mettre my_var à 2 est supérieur ou égal à 3
        mettre my_var à 2 est supérieur à 3
        mettre my_var à 2 est égal à 3
        mettre my_var à 2 est différent de 3
        mettre my_var à 2 n'est pas égal à 3
        """
        python_str = """
my_var = 2 <= 3
my_var = 2 < 3
my_var = 2 >= 3
my_var = 2 > 3
my_var = 2 == 3
my_var = 2 != 3
my_var = 2 != 3
        """
        assert check_ast(frenchPseutopy, python_str, pseudo_str)