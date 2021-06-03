"""
    Current state of assign rule: 

    ?assign: (testlist_star_expr ("=" (yield_expr|testlist_star_expr))*)
            | ("set" testlist_star_expr ("to" (yield_expr | testlist_star_expr))*)
"""

def test_simple_assign(pseutopy):
    python_code = 'a = 2'
    pseutopy_code = 'set a to 2'
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code)

def test_tuple_assign(pseutopy):
    python_code = 'a, b = True, 1 < 2'
    pseutopy_code = 'set a, b to true, 1 < 2'
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code)

def test_assign_with_variable(pseutopy):
    python_code = 'a = my_variable'
    pseutopy_code = 'set a to my_variable'
    assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code)

def test_assign_function(pseutopy):
    python_code = ['a = foo()', 'a = b.bar()']
    pseutopy_code = ['set a to foo()', 'set a to b.bar()']
    for python, pseudocode in zip(python_code, pseutopy_code):
        assert pseutopy.convert_to_ast(python) == pseutopy.convert_to_ast(pseudocode)
