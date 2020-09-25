from tests.utils import check_ast


class TestChainedAssignment:

    def test_assign_a_value_to_a_variable(self, frPseutopy):
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
        assert check_ast(frPseutopy, python_str, pseudo_str)

    def test_arithmetic_operators(self, frPseutopy):
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
        assert check_ast(frPseutopy, python_str, pseudo_str)

    def test_comparison_operators(self, frPseutopy):
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
        assert check_ast(frPseutopy, python_str, pseudo_str)

    def test_operator_is(self, frPseutopy):
        pseudo_str = """
        mettre my_var à a est b
        mettre my_var à a n'est pas b
        """
        python_str = """
my_var = a is b
my_var = a is not b
        """
        assert check_ast(frPseutopy, python_str, pseudo_str)

    def test_operator_in(self, frPseutopy):
        pseudo_str = """
        mettre my_var à 3 dans my_tuple
        mettre my_var à 3 pas dans my_list
        """
        python_str = """
my_var = 3 in my_tuple
my_var = 3 not in my_list
        """
        assert check_ast(frPseutopy, python_str, pseudo_str)

    def test_boolean_values(self, frPseutopy):
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
        assert check_ast(frPseutopy, python_str, pseudo_str)

    def test_boolean_operators(self, frPseutopy):
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
        assert check_ast(frPseutopy, python_str, pseudo_str)

    def test_input_function(self, frPseutopy):
        pseudo_str = """
        mettre my_var au résultat de la fonction: donnée ('This is a message to prompt the input')
        mettre my_var au résultat de la fonction: donnée "A message", "Another message"
        mettre my_var au résultat de la fonction: donnée entier "my_var will try to be an integer"
        mettre my_var au résultat de la fonction: donnée nombre "my_var will try to be a float"
        """
        python_str = """
my_var = input('This is a message to prompt the input')
my_var = input('A message', 'Another message')
my_var = int(input('my_var will try to be an integer'))
my_var = float(input('my_var will try to be a float'))
        """
        assert check_ast(frPseutopy, python_str, pseudo_str)

    def test_while_statements(self, frPseutopy):
        pseudo_str = """
        tant que vrai faire:
            mettre a à 1
        autrement:
            mettre a à 2
        fin
        """
        python_str = """
while true:
    a = 1
else:
    a = 2
        """
        assert check_ast(frPseutopy, python_str, pseudo_str)

    def test_for_statements(self, frPseutopy):
        pseudo_str = """
        pour i dans la gamme(0,10,1):
            mettre a à i
        autrement:
            mettre a à 2
        fin
        pour i dans (1, 2, 3, 5, 7) faire:
            mettre a à i
        fin
        """
        python_str = """
for i in range(0, 10, 1):
    a = i
else:
    a = 2
for i in (1, 2, 3, 5, 7):
    a = i
        """
        assert check_ast(frPseutopy, python_str, pseudo_str)

    def test_declare_function(self, frPseutopy):
        pseudo_str = """
        définir la fonction foo  avec aucun paramètre:
            mettre my_var à 1
        fin

        définir la fonction foo avec arg1 comme paramètre:
            mettre my_var à arg1
        fin

        définir la fonction bar avec (arg1, arg2) comme paramètres:
            mettre my_var1 à arg1
            mettre my_var2 à arg2
        fin

        définir la fonction bar avec (arg1, arg2) comme paramètres:
            mettre my_var1 à arg1
            mettre my_var2 à arg2
            retourner my_var1, my_var2
        fin
        """
        python_str = """
def foo():
    my_var = 1

def foo(arg1):
    my_var = arg1

def bar(arg1, arg2):
    my_var1 = arg1
    my_var2 = arg2

def bar(arg1, arg2):
    my_var1 = arg1
    my_var2 = arg2
    return my_var1, my_var2
        """
        assert check_ast(frPseutopy, python_str, pseudo_str)

    def test_call_function1(self, frPseutopy):
        pseudo_str = """
        appeler la fonction foo
        mettre my_var au résultat de la fonction: appeler la fonction foo
        """
        python_str = """
foo()
my_var = foo()
        """
        assert check_ast(frPseutopy, python_str, pseudo_str)

    def test_call_function2(self, frPseutopy):
        pseudo_str = """
            mettre my_var au résultat de la fonction: appeler la fonction bar avec comme paramètre 1
            """
        python_str = """
my_var = bar(1)
            """
        assert check_ast(frPseutopy, python_str, pseudo_str)

    def test_call_function3(self, frPseutopy):
        pseudo_str = """
            mettre my_var au résultat de la fonction: appeler la fonction bar avec comme paramètres (1, 2)
            """
        python_str = """
my_var = bar(1, 2)
            """
        assert check_ast(frPseutopy, python_str, pseudo_str)

    def test_print1(self, frPseutopy):
        pseudo_str = """
        afficher 'hello world'
        """
        python_str = """
print('hello world')
        """
        assert check_ast(frPseutopy, python_str, pseudo_str)

    def test_print2(self, frPseutopy):
        pseudo_str = """
        montrer 'hello world'
        """
        python_str = """
print('hello world')
        """
        assert check_ast(frPseutopy, python_str, pseudo_str)

    def test_print3(self, frPseutopy):
        pseudo_str = """
        afficher my_var
        """
        python_str = """
print(my_var)
        """
        assert check_ast(frPseutopy, python_str, pseudo_str)

    def test_pass(self, frPseutopy):
        pseudo_str = """
        passer
        """
        python_str = """
pass
        """
        assert check_ast(frPseutopy, python_str, pseudo_str)

    def test_break(self, frPseutopy):
        pseudo_str = """
        casser
        """
        python_str = """
break
        """
        assert check_ast(frPseutopy, python_str, pseudo_str)

    def test_continue(self, frPseutopy):
        pseudo_str = """
        continuer
        """
        python_str = """
continue
        """
        assert check_ast(frPseutopy, python_str, pseudo_str)


    def test_return(self, frPseutopy):
        pseudo_str = """
        retourner my_var
        """
        python_str = """
return(my_var)
        """
        assert check_ast(frPseutopy, python_str, pseudo_str)

    def test_if_statements(self, frPseutopy):
        pseudo_str = """
        si vrai ou faux:
            mettre my_var à 'Some random value'
        fin

        si vrai alors:
            mettre my_var = 'Some random value'
        sinon si faux alors:
            mettre my_var = 'Some other random value'
        autrement:
            mettre my_var = 'Some other random value'
        fin
        """
        python_str = """
if true or false:
    my_var = 'Some random value'
    
if true:
    my_var = 'Some random value'
elif false:
    my_var = 'Some other random value'
else:
    my_var = 'Some other random value'
        """
        assert check_ast(frPseutopy, python_str, pseudo_str)