import pytest

from pseutopy.pseutopy import PseuToPy as oldPseuToPy
from src.pseutopy.pseutopy import PseuToPy

@pytest.fixture(scope="session")
def enPseutopy():
    return oldPseuToPy()

#@pytest.fixture(scope="session")
#def nPseutopy():
#    return PseuToPy("en")

@pytest.fixture(scope="session")
def frPseutopy():
    return PseuToPy("fr")
