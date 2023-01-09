import pytest
import requests
# Particular test using fixture

# @pytest.fixture(scope='function') # 'function' = where fixture were call


@pytest.fixture(scope='module')  # 'module' = all file
def fixt():
    print('Started')
    yield {'initial': []}
    print('Test ended')


@pytest.fixture()  # 'module' = all file
def fixt_new():
    print('start test')
    yield
    print('finish test')


def test_one(fixt, fixt_new):
    response = requests.get("https://google.com")
    fixt["data"] = response.text
    assert response.status_code == 200


def test_second(fixt, fixt_new):
    print('Second')
    assert len(fixt["data"]) > 0