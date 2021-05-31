"""
Tests on augassign rule
Note that some of these rules do not have any PseuToPy equivalent yet.
"""


def test_aug_assign(pseutopy):
    python_code = ["a += 1", "a -= 1", "a *= 1", "a @= 1", "a /= 1", "a %= 1", "a &= 1", "a |= 1", "a &= 1", "a <<= 1",
                   "a >>= 1", "a **= 1", "a //= 1"]
    pseutopy_code = ["a += 1", "a -= 1", "a *= 1", "a @= 1", "a /= 1", "a %= 1", "a &= 1", "a |= 1", "a &= 1",
                     "a <<= 1", "a >>= 1", "a **= 1", "a //= 1"]
    for python, pseudocode in zip(python_code, pseutopy_code):
        assert pseutopy.convert_from_string(pseudocode) == python + "\n"