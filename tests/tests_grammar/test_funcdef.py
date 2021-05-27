"""
Current state of funcdef rule: 

async_funcdef: "async" funcdef
funcdef: ("def" | "define" "function") NAME "(" parameters? ")" ["->" test] (":" | "to do" | "to do:") suite
"""

def test_func_async(pseutopy):
    template = '''
async {} my_func(){} print("")
    '''
    python_code = template.format('def',':')
    pseutopy_code = [template.format('define function',' to do'), template.format('def',':'), template.format('def',' to do:')]
    for i in range(len(pseutopy_code)):
        assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code[i])

def test_func_1(pseutopy):
    template = '''
{} my_func(a,b){} print(a*b)
    '''
    python_code = template.format('def',':')
    pseutopy_code = [template.format('define function',' to do'), template.format('def',':'), template.format('def',' to do:')]
    for i in range(len(pseutopy_code)):
        assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code[i])

def test_func_2(pseutopy):
    template = '''
{} my_func(a,b){}(2 * a + 3) % 5 == 0{} print(a*b)
    '''
    python_code = template.format('def','->',':')
    pseutopy_code = [template.format('define function','->',' to do'), template.format('def','->',':'), 
    template.format('def','->',' to do:')]
    for i in range(len(pseutopy_code)):
        assert pseutopy.convert_to_ast(python_code) == pseutopy.convert_to_ast(pseutopy_code[i])
