"""
This module contains lots of classes that represent each rule that can be parsed by Lark.
To organize this module a little bit, we will try to:
- Keep token classes before tree classes
- Keep atom classes before expression classes
- Keep expression classes before statement classes
"""
import ast

#####################
##  Token classes  ##
#####################
import lark


class Decimal:
    @staticmethod
    def to_node(token):
        return ast.Constant(value=int(token.value), kind=None)


class Float:
    @staticmethod
    def to_node(token):
        return ast.Constant(value=float(token.value), kind=None)


class StringToken:
    @staticmethod
    def to_node(token):
        return ast.Constant(value=token.value, kind=None)


class Name:
    @staticmethod
    def to_node(token):
        return ast.Name(id=token.value, ctx=ast.Store())


####################
##  Tree classes  ##
####################

class Number:
    @staticmethod
    def to_node(token):
        return read_node(token[0].type).to_node(token[0])


class Var:
    @staticmethod
    def to_node(token):
        return read_node(token[0].type).to_node(token[0])


class String:
    @staticmethod
    def to_node(token):
        return read_node(token[0].type).to_node(token[0])


####################
##  Atom classes  ##
####################

class ConstTrue:
    @staticmethod
    def to_node(token):
        return ast.Constant(value=True, kind=None)


class ConstFalse:
    @staticmethod
    def to_node(token):
        return ast.Constant(value=False, kind=None)


class ConstNone:
    @staticmethod
    def to_node(token):
        return ast.Constant(value=None, kind=None)


class Set:
    @staticmethod
    def to_node(tree):
        return read_node(tree[0].data).to_node(tree[0].children)


class SetComp:
    @staticmethod
    def to_node(children):
        elts = [read_node(child.children[0].type).to_node(child.children[0]) for child in children]
        return ast.Set(elts=elts)


class Dict:
    @staticmethod
    def to_node(tree):
        return read_node(tree[0].data).to_node(tree[0].children)


class DictComp:
    @staticmethod
    def to_node(keysValues):
        keys = [read_node(child.children[0].data).to_node(child.children[0].children) for child in keysValues]
        values = [read_node(child.children[1].data).to_node(child.children[1].children) for child in keysValues]
        return ast.Dict(keys=keys, values=values)


class List:
    @staticmethod
    def to_node(tree):
        return read_node(tree[0].data).to_node(tree[0].children, 'list')


class Tuple:
    @staticmethod
    def to_node(tree):
        return read_node(tree[0].data).to_node(tree[0].children, 'tuple')


class TupleListComp:
    @staticmethod
    def to_node(children, type):
        if type == 'tuple':
            elts = [read_node(child.data).to_node(child.children) for child in children]
            return ast.Expression(body=ast.Tuple(elts=elts))
        else:
            elts = [read_node(child.data).to_node(child.children) for child in children]
            return ast.List(elts=elts)


##########################
##  Expression classes  ##
##########################


class TestlistStarExpr:
    @staticmethod
    def to_node(tree):
        elts = [read_node(child.data).to_node(child.children) for child in tree]
        return ast.Tuple(elts=elts)


class BinOp:
    @staticmethod
    def to_node(tree):
        if len(tree) == 3:
            left, op, right = [read_node(child.data).to_node(child.children) for child in tree]
            return ast.BinOp(left=left, op=op, right=right)
        else:
            right = read_node(tree[-1].data).to_node(tree[-1].children)
            op = read_node(tree[-2].data).to_node(tree[-2].children)
            left = read_node('arith_expr').to_node(tree[:-2])
            return ast.BinOp(left=left, op=op, right=right)


class ArithPlus:
    @staticmethod
    def to_node(tree):
        return ast.Add()


class ArithMinus:
    @staticmethod
    def to_node(tree):
        return ast.Sub()


class Mult:
    @staticmethod
    def to_node(tree):
        return ast.Mult()


class Div:
    @staticmethod
    def to_node(tree):
        return ast.Div()


