"""
    Current state of while/else rule:

    while_stmt: "while" test (":" | "do" | "do:") suite ["else" (":" | "do" | "do:") suite]
"""


def test_simple_while(pseutopy):
    python_code = """while 1 < 2:
    a = 2
"""
    pseutopy_code = """
while 1 is lower than 2 do:
    set a to 2
"""
    assert pseutopy.convert_from_string(pseutopy_code) == python_code


def test_while_else(pseutopy):
    python_code = """while 1 < 2:
    a = 2
else:
    a = 3
"""
    pseutopy_code = """
while 1 is lower than 2 do
    set a to 2
else do:
    set a to 3
"""
    assert pseutopy.convert_from_string(pseutopy_code) == python_code


def test_inner_while(pseutopy):
    python_code = """while 1 < 2:
    while a > b:
        a = a + 1
else:
    a = False
"""
    pseutopy_code = """
while 1 is lower than 2 do:
    while a is greater than b:
        set a to a plus 1
else do
    set a to false
"""
    assert pseutopy.convert_from_string(pseutopy_code) == python_code


def test_while_big_body(pseutopy):
    python_code = """while 1 < 2:
    a = 2
    b = 3
    print(a % 2 - b)
"""
    pseutopy_code = """
while 1 is lower than 2 do:
    set a to 2
    b = 3
    print((a % 2) - b)
"""
    assert pseutopy.convert_from_string(pseutopy_code) == python_code

def test_while_else_big_body(pseutopy):
    python_code = """while 1 < 2:
    a = 2
    b = 3
    print(a % 2 - b)
else:
    b = 2
    a = 3
    print(a + b)
"""
    pseutopy_code = """
while 1 is lower than 2 do:
    set a to 2
    b = 3
    print((a % 2) - b)
else do:
    b = 2
    set a to 3
    print(a + b)
"""
    assert pseutopy.convert_from_string(pseutopy_code) == python_code