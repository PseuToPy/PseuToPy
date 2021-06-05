"""
    Current state of funcdef rule:

    async_funcdef: "async" funcdef
    funcdef: ("def" | "define" "function") NAME "(" parameters? ")" ["->" test] (":" | "to do" | "to do:") suite
"""


def test_funcdef_flow_stmt(pseutopy):
    python_code = """def foo():
    pass
    continue
    break
    return a
"""
    pseutopy_code = """
define function foo() to do:
    pass
    continue
    break
    return a
"""
    assert pseutopy.convert_from_string(pseutopy_code) == python_code


def test_funcdef_simple(pseutopy):
    python_code = """def foo():
    print(a)
    return a
"""
    pseutopy_code = """
define function foo() to do:
    print(a)
    return a
"""
    assert pseutopy.convert_from_string(pseutopy_code) == python_code


def test_funcdef_arguments(pseutopy):
    python_code = """def foo(a):
    return a
"""
    pseutopy_code = """
define function foo(a) to do:
    return a
"""
    assert pseutopy.convert_from_string(pseutopy_code) == python_code


def test_funcdef_defaults(pseutopy):
    python_code = """def foo(a=True):
    print(a)
    return a
"""
    pseutopy_code = """
define function foo(a = true) to do
    print(a)
    return a
"""
    assert pseutopy.convert_from_string(pseutopy_code) == python_code


def test_funcdef_args(pseutopy):
    python_code = """def foo(*args):
    print(a)
    return a
"""
    pseutopy_code = """
define function foo(*args) to do
    print(a)
    return a
"""
    assert pseutopy.convert_from_string(pseutopy_code) == python_code


def test_funcdef_kwargs(pseutopy):
    python_code = """def foo(**kwargs):
    print(a)
    return a
"""
    pseutopy_code = """
define function foo(**kwargs) to do
    print(a)
    return a
"""
    assert pseutopy.convert_from_string(pseutopy_code) == python_code


def test_funcdef_total(pseutopy):
    python_code = """def foo(a, b=1, *args, **kwargs):
    print(a)
    return a
"""
    pseutopy_code = """
define function foo(a, b=1, *args, **kwargs) to do
    print(a)
    return a
"""
    assert pseutopy.convert_from_string(pseutopy_code) == python_code


def test_funcdef_return(pseutopy):
    python_code = """def foo():
    return a, b, 1
"""
    pseutopy_code = """
define function foo() to do
    return a, b, 1
"""
    assert pseutopy.convert_from_string(pseutopy_code) == python_code