class Mod:
    @staticmethod
    def to_node(tree):
        return ast.Mod()


class FloorDiv:
    @staticmethod
    def to_node(tree):
        return ast.FloorDiv()


class Power:
    @staticmethod
    def to_node(tree):
        left, right = [read_node(child.data).to_node(child.children) for child in tree]
        return ast.BinOp(left=left, op=ast.Pow(), right=right)


class Pow:
    @staticmethod
    def to_node(tree):
        return ast.Pow()


class And:
    @staticmethod
    def to_node(tree):
        op = ast.And()
        values = [read_node(child.data).to_node(child.children) for child in tree]
        return ast.BoolOp(op=op, values=values)


class Or:
    @staticmethod
    def to_node(tree):
        op = ast.Or()
        values = [read_node(child.data).to_node(child.children) for child in tree]
        return ast.BoolOp(op=op, values=values)


class Not:
    @staticmethod
    def to_node(tree):
        op = ast.Not()
        operand = read_node(tree[0].data).to_node(tree[0].children)
        return ast.UnaryOp(op=op, operand=operand)


class Factor:
    @staticmethod
    def to_node(tree):
        op, operand = [read_node(child.data).to_node(child.children) for child in tree]
        return ast.UnaryOp(op=op, operand=operand)


class UnaryAdd:
    @staticmethod
    def to_node(tree):
        return ast.UAdd()


class UnarySub:
    @staticmethod
    def to_node(tree):
        return ast.USub()


class Comparison:
    @staticmethod
    def to_node(tree):
        left = read_node(tree[0].data).to_node(tree[0].children)
        ops = [read_node(child.data).to_node(child.children) for index, child in enumerate(tree[1:]) if index % 2 == 0]
        comparators = [read_node(child.data).to_node(child.children) for index, child in enumerate(tree[1:]) if
                       index % 2 == 1]
        return ast.Compare(left=left, ops=ops, comparators=comparators)


class LessThan:
    @staticmethod
    def to_node(tree):
        return ast.Lt()


class LessOrEqualTo:
    @staticmethod
    def to_node(tree):
        return ast.LtE()


class MoreThan:
    @staticmethod
    def to_node(tree):
        return ast.Gt()


class MoreOrEqualTo:
    @staticmethod
    def to_node(tree):
        return ast.GtE()


class EqualTo:
    @staticmethod
    def to_node(tree):
        return ast.Eq()


class IsNotEqualTo:
    @staticmethod
    def to_node(tree):
        return ast.NotEq()


class In:
    @staticmethod
    def to_node(tree):
        return ast.In()


class NotIn:
    @staticmethod
    def to_node(tree):
        return ast.NotIn()


class Is:
    @staticmethod
    def to_node(tree):
        return ast.Is()


class IsNot:
    @staticmethod
    def to_node(tree):
        return ast.IsNot()


class ListExpr:
    @staticmethod
    def to_node(tree):
        return read_node(tree[0].data).to_node(tree[0].children)


class GetItem:
    @staticmethod
    def to_node(tree):
        value, slice = [read_node(child.data).to_node(child.children) for child in tree]
        return ast.Subscript(value=value, slice=slice, ctx=ast.Load(), type_ignores=[])


class Subscript:
    @staticmethod
    def to_node(tree):
        lower = read_node(tree[0].data).to_node(tree[0].children)
        return ast.Index(value=lower)


class LowerSlice:
    @staticmethod
    def to_node(tree):
        lower = read_node(tree[0].data).to_node(tree[0].children)
        return ast.Slice(lower=lower, upper=None, step=None)


class UpperSlice:
    @staticmethod
    def to_node(tree):
        upper = read_node(tree[0].data).to_node(tree[0].children)
        return ast.Slice(lower=None, upper=upper, step=None)


