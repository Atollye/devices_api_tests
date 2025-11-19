
from http import HTTPStatus
from dotenv import load_dotenv

import pytest

from api.api_client import ApiClient
from api.objects_api import post_object, delete_object
from assertions.assertion_base import assert_status_code
from utilities.files_utils import read_json_common_request_data


@pytest.fixture(scope='class')
def client():
    return ApiClient()

@pytest.fixture(scope='class')
def create_data(client):
    test_obj = read_json_common_request_data("valid_post_object")
    response = post_object(client, json=test_obj)
    assert_status_code(response, HTTPStatus.OK)
    yield response.json()
    delete_object(client, response.json()['id'])