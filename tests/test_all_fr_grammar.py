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

    def test_operator_is(self, pseutopy):
        frenchPseutopy = PseuToPy("fr")
        pseudo_str = """
        mettre my_var à a est b
        mettre my_var à a n'est pas b
        """
        python_str = """
my_var = a is b
my_var = a is not b
        """
        assert check_ast(frenchPseutopy, python_str, pseudo_str)

    def test_operator_in(self, pseutopy):
        frenchPseutopy = PseuToPy("fr")
        pseudo_str = """
        mettre my_var à 3 dans my_tuple
        mettre my_var à 3 pas dans my_list
        """
        python_str = """
my_var = 3 in my_tuple
my_var = 3 not in my_list
        """
        assert check_ast(frenchPseutopy, python_str, pseudo_str)

    def test_boolean_values(self, pseutopy):
        frenchPseutopy = PseuToPy("fr")
        pseudo_str = """
        mettre my_var à vrai
        mettre my_var à Vrai
        mettre my_var à faux
        mettre my_var à Faux
        """
        python_str = """
my_var = true
my_var = true
my_var = false
my_var = false
        """
        assert check_ast(frenchPseutopy, python_str, pseudo_str)

    def test_boolean_operators(self, pseutopy):
        frenchPseutopy = PseuToPy("fr")
        pseudo_str = """
        mettre my_var à vrai et faux
        mettre my_var à vrai ou faux
        mettre my_var à non vrai
        """
        python_str = """
my_var = true and false
my_var = true or false
my_var = not true
        """
        assert check_ast(frenchPseutopy, python_str, pseudo_str)