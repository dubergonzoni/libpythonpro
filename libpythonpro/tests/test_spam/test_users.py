from libpythonpro.spam.models import User


def test_save_user(session):
    user = User(name='Eduardo', email='dubergonzoni@usp.br')
    session.save(user)
    assert isinstance(user.id, int)


def test_list_users(session):
    users = [User(name='Eduardo', email='dubergonzoni@usp.br'),
             User(name='Jason', email='dubergonzoni@usp.br')]
    for user in users:
        session.save(user)
    assert users == session.list()
