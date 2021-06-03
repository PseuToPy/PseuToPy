"""
    Current state of if/elif/else rule:

    if_stmt: "if" test (":" | "then" | "then:") suite (elif_stmt test (":" | "then" | "then:") suite)* ["else" (":" | "then" | "then:") suite]
    elif_stmt : ("elif" | "else" "if") -> elseif
"""



def test_simple_if(pseutopy):
    python_code = """if a < b:
    a = 2
"""
    pseutopy_code = """
if a is lower than b then
    set a to 2
"""
    assert pseutopy.convert_from_string(pseutopy_code) == python_code


def test_simple_if_else(pseutopy):
    python_code = """if a < b:
    a = 2
else:
    b = 2
"""
    pseutopy_code = """
if a is lower than b then
    set a to 2
else then
    set b to 2
"""
    assert pseutopy.convert_from_string(pseutopy_code) == python_code


def test_simple_if_elif(pseutopy):
    python_code = """if a < b:
    a = 2
elif a > b:
    b = 2
"""
    pseutopy_code = """
if a is lower than b then
    set a to 2
else if a is greater than b then
    set b to 2
"""
    assert pseutopy.convert_from_string(pseutopy_code) == python_code


def test_simple_if_elif_else(pseutopy):
    python_code = """if a < b:
    a = 2
elif a > b:
    b = 2
else:
    c = 2
"""
    pseutopy_code = """
if a is lower than b then
    set a to 2
else if a is greater than b:
    set b to 2
else then:
    set c to 2
"""
    assert pseutopy.convert_from_string(pseutopy_code) == python_code


def test_inner_if(pseutopy):
    python_code = """if a < b:
    if c > d:
        e = 2
    elif c < d:
        e = 3
    else:
        e = 4
"""
    pseutopy_code = """
if a is lower than b then:
    if c is greater than d then
        set e to 2
    else if c is lower than d then:
        set e to 3
    else:
        set e to 4
"""
    assert pseutopy.convert_from_string(pseutopy_code) == python_code