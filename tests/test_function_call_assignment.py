from tests.utils import check_ast


class TestFunctionCallAssignment:
    def test_function_call_assignment_input(self, enPseutopy):
        pseudo_str = "set a to the result of input (\"Hello\", myVar)"
        python_str = "a = input(\"Hello\", myVar)"
        assert check_ast(enPseutopy, python_str, pseudo_str)

    def test_function_call_assignment_input_int(self, enPseutopy):
        pseudo_str = "set a to the result of input integer (1)"
        python_str = "a = int(input(1))"
        assert check_ast(enPseutopy, python_str, pseudo_str)

    def test_function_call_assignment_input_float(self, enPseutopy):
        pseudo_str = "set a to the result of input number (\"Hello\")"
        python_str = "a = float(input(\"Hello\"))"
        assert check_ast(enPseutopy, python_str, pseudo_str)

    def test_function_call_assignment_with_function(self, enPseutopy):
        pseudo_str = """
        set a to the result of call function foo with parameter 10
        set b to the result of call function bar with parameters 0, 10
        set c to the result of call function foobar with parameter myVar
        set d to the result of call function fizzbuzz with parameters var1, var2
        set e to the result of call function fizbuz
        """
        python_str = """
a = foo(10)
b = bar(0, 10)
c = foobar(myVar)
d = fizzbuzz(var1, var2)
e = fizbuz()
        """
        assert check_ast(enPseutopy, python_str, pseudo_str)

    def test_function_call_assignment_with_TestList(self, enPseutopy):
        pseudo_str = """
        set a to the result of range(10)
        set b to the result of range(0, 10)
        set c to the result of range(var1)
        set d to the result of range(var1, var2)
        """
        python_str = """
a = range(10)
b = range(0, 10)
c = range(var1)
d = range(var1, var2)
        """
        assert check_ast(enPseutopy, python_str, pseudo_str)
