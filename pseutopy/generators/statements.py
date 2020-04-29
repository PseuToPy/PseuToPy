import ast


class Statement(object):
    def __init__(self, parent):
        self.parent = parent

    def to_node(self):
        pass


# -----------------------------------------------------------------------------
# Generators for simple statements
# -----------------------------------------------------------------------------
class ExprStmt(Statement):
    def __init__(self, parent, name, chained_value, value):
        super().__init__(parent)
        self.name = name
        self.chained_value = chained_value
        self.value = value

    def to_node(self):
        if len(self.chained_value) > 0:
            return self.__create_chained_assignment_node()
        if self.value is not None:
            return self.__create_function_assignment_node()

    def __create_chained_assignment_node(self):
        """
        When creating a chained assignment, it is either:
            - A true chained assignment (e.g., a = b = True)
            - A single assignment (e.g., a = True)
        This method takes care of both these cases
        :return: The node representing a chained assignment
        """
        chained_value = self.chained_value
        value = None
        targets = self.__create_targets()
        for i in range(len(chained_value)):
            if i == len(chained_value) - 1:
                value = chained_value[i].to_node()
            else:
                targets.append(chained_value[i].to_node())
        return ast.Assign(targets=targets, value=value)

    def __create_function_assignment_node(self):
        targets = self.__create_targets()
        return ast.Assign(targets=targets, value=self.value.to_node())

    def __create_targets(self):
        targets = []
        if len(self.name.values) == 1:
            targets.append(ast.Name(id=self.name.to_node(), ctx=ast.Store))
        else:
            elements = []
            for element in self.name.values:
                elements.append(ast.Name(id=element.to_node(), ctx=ast.Store))
            targets.append(ast.Tuple(elts=elements, ctx=ast.Load))
        return targets


class InputStmt(Statement):
    def __init__(self, parent, cast_type, args, values):
        super().__init__(parent)
        self.cast_type = cast_type
        self.args = args
        self.values = values

    def to_node(self):
        args = [self.args.to_node()]
        for value in self.values:
            args.append(value.to_node())
        return ast.Expr(value=ast.Call(func=ast.Name(id='input', ctx=ast.Load),
                                       args=args, keywords=[]))


class PrintStmt(Statement):
    def __init__(self, parent, args):
        super().__init__(parent)
        self.args = args

    def to_node(self):
        args = []
        for arg in self.args:
            args.append(arg.to_node())
        return ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load),
                                       args=args, keywords=[]))


class FuncCallStmt(Statement):
    def __init__(self, parent, name, args):
        super().__init__(parent)
        self.name = name
        self.args = args

    def to_node(self):
        args = []
        for arg in self.args:
            args.append(arg.to_node())
        return ast.Expr(value=ast.Call(func=ast.Name(id=self.name.to_node(),
                                                     ctx=ast.Load),
                                       args=args, keywords=[]))


class DeclareStmt(Statement):
    def __init__(self, parent, name):
        super().__init__(parent)
        self.name = name

    def to_node(self):
        return ast.Assign(targets=[self.name.to_node()],
                          value=ast.NameConstant(value="None"))


class DelStmt(Statement):
    def __init__(self, parent, name):
        super().__init__(parent)
        self.name = name

    def to_node(self):
        targets = []
        for name in self.name.value:
            targets.append(name.to_node())
        return ast.Delete(targets=targets)


# -----------------------------------------------------------------------------
# Generators for Compound Statements
# -----------------------------------------------------------------------------
class IfStmt(Statement):
    def __init__(self, parent, condition, body):
        super().__init__(parent)
        self.condition = condition
        self.body = body

    def to_node(self):
        # Because __recursive_orelse function returns a List of size 1,
        # we need to retrieve the first element of the returned result
        return self.__recursive_orelse()[0]

    def __recursive_orelse(self):
        """
        This recursive function creates a AST node for any IfStmt. To make
        the recursion work, we must return the final AST node inside a List.
        This is why we also retrieve the element at index 0 in the to_node()
        function.
        :return: A List of size 1 which contains the whole If statement
        """
        statements = self.body[0].statement
        body = []
        for statement in statements:
            body.append(statement.to_node())
        # This is a case of a single If statement
        if len(self.condition) == 1 and len(self.body) == 1:
            return [ast.If(test=self.condition[0].to_node(), body=body,
                           orelse=[])]
        # This is the case of a 'Else' statement
        elif len(self.condition) == 0 and len(self.body) == 1:
            return body
        # This is a case of a If statement followed by any other statement
        else:
            self.body.pop(0)
            return [ast.If(test=self.condition.pop(0).to_node(), body=body,
                           orelse=self.__recursive_orelse())]


# class WhileStmt(Statement):
#     def __init__(self, parent, condition, body, else_body):
#         super().__init__(parent)
#         self.condition = condition
#         self.body = body
#         self.else_body = else_body
#
#     def to_node(self):
#         test = self.condition.to_node()
#         body = []
#         for statement in self.body.statement:
#             body.append(statement.to_node())
#         orelse = []
#         for statement in self.else_body.statement:
#             orelse.append(statement.to_node())
#         return ast.While(test=test, body=body, orelse=orelse)