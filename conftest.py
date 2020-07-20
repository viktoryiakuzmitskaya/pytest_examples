import pytest
from fixture.application import Application

#@pytest.fixture(scope = "session")
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
