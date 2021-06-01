"""
funccall and getattr
"""


def test_func_call(pseutopy):
    python_code = ["foo()", "foo(a)", "foo(a, b, 1, c=True)"]
    pseutopy_code = ["foo()", "foo(a)", "foo(a, b, 1, c=True)"]
    for python, pseudocode in zip(python_code, pseutopy_code):
        assert pseutopy.convert_from_string(pseudocode) == python + "\n"


def test_getattr(pseutopy):
    python_code = ["a.b", "a.b.c"]
    pseutopy_code = ["a.b", "a.b.c"]
    for python, pseudocode in zip(python_code, pseutopy_code):
        assert pseutopy.convert_from_string(pseudocode) == python + "\n"


def test_method_call(pseutopy):
    python_code = ["a.b()", "a.b(c)", "a.b(c, d=\"hello\")"]
    pseutopy_code = ["a.b()", "a.b(c)", "a.b(c, d=\"hello\")"]
    for python, pseudocode in zip(python_code, pseutopy_code):
        assert pseutopy.convert_from_string(pseudocode) == python + "\n"


def test_func_call_mixed(pseutopy):
    python_code = ["a.foo()", "a.foo(a.bar)", "a.foo(a.bar(), b.foo(1), 1, c=True)"]
    pseutopy_code = ["a.foo()", "a.foo(a.bar)", "a.foo(a.bar(), b.foo(1), 1, c=True)"]
    for python, pseudocode in zip(python_code, pseutopy_code):
        assert pseutopy.convert_from_string(pseudocode) == python + "\n"
