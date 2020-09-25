import pytest

from src.pseutopy.pseutopy import PseuToPy

@pytest.fixture(scope="session")
def enPseutopy():
    return PseuToPy("en")

@pytest.fixture(scope="session")
def frPseutopy():
    return PseuToPy("fr")
