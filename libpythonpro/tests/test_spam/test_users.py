from libpythonpro.spam.models import User


def test_save_user(session):
    user = User(name='Eduardo')
    session.save(user)
    assert isinstance(user.id, int)


def test_list_users(session):
    users = [User(name='Eduardo'), User(name='Jason')]
    for user in users:
        session.save(user)
    assert users == session.list()