class Slice:
    @staticmethod
    def to_node(tree):
        lower = read_node(tree[0].data).to_node(tree[0].children)
        upper = None if len(tree) < 2 else read_node(tree[1].data).to_node(tree[1].children)
        step = None if len(tree) < 3 else read_node(tree[2].data).to_node(tree[2].children)
        return ast.Slice(lower=lower, upper=upper, step=step)


class SliceOp:
    @staticmethod
    def to_node(tree):
        return read_node(tree[0].data).to_node(tree[0].children)


##########################
##  Statements classes  ##
##########################


class Assign:
    @staticmethod
    def to_node(children):
        """
        Assign rule can match multiple things:
        - a = 1
        - a, b = 1, 2
        :param children: The list that belongs to the Assign Tree
        :return: The ast.Assign node to be inserted into the ast.Module
        """
        left, right = children
        targets = [read_node(left.data).to_node(left.children)]
        value = read_node(right.data).to_node(right.children)
        return ast.Assign(targets=targets, value=value)


class AugAssign:
    @staticmethod
    def to_node(tree):
        target = read_node(tree[0].data).to_node(tree[0].children)
        op = read_node(tree[1].value).to_node(tree[1])
        value = read_node(tree[2].data).to_node(tree[2].children)
        return ast.AugAssign(target=target, op=op, value=value)


class MatMult:
    @staticmethod
    def to_node(tree):
        return ast.MatMult()


class BitAnd:
    @staticmethod
    def to_node(tree):
        return ast.BitAnd()


class BitOr:
    @staticmethod
    def to_node(tree):
        return ast.BitOr()


class BitXor:
    @staticmethod
    def to_node(tree):
        return ast.BitXor()


class LeftShift:
    @staticmethod
    def to_node(tree):
        return ast.LShift()


class RightShift:
    @staticmethod
    def to_node(tree):
        return ast.RShift()


class TestList:
    @staticmethod
    def to_node(tree):
        return read_node(tree[0].data).to_node(tree[0].children)


class CompoundStmt:
    @staticmethod
    def to_node(tree):
        return read_node(tree[0].data).to_node(tree[0].children)


class IfStmt:
    @staticmethod
    def to_node(tree):
        """
        If statements are created recursively with 'elif' and 'else' statements being inserted in their respective
        outer 'if/elif' statements.

        Because the way Lark generates the IfStmt tree (which is not a tree but a flat list with 'else_if' rules,
        we use a single class to manage both these cases. As a consequence, this adds some complexity to this method
        when generating the `orelse` attribute of the `ast.If` node.
        :param tree:
        :return:
        """
        is_else_if = False
        if tree[0].data == 'elseif':
            tree.pop(0)
            is_else_if = True
        test = read_node(tree[0].data).to_node(tree[0].children)
        body = read_node(tree[1].data).to_node(tree[1].children)
        if len(tree) == 2:  # There is no elif/else statement
            orelse = []
        elif len(tree) == 3:  # There is a final `else` statement
            orelse = read_node(tree[2].data).to_node(tree[2].children)
        else:  # There is a `elif` statement
            orelse = read_node(tree[2].data).to_node(tree[2:])
        return [ast.If(test=test, body=body, orelse=orelse)] if is_else_if else ast.If(test=test, body=body,
                                                                                       orelse=orelse)


class Suite:
    @staticmethod
    def to_node(tree):
        return [ast.Expr(value=read_node(child.data).to_node(child.children)) for child in tree]


class WhileStmt:
    @staticmethod
    def to_node(tree):
        test = read_node(tree[0].data).to_node(tree[0].children)
        body = read_node(tree[1].data).to_node(tree[1].children)
        orelse = read_node(tree[2].data).to_node(tree[2].children) if len(tree) > 2 else []
        return ast.While(test=test, body=body, orelse=orelse)


class FuncDef:
    @staticmethod
    def to_node(tree):
        name = str(tree[0])
        args, body = None, []
        for child in tree[1:]:
            if child.data == "parameters":
                args = read_node(tree[1].data).to_node(tree[1].children)
            else:
                body = [ast.Expr(value=read_node(element.data).to_node(element.children)) if element.data == "funccall"
                        else read_node(element.data).to_node(element.children)
                        for element in child.children]
        if not args:
            args = ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])
        return ast.FunctionDef(name=name, args=args, body=body, decorator_list=[], returns=None)


