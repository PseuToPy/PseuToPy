"""
Current state of assign rule: 

?assign: (testlist_star_expr ("=" (yield_expr|testlist_star_expr))*)
         | ("set" testlist_star_expr ("to" (yield_expr | testlist_star_expr))*)
"""

def test_simple_assign(pseutopy):
    python_code = 'a = 2'
    pseutopy_code = 'set a to 2'
    assert pseutopy.convert_from_string(python_code) == pseutopy.convert_from_string(pseutopy_code)

def test_tuple_assign(pseutopy):
    python_code = 'a, b = True, 1 < 2'
    pseutopy_code = 'set a, b to true, 1 < 2'
    assert pseutopy.convert_from_string(python_code) == pseutopy.convert_from_string(pseutopy_code)

def test_assign_with_variable(pseutopy):
    python_code = 'a = my_variable'
    pseutopy_code = 'set a to my_variable'
    assert pseutopy.convert_from_string(python_code) == pseutopy.convert_from_string(pseutopy_code)

def test_assign_function(pseutopy):
    # TODO: Complete this when function calls are defined
    pass
