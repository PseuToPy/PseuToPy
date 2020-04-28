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
        if self.chained_value is not None:
            return self.__create_chained_assignment_node()

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
        targets = []
        if len(self.name.values) == 1:
            targets.append(ast.Name(id=self.name.to_node(), ctx=ast.Store))
        else:
            elements = []
            for element in self.name.values:
                elements.append(ast.Name(id=element.to_node(), ctx=ast.Store))
            targets.append(ast.Tuple(elts=elements, ctx=ast.Load))
        for i in range(len(chained_value)):
            if i == len(chained_value) - 1:
                value = chained_value[i].to_node()
            else:
                targets.append(chained_value[i].to_node())
        return ast.Assign(targets=targets, value=value)