class Parameter:
    @staticmethod
    def to_node(tree):
        args, defaults, varargs, kwargs = [], [], None, None
        for child in tree:
            if isinstance(child, lark.Token):
                args.append(ast.arg(arg=str(child), annotation=None))
            else:
                if child.data == 'paramvalue':
                    arg, default = (read_node(child.data).to_node(child.children))
                    args.append(arg)
                    defaults.append(default)
                elif child.data == 'starparams':
                    varargs, kwargs = (read_node(child.data).to_node(child.children))
                elif child.data == 'kwparams':
                    kwargs = read_node(child.data).to_node(child.children)
        return ast.arguments(posonlyargs=[], args=args, vararg=varargs, kwonlyargs=[], kw_defaults=[], kwarg=kwargs,
                             defaults=defaults)


class ParamValue:
    @staticmethod
    def to_node(tree):
        arg = read_node(tree[0].type).to_node(tree[0])
        default = read_node(tree[1].data).to_node(tree[1].children)
        return arg, default


class StarParam:
    @staticmethod
    def to_node(tree):
        args, kwargs = None, None
        for child in tree:
            if isinstance(child, lark.Token):
                args = ast.arg(arg=str(child), annotation=None)
            else:
                kwargs = read_node(child.data).to_node(child.children)
        return args, kwargs


class KwParam:
    @staticmethod
    def to_node(tree):
        return ast.arg(arg=str(tree[0]), annotation=None)


class ReturnStmt:
    @staticmethod
    def to_node(tree):
        value = read_node(tree[0].data).to_node(tree[0].children)
        return ast.Return(value=value)


class TestlistTuple:
    @staticmethod
    def to_node(tree):
        elts = [read_node(child.data).to_node(child.children) for child in tree]
        return ast.Tuple(elts=elts, ctx=ast.Load())


class PassStmt:
    @staticmethod
    def to_node(tree):
        return ast.Pass()


class ContinueStmt:
    @staticmethod
    def to_node(tree):
        return ast.Continue()


class BreakStmt:
    @staticmethod
    def to_node(tree):
        return ast.Break()


class FuncCall:
    @staticmethod
    def to_node(tree):
        func = read_node(tree[0].data).to_node(tree[0].children)
        args, keywords = (read_node(tree[1].data).to_node(tree[1].children)) if len(tree) > 1 else ([], [])
        return ast.Call(func=func, args=args, keywords=keywords)


class GetAttribute:
    @staticmethod
    def to_node(tree):
        value = read_node(tree[0].data).to_node(tree[0].children)
        attr = read_node(tree[1].type).to_node(tree[1])
        return ast.Attribute(value=value, attr=attr)


class Argument:
    @staticmethod
    def to_node(tree):
        args, keywords = [], []
        for child in tree:
            if child.data == 'argvalue' or child.data == 'kwargs':
                keywords.append(read_node(child.data).to_node(child.children))
            elif child.data == 'starargs':
                args.append(read_node(child.data).to_node(child.children))
                if len(child.children) > 1:
                    keywords.append(read_node(child.children[1].data).to_node(child.children[1].children))
            else:
                args.append(read_node(child.data).to_node(child.children))
        return args, keywords


class StarArg:
    @staticmethod
    def to_node(tree):
        value = read_node(tree[0].data).to_node(tree[0].children)
        return ast.Starred(value=value)


class KeywordArg:
    @staticmethod
    def to_node(tree):
        value = read_node(tree[0].data).to_node(tree[0].children)
        return ast.keyword(arg=None, value=value)


class ArgValue:
    @staticmethod
    def to_node(tree):
        arg, value = [read_node(child.data).to_node(child.children) for child in tree]
        return ast.keyword(arg=arg, value=value)


