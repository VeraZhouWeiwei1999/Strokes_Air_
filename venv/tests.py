import pytest
import explore_air_data
from explore_air_data import get_data
#


# load data. define scope == session
@pytest.mark.skipif(condition?)
@pytest.fixture(scope="session")
def df_input():
    return print("test is running")

# # using data loaded in fixture, write tests
# def check_all_needed_dates_present():
#     #Given
#     # data from fixture
#     #When
#     # transform data with explore_data_function
#     #Then
#     assert

