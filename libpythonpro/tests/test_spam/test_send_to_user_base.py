from libpythonpro.spam.email_sender import Sender
from libpythonpro.spam.main import SpamSender


def test_spam_send(session):
    spam_sender =  SpamSender(session, Sender())
    spam_sender.send_emails(
        'dubergonzoni@usp.br',
        'Python Pro course',
        'Finally learning a lot and being prepared to Django'
    )