from src.pseutopy.pseutopy import PseuToPy


def test_name():
    pseutopy = PseuToPy()
    python_code = 'my_var'
    pseutopy_code = 'my_var'
    assert pseutopy.convert_from_string(python_code) == pseutopy.convert_from_string(pseutopy_code)


def test_integer():
    pseutopy = PseuToPy()
    python_code = '1'
    pseutopy_code = '1'
    assert pseutopy.convert_from_string(python_code) == pseutopy.convert_from_string(pseutopy_code)


def test_float():
    pseutopy = PseuToPy()
    python_code = '1.2'
    pseutopy_code = '1.2'
    assert pseutopy.convert_from_string(python_code) == pseutopy.convert_from_string(pseutopy_code)


def test_string():
    pseutopy = PseuToPy()
    python_code = '"A string"'
    pseutopy_code = '"A string"'
    assert pseutopy.convert_from_string(python_code) == pseutopy.convert_from_string(pseutopy_code)


def test_const_none():
    pseutopy = PseuToPy()
    python_code = 'None'
    pseutopy_code = 'none'
    assert pseutopy.convert_from_string(python_code) == pseutopy.convert_from_string(pseutopy_code)


def test_const_true():
    pseutopy = PseuToPy()
    python_code = 'True'
    pseutopy_code = 'true'
    assert pseutopy.convert_from_string(python_code) == pseutopy.convert_from_string(pseutopy_code)


def test_const_false():
    pseutopy = PseuToPy()
    python_code = 'False'
    pseutopy_code = 'false'
    assert pseutopy.convert_from_string(python_code) == pseutopy.convert_from_string(pseutopy_code)


def test_tuple():
    # TODO: Modify the atom rule to provide a PseuToPy variant for tuples
    pass


def test_list():
    # TODO: Modify the atom rule to provide a PseuToPy variant for lists
    pass


def test_set():
    # TODO: Modify the atom rule to provide a PseuToPy variant for sets
    pass


def test_dict():
    # TODO: Modify the atom rule to provide a PseuToPy variant for dictionaries
    pass


def test_test():
    """There is no need to test this rule, as it depends on the `test` rule that we will
    test later. As a reminder, the `test` rule is used for all types of operations."""
    pass