class ForStmt:
    @staticmethod
    def to_node(tree):
        target = read_node(tree[0].data).to_node(tree[0].children)
        iterrable = read_node(tree[1].data).to_node(tree[1].children)
        body = read_node(tree[2].data).to_node(tree[2].children)
        orelse = read_node(tree[3].data).to_node(tree[3].children) if len(tree) > 3 else []
        return ast.For(target=target, iter=iterrable, body=body, orelse=orelse)


def parse_ast_to_python(tree):
    ast_module = ast.Module()
    ast_module.body = []
    for child in tree.children:
        if child.data == 'funccall':
            ast_module.body.append(ast.Expr(value=read_node(child.data).to_node(child.children)))
        else:
            ast_module.body.append(read_node(child.data).to_node(child.children))
    return ast_module


def read_node(node):
    """
    index: Either 'data' or 'value'
    """
    mapping = {
        # Token
        'DEC_NUMBER': Decimal,
        'FLOAT_NUMBER': Float,
        'STRING': StringToken,
        'NAME': Name,
        # Token classes
        'number': Number,
        'var': Var,
        'string': String,
        # Atom classes
        'const_true': ConstTrue,
        'const_false': ConstFalse,
        'const_none': ConstNone,
        'set': Set,
        'set_comp': SetComp,
        'dict': Dict,
        'dict_comp': DictComp,
        'list': List,
        'tuple': Tuple,
        'tuplelist_comp': TupleListComp,
        # Expression classes
        'testlist_star_expr': TestlistStarExpr,
        'arith_expr': BinOp,
        'arith_plus': ArithPlus,
        'arith_minus': ArithMinus,
        'term': BinOp,
        'mult': Mult,
        'div': Div,
        'mod': Mod,
        'floor_div': FloorDiv,
        'power': Power,
        'and_test': And,
        'or_test': Or,
        'not': Not,
        'factor': Factor,
        'plus': UnaryAdd,
        'minus': UnarySub,
        'comparison': Comparison,
        'less_than': LessThan,
        'less_or_equal_to': LessOrEqualTo,
        'more_than': MoreThan,
        'more_or_equal_to': MoreOrEqualTo,
        'equal_to': EqualTo,
        'is_not_equal_to': IsNotEqualTo,
        'in': In,
        'not_in': NotIn,
        'is': Is,
        'is_not': IsNot,
        'exprlist': ListExpr,
        'getitem': GetItem,
        'subscript': Subscript,
        'lower_slice': LowerSlice,
        'upper_slice': UpperSlice,
        'slice': Slice,
        'sliceop': SliceOp,
        # Statement classes
        'assign': Assign,
        'augassign': AugAssign,
        '+=': ArithPlus,
        '-=': ArithMinus,
        '*=': Mult,
        '@=': MatMult,
        '/=': Div,
        '%=': Mod,
        '&=': BitAnd,
        '|=': BitOr,
        '^=': BitXor,
        '<<=': LeftShift,
        '>>=': RightShift,
        '**=': Pow,
        '//=': FloorDiv,
        'testlist': TestList,
        'compound_stmt': CompoundStmt,
        'if_stmt': IfStmt,
        'suite': Suite,
        'elseif': IfStmt,
        'while_stmt': WhileStmt,
        'funcdef': FuncDef,
        'parameters': Parameter,
        'paramvalue': ParamValue,
        'starparams': StarParam,
        'kwparams': KwParam,
        'pass_stmt': PassStmt,
        'continue_stmt': ContinueStmt,
        'break_stmt': BreakStmt,
        'return_stmt': ReturnStmt,
        'testlist_tuple': TestlistTuple,
        'funccall': FuncCall,
        'getattr': GetAttribute,
        'arguments': Argument,
        'starargs': StarArg,
        'kwargs': KeywordArg,
        'argvalue': ArgValue,
        'for_stmt': ForStmt,
    }
    return mapping[node]
