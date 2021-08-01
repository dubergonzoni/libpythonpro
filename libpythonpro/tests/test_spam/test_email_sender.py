from libpythonpro.spam.email_sender import Sender, InvalidEmail
from libpythonpro.tests.test_spam.conftest import pytest


def test_email_sender():
    sender = Sender()
    assert sender is not None


@pytest.mark.parametrize(
    'shipper',
    ['dubergonzoni@gmail.com', 'foo@bar.com.br']
)
def test_shipper(shipper):
    sender = Sender()
    result = sender.send(
        shipper,
        'dubergonzoni@usp.br',
        'Python Pro Course',
        'Learning about Python for backend applications.'
    )
    assert shipper in result


@pytest.mark.parametrize(
    'shipper',
    ['', 'dubergonzoni']
)
def test_shipper_invalid(shipper):
    sender = Sender()
    with pytest.raises(InvalidEmail):
        sender.send(
            shipper,
            'dubergonzoni@usp.br',
            'Python Pro Course',
            'Learning about Python for backend applications.'
        )

