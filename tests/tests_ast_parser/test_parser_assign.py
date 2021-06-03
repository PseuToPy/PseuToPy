"""
    Current state of assign rule:

    ?assign: (testlist_star_expr ("=" (yield_expr|testlist_star_expr))*)
         | ("set" testlist_star_expr ("to" (yield_expr | testlist_star_expr))*)
"""

def test_assign_simple(pseutopy):
    python_code = "a = 1 ** 2"
    pseutopy_code = ["set a to 1**2", "a=(1**2)"]
    for i in pseutopy_code:
        assert pseutopy.convert_from_string(i) == python_code + "\n"

def test_assign_multiple(pseutopy):
    python_code = "a, b, c = 1, a, b % 2"
    pseutopy_code = ["set a, b, c to 1, a, b % 2", "a,b,c = 1,a,(b % 2)"]
    for i in pseutopy_code:
        assert pseutopy.convert_from_string(i) == python_code + "\n"