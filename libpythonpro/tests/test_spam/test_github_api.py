from unittest.mock import Mock

import pytest

from libpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/50045444?v=4'
    resp_mock.json.return_value = {
        'login': 'dubergonzoni', 'id': 50045444,
        'avatar_url': url,
    }
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value=resp_mock
    return url


def test_find_avatar(avatar_url):
    url = github_api.find_avatar('dubergonzoni')
    assert avatar_url == url


def test_find_avatar_integration():
    url = github_api.find_avatar('dubergonzoni')
    assert 'https://avatars.githubusercontent.com/u/50045444?v=4' == url