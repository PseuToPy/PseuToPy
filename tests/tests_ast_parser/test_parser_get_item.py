"""
    Current state of the rule:

    ?atom_expr: atom_expr "(" [arguments] ")"      -> funccall
          | atom_expr "[" subscriptlist "]"  -> getitem
          | atom_expr "." NAME               -> getattr
          | atom


    subscript: test | ([test] ":" [test] [sliceop]) -> slice
    sliceop: ":" [test]
"""


def test_subscript(pseutopy):
    python_code = ["a[1]", "a[b]"]
    pseutopy_code = ["a[1]", "a[b]"]
    for python, pseudocode in zip(python_code, pseutopy_code):
        assert pseutopy.convert_from_string(pseudocode) == python + "\n"


def test_slice_without_step(pseutopy):
    python_code = ["a[1:10]", "a[b:10]"]
    pseutopy_code = ["a[1:10]", "a[b:10]"]
    for python, pseudocode in zip(python_code, pseutopy_code):
        assert pseutopy.convert_from_string(pseudocode) == python + "\n"


def test_slice_with_step(pseutopy):
    python_code = ["a[1:10:1]", "a[b:10:2]"]
    pseutopy_code = ["a[1:10:1]", "a[b:10:2]"]
    for python, pseudocode in zip(python_code, pseutopy_code):
        assert pseutopy.convert_from_string(pseudocode) == python + "\n"
