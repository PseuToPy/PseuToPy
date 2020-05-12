import ast


class Number(object):
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value

    def to_node(self):
        return ast.Num(n=self.value)


class Name(object):
    def __init__(self, parent, id):
        self.parent = parent
        self.id = id

    def to_node(self):
        return ast.Name(id="" + self.id, ctx=ast.Store)


class String(object):
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value

    def to_node(self):
        return ast.Str(s=self.value)


class Boolean(object):
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value

    def to_node(self):
        return ast.NameConstant(value=self.value)


class NoneType(object):
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value

    def to_node(self):
        return ast.NameConstant(value=None)
