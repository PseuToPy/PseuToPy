import ast


class BinaryOp(object):
    def __init__(self, parent, left, operator, right):
        self.parent = parent
        self.left = left
        self.operator = operator
        self.right = right

    def to_node(self):
        pass


class OrTest(BinaryOp):
    def to_node(self):
        if len(self.right) == 0:
            return self.left.to_node()
        else:
            nodes = [self.left.to_node()]
            for node in self.right:
                nodes.append(node.to_node())
            return ast.BoolOp(op=ast.Or(), values=nodes)


class AndTest(BinaryOp):
    def to_node(self):
        if len(self.right) == 0:
            return self.left.to_node()
        else:
            nodes = [self.left.to_node()]
            for node in self.right:
                nodes.append(node.to_node())
            return ast.BoolOp(ast.And(), nodes)


class Comparison(BinaryOp):
    def to_node(self):
        if len(self.operator) == 0:
            return self.left.to_node()
        else:
            right_nodes = []
            comp_operator = []
            for i in range(len(self.right)):
                right_nodes.append(self.right[i].to_node())
                if self.operator[i] in ['<', 'is lower than']:
                    comp_operator.append(ast.Lt())
                elif self.operator[i] in ['<=', 'is lower or equal to']:
                    comp_operator.append(ast.LtE())
                elif self.operator[i] in ['>', 'is greater than']:
                    comp_operator.append(ast.Gt())
                elif self.operator[i] in ['>=', 'is greater or equal to']:
                    comp_operator.append(ast.GtE())
                elif self.operator[i] in ['==', 'is equal to']:
                    comp_operator.append(ast.Eq())
                elif self.operator[i] in ['!=', 'is different from',
                                          'is not equal to']:
                    comp_operator.append(ast.NotEq())
                elif self.operator[i] == 'in':
                    comp_operator.append(ast.In())
                elif self.operator[i] == 'not in':
                    comp_operator.append(ast.NotIn())
                elif self.operator[i] == 'is':
                    comp_operator.append(ast.Is())
                elif self.operator[i] == 'is not':
                    comp_operator.append(ast.IsNot())
                else:
                    raise Exception("Unrecognized argument in Comparison")
            return ast.Compare(left=self.left.to_node(), ops=comp_operator,
                               comparators=right_nodes)


class Expr(BinaryOp):
    def to_node(self):
        node = self.left.to_node()
        if len(self.operator) == 0:
            return node
        else:
            for right_node in self.right:
                node = ast.BinOp(node, ast.BitOr(), right_node.to_node())
            return node


class XorExpr(BinaryOp):
    def to_node(self):
        node = self.left.to_node()
        if len(self.operator) == 0:
            return node
        else:
            for right_node in self.right:
                node = ast.BinOp(node, ast.BitXor(), right_node.to_node())
            return node


class AndExpr(BinaryOp):
    def to_node(self):
        node = self.left.to_node()
        if len(self.operator) == 0:
            return node
        else:
            for right_node in self.right:
                node = ast.BinOp(node, ast.BitAnd(), right_node.to_node())
            return node


class ShiftExpr(BinaryOp):
    def to_node(self):
        node = self.left.to_node()
        if len(self.operator) == 0:
            return node
        else:
            for right_node in self.right:
                if self.operator[0] == '<<':
                    node = ast.BinOp(node, ast.LShift(), right_node.to_node())
                else:
                    node = ast.BinOp(node, ast.RShift(), right_node.to_node())
            return node


class ArithExpr(BinaryOp):
    def to_node(self):
        """
        Creates a node that represent arithmetic operations (+ and -).
        This node can be inserted into the AST being constructed.
        :return: The node to be inserted into the AST
        """
        node = self.left.to_node()
        if len(self.operator) == 0:
            return node
        else:
            # Because there can be chained operations, the trick is to
            # recursively build the node by creating it as follow:
            # node = ast.BinOp(node, ast.Op(), right) <-- note that node
            # inside ast.BinOp() is reused when creating the final node
            for i in range(len(self.right)):
                if self.operator[i] in ['+', 'plus']:
                    node = ast.BinOp(node, ast.Add(), self.right[i].to_node())
                elif self.operator[i] in ['-', 'minus']:
                    node = ast.BinOp(node, ast.Sub(), self.right[i].to_node())
            return node


class Term(BinaryOp):
    def to_node(self):
        node = self.left.to_node()
        if len(self.operator) == 0:
            return node
        else:
            for i in range(len(self.right)):
                if self.operator[i] in ['*', 'times']:
                    node = ast.BinOp(node, ast.Mult(), self.right[i].to_node())
                elif self.operator[i] in ['/', 'divided by']:
                    node = ast.BinOp(node, ast.Div(), self.right[i].to_node())
                elif self.operator[i] in ['%', 'modulo']:
                    node = ast.BinOp(node, ast.Mod(), self.right[i].to_node())
                elif self.operator[i] == '@':
                    node = ast.BinOp(node, ast.MatMult(),
                                     self.right[i].to_node())
                elif self.operator[i] == '//':
                    node = ast.BinOp(node, ast.FloorDiv(),
                                     self.right[i].to_node())
            return node


class Power(BinaryOp):
    def to_node(self):
        if len(self.operator) == 0:
            return self.left.to_node()
        else:
            return ast.BinOp(self.left.to_node(), ast.Pow(),
                             self.right.to_node())


