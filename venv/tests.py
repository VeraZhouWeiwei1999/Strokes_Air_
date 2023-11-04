from fastapi.testclient import TestClient

from try_api import app
from functions_for_api import get_db_session


testing_db = ["DB for testing"]


def get_testing_db():
    return testing_db


app.dependency_overrides[get_db_session] = get_testing_db
client = TestClient(app)


def test_item_should_add_to_database():
    response = client.get(
        "/add-item/?item=sugar",
    )
    assert response.status_code == 200
    assert response.text == '{"message":"added item sugar"}'



# # using data loaded in fixture, write tests
# def check_all_needed_dates_present():
#     #Given
#     # data from fixture
#     #When
#     # transform data with explore_data_function
#     #Then
#     assert

