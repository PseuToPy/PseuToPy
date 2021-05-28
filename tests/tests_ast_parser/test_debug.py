"""
    Debug purpose only
"""

def test_debug(pseutopy):
    assert pseutopy.convert_from_string('primes = {1, 3, b, 7, "11"}') == 'primes = {1, 3, b, 7, "11"}' + '\n'
