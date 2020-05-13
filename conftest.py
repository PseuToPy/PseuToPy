import pytest

from pseutopy.pseutopy import PseuToPy


@pytest.fixture(scope="session")
def pseutopy():
    return PseuToPy()
