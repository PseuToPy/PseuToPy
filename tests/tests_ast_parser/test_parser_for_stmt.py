"""
Current state of for rule: 

for_stmt: "for" exprlist "in" testlist (":" | "do" | "do:") suite ["else" (":" | "do" | "do:") suite]
"""

def test_simple_for(pseutopy):
    python_code = """for i in 5:
    a = a + i
"""
    pseutopy_code = """
for i in 5 do
    set a to a + i
"""
    assert pseutopy.convert_from_string(pseutopy_code) == python_code

def test_for_orelse(pseutopy):
    python_code = """for i in 5:
    a = a + i
    print(a)
else:
    b = a + 1
"""
    pseutopy_code = """
for i in 5 do:
    a = a + i
    print(a)
else do set b to (a + 1)
"""
    assert pseutopy.convert_from_string(pseutopy_code) == python_code

def test_for_orelse_with_stmt_inside(pseutopy):
    python_code = """for i in 5:
    if i <= 3:
        print(a)
        do_something(len(tab) - a)
    elif i > 3:
        a = len(super_tab)
    else:
        print("There is something wrong here")
else:
    while cmp < 5:
        print(cmp)
        if cmp - a < 2:
            b = cmp
        elif a < cmp:
            print(a - cmp)
"""
    pseutopy_code = """
for i in 5:
    if i<= 3 then
        print(a)
        do_something(len(tab)-a)
    elif i is greater than 3 then:
        a = len(super_tab)
    else: print("There is something wrong here")
else do:
    while cmp < 5 do
        print(cmp)
        if (cmp-a)<2 then:
            set b to cmp
        elif a is lower than cmp: print(a- cmp)
"""
    assert pseutopy.convert_from_string(pseutopy_code) == python_code