import pytest

from pseutopy.pseutopy import PseuToPy
from src.pseutopy.pseutopy import PseuToPy as frPseuToPy

@pytest.fixture(scope="session")
def pseutopy():
    return PseuToPy()

@pytest.fixture(scope="session")
def enPseutopy():
    return frPseuToPy("en")

@pytest.fixture(scope="session")
def frPseutopy():
    return frPseuToPy("fr")
