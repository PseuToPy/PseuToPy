from tests.utils import check_ast


class TestAugAssignment:
    def test_AugAssigment_operators(self, pseutopy):
        pseudo_str = """
a += 1
a -= 1
a *= 1
a @= 1
a /= 1
a %= 1
a &= 1
a |= 1
a ^= 1
a <<= 1
a >>= 1
a **= 1
a //= 1
        """
        python_str = """
a += 1
a -= 1
a *= 1
a @= 1
a /= 1
a %= 1
a &= 1
a |= 1
a ^= 1
a <<= 1
a >>= 1
a **= 1
a //= 1
        """
        assert check_ast(pseutopy, python_str, pseudo_str)

    def test_AugAssigment_list(self, pseutopy):
        pseudo_str = """
li += [1, 2, 3]
li += [1,]
li += [a, b, c]
li += [a,]
li += [1, a]
li += []
        """
        python_str = """
li += [1, 2, 3]
li += [1,]
li += [a, b, c]
li += [a,]
li += [1, a]
li += []
        """
        assert check_ast(pseutopy, python_str, pseudo_str)

    def test_AugAssigment_tuple(self, pseutopy):
        pseudo_str = """
li += 1, 2, 3
li += (1, 2, 3)
li += (1,)
li += ()
        """
        python_str = """
li += 1, 2, 3
li += (1, 2, 3)
li += (1,)
li += ()
        """
        assert check_ast(pseutopy, python_str, pseudo_str)

    def test_AugAssigment_set(self, pseutopy):
        pseudo_str = """
se &= {1, 2}
se |= {a, b}
se ^= {1, a}
se -= {}
        """
        python_str = """
se &= {1, 2}
se |= {a, b}
se ^= {1, a}
se -= {}
        """
        assert check_ast(pseutopy, python_str, pseudo_str)

    def test_AugAssigment_str(self, pseutopy):
        pseudo_str = """
st += "world"
st += ""
st += 'world'
st += ''
        """
        python_str = """
st += "world"
st += ""
st += 'world'
st += ''
        """
        assert check_ast(pseutopy, python_str, pseudo_str)

    def test_AugAssigment_expression(self, pseutopy):
        pseudo_str = """
a //= 1 + 3
b /= 2 - a
a *= b + 3**c <= d - 7
        """
        python_str = """
a //= 1 + 3
b /= 2 - a
a *= b + 3**c <= d - 7
        """
        assert check_ast(pseutopy, python_str, pseudo_str)