# -----------------------------------------------------------------------------
# Generators for Unary operators
# -----------------------------------------------------------------------------
class UnaryOp(object):
    def __init__(self, parent, operator, value):
        self.parent = parent
        self.operator = operator
        self.value = value

    def to_node(self):
        pass


class Factor(UnaryOp):
    def to_node(self):
        value = self.value
        operator = self.operator
        if operator in ('+', 'plus'):
            return ast.UnaryOp(ast.UAdd(), value.to_node())
        elif operator in ('-', 'minus'):
            return ast.UnaryOp(ast.USub(), value.to_node())
        elif operator == '~':
            return ast.UnaryOp(ast.Invert(), value.to_node())
        else:
            return value.to_node()


class NotTest(UnaryOp):
    def to_node(self):
        value = self.value
        operator = self.operator
        if operator == 'not':
            return ast.UnaryOp(ast.Not(), value.to_node())
        else:
            return value.to_node()


# -----------------------------------------------------------------------------
# Functions and data structures
# -----------------------------------------------------------------------------
class TestListStarExpr(object):
    def __init__(self, parent, values):
        self.parent = parent
        self.values = values

    def to_node(self):
        """
        This method will be called when both evaluating names or values.
        """
        # If single identifier: list of size 1
        # If multiple identifiers: list of size n
        if len(self.values) > 1:
            elements = []
            for element in self.values:
                elements.append(element.to_node())
            return ast.Tuple(elts=elements, ctx=ast.Load)
        else:
            return self.values[0].to_node()


class TestList(object):
    def __init__(self, parent, range_params, args):
        self.parent = parent
        self.range_params = range_params
        self.args = args

    def to_node(self):
        if self.range_params is not None:
            range_params = []
            for param in self.range_params.args:
                range_params.append(param.to_node())
            node = ast.Call(func=ast.Name(id='range', ctx='Load'),
                            args=range_params, keywords=[])
            return node
        else:
            if len(self.args) == 1:
                return self.args[0].to_node()
            else:
                node = []
                for arg in self.args:
                    node.append(arg.to_node())
                return node


class AtomExpr(object):
    def __init__(self, parent, atom, trailer):
        self.parent = parent
        self.atom = atom
        self.trailer = trailer

    def to_node(self):
        atom = self.atom
        # We are not dealing with Trailers yet, so we comment out the next line
        # trailer = self.trailer
        return atom.to_node()


class Atom(object):
    def __init__(self, parent, is_tuple, is_list, is_dict, values, name,
                 number, string, none, boolean):
        self.parent = parent
        self.is_tuple = is_tuple
        self.is_list = is_list
        self.is_dict = is_dict
        self.values = values
        self.name = name
        self.number = number
        self.string = string
        self.none = none
        self.boolean = boolean

    def to_node(self):
        if self.is_tuple != '':
            elements = self.__create_elements()
            return ast.Tuple(elts=elements, ctx=ast.Load)
        elif self.is_list != '':
            elements = self.__create_elements()
            return ast.List(elts=elements, ctx=ast.Load)
        elif self.is_dict != '':
            if self.values is None:
                return ast.Dict(keys=[], values=[])
            elif self.__is_dict():
                keys, values = self.__create_keys_values()
                return ast.Dict(keys=keys, values=values)
            else:
                elements = self.__create_elements()
                return ast.Set(elts=elements, ctx=ast.Load)
        elif self.name is not None:
            return self.name.to_node()
        elif self.number is not None:
            return self.number.to_node()
        elif self.none is not None:
            return self.none.to_node()
        elif self.boolean is not None:
            return self.boolean.to_node()
        elif self.string is not None:
            return self.string[0].to_node()

    def __create_elements(self):
        elements = []
        if self.values is None:
            return elements
        else:
            values = self.values.values
            for element in values:
                elements.append(element.to_node())
            return elements

    def __is_dict(self):
        return len(self.values.keys) > 0

    def __create_keys_values(self):
        keys = []
        values = []
        for key in self.values.keys:
            keys.append(key.to_node())
        for value in self.values.values:
            values.append(value.to_node())
        return keys, values


class TestListComp(object):
    def __init__(self, parent, values):
        self.parent = parent
        self.values = values

    def to_node(self):
        if len(self.values) > 1:
            elements = []
            for element in self.values:
                elements.append(element.to_node())
            return ast.Tuple(elts=elements, ctx=ast.Load)
        else:
            return self.values.to_node()


class Parameters(object):
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value

    def to_node(self):
        if self.value is not None:
            return self.value.to_node()
        return ast.arguments(args=[], defaults=[], kw_defaults=[], kwarg=None,
                             kwonlyargs=[], vararg=None)


class TypedArgsList(object):
    def __init__(self, parent, type_def, value):
        self.parent = parent
        self.type_def = type_def
        self.value = value

    def to_node(self):
        args = []
        for arg in self.type_def:
            args.append(ast.arg(arg=arg.name.to_node().id, annotation=None))
        defaults = []
        for default in self.value:
            defaults.append(default.to_node())
        return ast.arguments(args=args, defaults=defaults, vararg=None,
                             kwarg=None, kw_default=[], kwonlyargs=[])
