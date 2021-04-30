"""
Current state of if rule: 

if_stmt: "if" test (":" | "then" | "then:") suite (elif_stmt test (":" | "then" | "then:") suite)* ["else" (":" | "then" | "then:") suite]
elif_stmt : ("elif" | "else" "if") -> elseif
"""

def test_if_simple(pseutopy):
    template = '''
if True{} a = 2
    '''
    python_code = template.format((':'))
    pseutopy_code = [template.format((':')), template.format((' then')), template.format((' then:'))]
    for i in range(len(pseutopy_code)):
        assert pseutopy.convert_from_string(python_code) == pseutopy.convert_from_string(pseutopy_code[i])

def test_if_simple_2(pseutopy):
    template = '''
if True{}
    a = 2
    '''
    python_code = template.format((':'))
    pseutopy_code = [template.format((':')), template.format((' then')), template.format((' then:'))]
    for i in range(len(pseutopy_code)):
        assert pseutopy.convert_from_string(python_code) == pseutopy.convert_from_string(pseutopy_code[i])

def test_if_else_simple(pseutopy):
    template = '''
if False{} a = 2
else{} b = 2
    '''
    python_code = template.format(":", ":")
    pseutopy_code = [template.format(":", ":"), template.format(" then", " then"), 
        template.format(" then:", " then:"), template.format(":", " then:"), 
        template.format(" then", ":")]
    for i in range(len(pseutopy_code)):
        assert pseutopy.convert_from_string(python_code) == pseutopy.convert_from_string(pseutopy_code[i])

def test_if_else_simple_2(pseutopy):
    template = '''
if False{}
    a = 2
else{} b = 2
    '''
    python_code = template.format(":", ":")
    pseutopy_code = [template.format(":", ":"), template.format(" then", " then"), 
        template.format(" then:", " then:"), template.format(":", " then:"), 
        template.format(" then", ":")]
    for i in range(len(pseutopy_code)):
        assert pseutopy.convert_from_string(python_code) == pseutopy.convert_from_string(pseutopy_code[i])

def test_if_else_simple_3(pseutopy):
    template = '''
if False{}
    a = 2
else{}
    b = 2
    '''
    python_code = template.format(":", ":")
    pseutopy_code = [template.format(":", ":"), template.format(" then", " then"), 
        template.format(" then:", " then:"), template.format(":", " then:"), 
        template.format(" then", ":")]
    for i in range(len(pseutopy_code)):
        assert pseutopy.convert_from_string(python_code) == pseutopy.convert_from_string(pseutopy_code[i])

def test_elif_simple(pseutopy):
    template = '''
if a >= b - 4{}
    a = 2
{} a == 2{}
    b = 2
else{}
    b = a - b**-3
    '''
    python_code = template.format(":", "elif", ":", ":")
    pseutopy_code = [template.format(":", "elif", ":", ":"), template.format(":", "else if", ":", ":"), 
        template.format(":", "elif", " then:", ":"), template.format(":", "else if", " then", ":")]
    for i in range(len(pseutopy_code)):
        assert pseutopy.convert_from_string(python_code) == pseutopy.convert_from_string(pseutopy_code[i])

def test_elif_simple_2(pseutopy):
    template = '''
if a >= b - 4{} a = 2
{} a == 2{} b = 2
else{} b = a - b**-3
    '''
    python_code = template.format(":", "elif", ":", ":")
    pseutopy_code = [template.format(":", "elif", ":", ":"), template.format(":", "else if", ":", ":"), 
        template.format(":", "elif", " then:", ":"), template.format(":", "else if", " then", ":")]
    for i in range(len(pseutopy_code)):
        assert pseutopy.convert_from_string(python_code) == pseutopy.convert_from_string(pseutopy_code[i])

def test_if_stmt(pseutopy):
    template = '''
if range(a) >= len(b) {}
    a = 2
{} a == 2{} b = 2
{} b == 2{} 
    a = b = a - b**-3
    '''
    python_code = template.format(":", "elif", ":", "elif", ":")
    pseutopy_code = [template.format(":", "elif", ":", "elif", ":"), template.format(" then", "elif", " then:", "else if", ":"),
    template.format(":", "else if", ":", "else if", " then:"), template.format(" then:", "else if", " then", "elif", ":")]
    for i in range(len(pseutopy_code)):
        assert pseutopy.convert_from_string(python_code) == pseutopy.convert_from_string(pseutopy_code[i])