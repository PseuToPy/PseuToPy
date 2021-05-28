"""
Current state of the `atom` rule:

?atom: "(" [yield_expr|tuplelist_comp] ")" -> tuple
     | "[" [testlist_comp] "]"  -> list
     | "{" [dict_comp] "}" -> dict
     | "{" set_comp "}" -> set
     | NAME -> var
     | number | string+
     | "(" test ")"
     | "..." -> ellipsis
     | ("None" | "none")    -> const_none
     | ("True" | "true")    -> const_true
     | ("False" | "false")    -> const_false
"""

