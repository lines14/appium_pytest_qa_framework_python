import pytest
from http import HTTPStatus
from tests.API.auth_API import AuthAPI
from assertions.operators import Operators
from main.utils.data.data_utils import DataUtils
from main.utils.data.JSON_loader import JSONLoader
from assertions import assert_, assert_response_status, assert_json, assert_truth


class TestTempUserEquality:
    @pytest.mark.asyncio
    async def test_temp_user_equality(self):
        response = await AuthAPI().get_temp_user(JSONLoader.test_data.temp_user_ID)
        print(response.json())

        # assert_response_status(response.status_code, HTTPStatus.OK)
        # assert_truth(DataUtils.is_JSON(response.json()), 'response is json')
        # assert_json(response.json(), JSONLoader.test_data.resourceToCompare)
        # assert_(len(response), 4, 'author data contains four fields', Operators.EQUAL)