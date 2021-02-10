from tests.utils import check_ast


# class TestStatement:
#     def test_input_statement(self, pseutopy):
#         pseudo_str = """
#         input "This is the message to display"
#         input "This is a message", "And another one"
#         input "This is a message", myVar
#         input(myVar)
#         input(1)
#         input(myVar, "This is a text", 1)
#         input(True, "This is a text")
#         """
#         python_str = """
# input("This is the message to display")
# input("This is a message", "And another one")
# input("This is a message", myVar)
# input(myVar)
# input(1)
# input(myVar, "This is a text", 1)
# input(True, "This is a text")
#         """
#         assert check_ast(pseutopy, python_str, pseudo_str)
#
#     def test_int_input_statement(self, pseutopy):
#         pseudo_str = """
#         input integer "This is the message to display"
#         input integer "This is a message", "And another one"
#         input integer "This is a message", myVar
#         input integer (myVar)
#         input integer (1)
#         input integer (myVar, "This is a text", 1)
#         input integer(True, "This is a text")
#         """
#         python_str = """
# int(input("This is the message to display"))
# int(input("This is a message", "And another one"))
# int(input("This is a message", myVar))
# int(input(myVar))
# int(input(1))
# int(input(myVar, "This is a text", 1))
# int(input(True, "This is a text"))
#         """
#         assert check_ast(pseutopy, python_str, pseudo_str)
#
#     def test_float_input_statement(self, pseutopy):
#         pseudo_str = """
#         input number "This is the message to display"
#         input number "This is a message", "And another one"
#         input number "This is a message", myVar
#         input number (myVar)
#         input number (1)
#         input number (myVar, "This is a text", 1)
#         input number(True, "This is a text")
#         """
#         python_str = """
# float(input("This is the message to display"))
# float(input("This is a message", "And another one"))
# float(input("This is a message", myVar))
# float(input(myVar))
# float(input(1))
# float(input(myVar, "This is a text", 1))
# float(input(True, "This is a text"))
#         """
#         assert check_ast(pseutopy, python_str, pseudo_str)
#
#     def test_print_statements(self, pseutopy):
#         pseudo_str = """
#         print "This is a message"
#         print "This is a message", "And another one"
#         print 1
#         print myVar
#         display("This is a message", 1, myVar)
#         show("This is a message" followed by var1 followed by var2, var3)
#         show "This is a message" followed by var1 followed by var2, var3
#         """
#         python_str = """
# print("This is a message")
# print("This is a message", "And another one")
# print(1)
# print(myVar)
# print("This is a message", 1, myVar)
# print("This is a message", var1, var2, var3)
# print("This is a message", var1, var2, var3)
#         """
#         assert check_ast(pseutopy, python_str, pseudo_str)
#
#     def test_func_call_statements(self, pseutopy):
#         pseudo_str = """
#         call function foo
#         call function foobar with parameter 1
#         call function foobar with parameters 1
#         call function foobar with parameter 1, 2
#         call function foobar with parameters 1, 2
#         call function foobar with parameter a
#         call function foobar with parameters (a, b)
#         call function foobar with parameters ((a,"This is a message"), 3)
#         """
#         python_str = """
# foo()
# foobar(1)
# foobar(1)
# foobar(1, 2)
# foobar(1, 2)
# foobar(a)
# foobar(a, b)
# foobar((a, "This is a message"), 3)
#         """
#         assert check_ast(pseutopy, python_str, pseudo_str)
#
#     def test_del_statments(self, pseutopy):
#         pseudo_str = "del myVar"
#         python_str = "del myVar"
#         assert check_ast(pseutopy, python_str, pseudo_str)
#
#     def test_if_statement(self, pseutopy):
#         pseudo_str = """
#         if True then
#         set a to 1
#         end
#         """
#         python_str = """
# if True:
#     a = 1
#         """
#         assert check_ast(pseutopy, python_str, pseudo_str)
#
#     def test_if_elif_statement(self, pseutopy):
#         pseudo_str = """
#         if a <= b then
#         set a to 1
#         else if a > b:
#         set a to 2
#         end
#         """
#         python_str = """
# if a <= b:
#     a = 1
# elif a > b:
#     a = 2
#         """
#         assert check_ast(pseutopy, python_str, pseudo_str)
#
#     def test_if_else_statement(self, pseutopy):
#         pseudo_str = """
#         if a <= b then
#         set a to 1
#         else:
#         set a to 2
#         end
#         """
#         python_str = """
# if a <= b:
#     a = 1
# else:
#     a = 2
#         """
#         assert check_ast(pseutopy, python_str, pseudo_str)
#
#     def test_if_elif_else_statement(self, pseutopy):
#         pseudo_str = """
#         if a <= b then
#         set a to 1
#         else if a > b:
#         set a to 2
#         else then:
#         set a to 3
#         end
#         """
#         python_str = """
# if a <= b:
#     a = 1
# elif a > b:
#     a = 2
# else:
#     a = 3
#         """
#         assert check_ast(pseutopy, python_str, pseudo_str)
#
#     def test_while_statement(self, pseutopy):
#         pseudo_str = """
#         while a <= b do:
#         set a to 1
#         end
#
#         while a < b:
#         set a to 2
#         end
#
#         while a < b do
#         set a to 1
#         end
#         """
#         python_str = """
# while a <= b:
#     a = 1
#
# while a < b:
#     a = 2
#
# while a < b:
#     a = 1
#         """
#         assert check_ast(pseutopy, python_str, pseudo_str)
#
#     def test_for_range_statement(self, pseutopy):
#         pseudo_str = """
#         for i in range(0, 10, 1) do:
#         set a to i
#         end
#         """
#         python_str = """
# for i in range(0, 10, 1):
#     a = i
#         """
#         assert check_ast(pseutopy, python_str, pseudo_str)
#
#     def test_for_tuple_statement(self, pseutopy):
#         pseudo_str = """
#         for i in (1, 2, 5, 6):
#         set a to i
#         end
#         """
#         python_str = """
# for i in (1, 2, 5, 6):
#     a = i
#         """
#         assert check_ast(pseutopy, python_str, pseudo_str)
#
#     def test_for_list_statement(self, pseutopy):
#         pseudo_str = """
#         for i in [1, 2, 5, 6]:
#         set a to i
#         end
#         """
#         python_str = """
# for i in [1, 2, 5, 6]:
#     a = i
#         """
#         assert check_ast(pseutopy, python_str, pseudo_str)
#
#     def test_func_def_no_parameter_statement(self, pseutopy):
#         pseudo_str = """
#         define function foo with no parameter:
#         set a to 1
#         end
#         """
#         python_str = """
# def foo():
#     a = 1
#         """
#         assert check_ast(pseutopy, python_str, pseudo_str)
#
#     def test_func_def_parameter_statement(self, pseutopy):
#         pseudo_str = """
#         def foo with arg1 as parameter:
#         set a to arg1
#         end
#         """
#         python_str = """
# def foo(arg1):
#     a = arg1
#         """
#         assert check_ast(pseutopy, python_str, pseudo_str)
#
#     def test_func_def_multiple_parameters_statement(self, pseutopy):
#         pseudo_str = """
#         def foo with (arg1, arg2) as parameter:
#         set a to arg1
#         set b to arg2
#         end
#         """
#         python_str = """
# def foo(arg1, arg2):
#     a = arg1
#     b = arg2
#         """
#         assert check_ast(pseutopy, python_str, pseudo_str)
#
#     def test_func_def_multiple_parameters_statement_2(self, pseutopy):
#         pseudo_str = """
#         def foo with arg1, arg2 as parameters:
#         set a to arg1
#         set b to arg2
#         end
#         """
#         python_str = """
# def foo(arg1, arg2):
#     a = arg1
#     b = arg2
#         """
#         assert check_ast(pseutopy, python_str, pseudo_str)
#
#     def test_func_def_multiple_parameters_single_return_statement_(self,
#                                                                    pseutopy):
#         pseudo_str = """
#         def foo with arg1, arg2 as parameters:
#         set a to arg1 + arg2
#         return a
#         end
#         """
#         python_str = """
# def foo(arg1, arg2):
#     a = arg1 + arg2
#     return a
#         """
#         assert check_ast(pseutopy, python_str, pseudo_str)
#
#     def test_func_def_multiple_parameters_multiple_return_statement_(self,
#                                                                      pseutopy):
#         pseudo_str = """
#         def foo with arg1, arg2 as parameters:
#         set a to arg1
#         set b to arg2
#         return a, b
#         end
#         """
#         python_str = """
# def foo(arg1, arg2):
#     a = arg1
#     b = arg2
#     return a, b
#         """
#         assert check_ast(pseutopy, python_str, pseudo_str)
