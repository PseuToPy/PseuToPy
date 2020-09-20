import pytest

from pseutopy.pseutopy import PseuToPy as oldPseuToPy
from src.pseutopy.pseutopy import PseuToPy

@pytest.fixture(scope="session")
def pseutopy():
    return oldPseuToPy()

@pytest.fixture(scope="session")
def enPseutopy():
    return PseuToPy("en")

@pytest.fixture(scope="session")
def frPseutopy():
    return PseuToPy("fr")
