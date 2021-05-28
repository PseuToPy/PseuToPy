"""
Current state of the `atom` rule:

?atom: "(" [yield_expr|tuplelist_comp] ")" -> tuple
     | "[" [testlist_comp] "]"  -> list
     | "{" [dict_comp] "}" -> dict
     | "{" set_comp "}" -> set
     | NAME -> var
     | number | string+
     | "(" test ")"
     | "..." -> ellipsis
     | ("None" | "none")    -> const_none
     | ("True" | "true")    -> const_true
     | ("False" | "false")    -> const_false
"""


def test_const_none(pseutopy):
     pseudo_code = ["a = none", "a = None", "set a to none", "set a to None"]
     python_code = "a = None"
     for i in pseudo_code:
          assert pseutopy.convert_from_string(i) == python_code + '\n'


def test_const_true(pseutopy):
     pseudo_code = ["isTrue = true", "isTrue = True", "set isTrue to true", "set isTrue to True"]
     python_code = "isTrue = True"
     for i in pseudo_code:
          assert pseutopy.convert_from_string(i) == python_code + '\n'


def test_const_false(pseutopy):
     pseudo_code = ["isFalse = false", "isFalse = False", "set isFalse to false", "set isFalse to False"]
     python_code = "isFalse = False"
     for i in pseudo_code:
          assert pseutopy.convert_from_string(i) == python_code + '\n'


def test_decimal_number(pseutopy):
     pseudo_code = ["a = 1", "set a to 1"]
     python_code = "a = 1"
     for i in pseudo_code:
          assert pseutopy.convert_from_string(i) == python_code + '\n'
          

def test_float_number(pseutopy):
     pseudo_code = ["a = 1.05", "set a to 1.05"]
     python_code = "a = 1.05"
     for i in pseudo_code:
          assert pseutopy.convert_from_string(i) == python_code + '\n'


def test_name(pseutopy):
     pseudo_code = ["my_var = a", "set my_var to a"]
     python_code = "my_var = a"
     for i in pseudo_code:
          assert pseutopy.convert_from_string(i) == python_code + '\n'