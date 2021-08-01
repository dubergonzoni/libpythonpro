import pytest
from libpythonpro.spam.db import Conexion


@pytest.fixture(scope='session')
def conexion():
    # Setup
    conexion_obj = Conexion()
    yield conexion_obj  # Return values to be inject in the tests
    # Tear Down
    conexion_obj.close()


@pytest.fixture
def session(conexion):
    session_obj = conexion.generate_session()
    yield session_obj
    session_obj.roll_back()
    session_obj.close()
