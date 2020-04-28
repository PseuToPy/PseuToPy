import ast


class Statement(object):
    def __init__(self, parent):
        self.parent = parent

    def to_node(self):
        pass


class ExprStmt(Statement):
    def __init__(self, parent, name, chained_value, value):
        super().__init__(parent)
        self.name = name
        self.chained_value = chained_value
        self.value = value

    def to_node(self):
        # TODO: Finish the implementation here to manage assignments with
        #  functions
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
        return ast.Call(func=ast.Name(id='input', ctx=ast.Load), args=args,
                        keywords=[])


class FuncCallStmt(Statement):
    def __init__(self, parent, name, args):
        super().__init__(parent)
        self.name = name
        self.args = args

    def to_node(self):
        args = []
        for arg in self.args:
            args.append(arg.to_node())
        return ast.Call(func=ast.Name(id=self.name.to_node(), ctx=ast.Load),
                        args=args, keywords=[])
