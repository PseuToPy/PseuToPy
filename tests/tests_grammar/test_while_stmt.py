"""
    Current state of while/else rule: 

    while_stmt: "while" test (":" | "do" | "do:") suite ["else" (":" | "do" | "do:") suite]
"""

def test_while_noelse(pseutopy):
    template = '''
while a%2 == 0{}
    a += 1
    print((a - 5**3) % 3)
    '''
    python_code = template.format(':')
    pseutopy_code = [template.format(':'), template.format(' do'), template.format(' do:')]
    for i in range(len(pseutopy_code)):
        assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code[i])

def test_while_else(pseutopy):
    template = '''
while a%2 == 0{}
    a += 1
    print((a - 5**3) % 3)
else{}
    a = a**3
    print('It is fun to use composed while instruction')
    if a == 8:
        a *= 3
        print(a)
    else: a = "toto"
    '''
    python_code = template.format(':', ':')
    pseutopy_code = [template.format(':', ':'), template.format(' do', ' do'), 
        template.format(':', ' do:'), template.format(' do', ':'), template.format(' do:', ' do:'),
        template.format(' do', ' do:')]
    for i in range(len(pseutopy_code)):
        assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code[i])