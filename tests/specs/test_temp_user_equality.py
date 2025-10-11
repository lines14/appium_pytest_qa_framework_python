import pytest
from http import HTTPStatus
from tests.API.auth_API import AuthAPI
from assertions.operators import Operators
from main.utils.data.data_utils import DataUtils
from main.utils.data.JSON_loader import JSONLoader
from assertions import assert_, assert_response_status, assert_json, assert_truth


class TestTempUserEquality:
    auth_API = AuthAPI()

    @pytest.mark.asyncio
    async def test_temp_user_equality(self):
        response = await self.auth_API.get_temp_user(353)

        # assert_response_status(response.status_code, HTTPStatus.OK)
        # assert_truth(DataUtils.is_JSON(response.json()), 'response is json')
        # assert_json(response.json(), JSONLoader.test_data.resourceToCompare)
        # assert_(len(response), 4, 'author data contains four fields', Operators.EQUAL)