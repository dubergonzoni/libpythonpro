from unittest.mock import Mock

import pytest

from libpythonpro.spam.email_sender import Sender
from libpythonpro.spam.main import SpamSender
from spam.models import User


@pytest.mark.parametrize(
    'users',
    [
        [
            User(name='Eduardo', email='dubergonzoni@usp.br'),
            User(name='Jason', email='dubergonzoni@usp.br')
        ],
        [
            User(name='Eduardo', email='dubergonzoni@usp.br')
        ]
    ]
)
def test_amount_spam(session, users):
    for user in users:
        session.save(user)
    sender = Mock()
    spam_sender = SpamSender(session, sender)
    spam_sender.send_emails(
        'dubergonzoni@usp.br',
        'Python Pro course',
        'Finally learning a lot and being prepared to Django'
    )
    assert len(users) == sender.send.call_count


def test_spam_parameters(session):
    user = User(name='Eduardo', email='dubergonzoni@usp.br')
    session.save(user)
    sender = Mock()
    spam_sender = SpamSender(session, sender)
    spam_sender.send_emails(
        'dubergonzoni@gmail.com.br',
        'Python Pro course',
        'Finally learning a lot and being prepared to Django'
    )
    sender.send.assert_called_once_with(
        'dubergonzoni@gmail.com.br',
        'dubergonzoni@usp.br',
        'Python Pro course',
        'Finally learning a lot and being prepared to Django'
    )