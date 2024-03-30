import pytest
from unittest.mock import patch  
from unittest.mock import MagicMock


from repositories.OperateurRepository import OperateurRepository 
from models.models import  Operateur 
@pytest.fixture
def mock_session(mocker):
    mock_session = mocker.patch('app.repositories.OperateurRepository.SessionLocal')
    return mock_session


def repository():
    return OperateurRepository()


@pytest.mark.usefixtures("mock_session")
def test_get_operateur_by_id(mock_session):
    # a sample Operateur object to be returned by the query
    mock_operateur = Operateur(idOperateur=1, nom="John", prenom="Doe", password="password")
    mock_session = MagicMock()
    mock_query = MagicMock()
    mock_session.query.return_value = mock_query
    mock_query.filter_by.return_value = mock_query
    mock_query.first.return_value = mock_operateur
    
    #  the repository with the mocked session
    repository = OperateurRepository(session=mock_session)
    # the method to be tested
    retrieved_operateur = repository.get_operateur_by_id(1)
    # Assert that the retrieved Operateur matches the expected one
    assert retrieved_operateur == mock_operateur


