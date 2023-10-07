import pytest
from api.base_api_client import BaseAPIClient


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="http://10.0.2.15:8081")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def api_token(base_url):
    api_client = BaseAPIClient(base_url=base_url)
    token = api_client.get_token()

    return token
