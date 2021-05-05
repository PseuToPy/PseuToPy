"""
Current state of for rule: 

for_stmt: "for" exprlist "in" testlist (":" | "do" | "do:") suite ["else" (":" | "do" | "do:") suite]
"""

def test_for_1(pseutopy):
    template = '''
for n in range(2, max){} print(n, 'is a prime number')
    '''
    python_code = template.format((':'))
    pseutopy_code = [template.format((':')), template.format((' do')), template.format((' do:'))]
    for i in range(len(pseutopy_code)):
        assert pseutopy.convert_from_string(python_code) == pseutopy.convert_from_string(pseutopy_code[i])

def test_for_2(pseutopy):
    template = '''
for n in range(2, max){}
    for x in range(2, n){}
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else{}
        print(n, 'is a prime number')
        break
    '''
    python_code = template.format(':', ':', ':')
    pseutopy_code = [template.format(':', ':', ':'), template.format(':', ' do:', ' do'),
        template.format(' do:', ':', ':'), template.format(' do', ':', ' do:'), 
        template.format(':', ' do:', ' do')]
    for i in range(len(pseutopy_code)):
        assert pseutopy.convert_from_string(python_code) == pseutopy.convert_from_string(pseutopy_code[i])