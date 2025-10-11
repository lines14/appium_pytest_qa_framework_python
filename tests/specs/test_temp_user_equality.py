import json
import pytest
from http import HTTPStatus
from tests.DB.auth_DB import AuthDB
from tests.API.auth_API import AuthAPI
from assertions.operators import Operators
from main.utils.data.data_utils import DataUtils
from main.utils.data.JSON_loader import JSONLoader
from assertions import assert_, assert_response_status, assert_truth


class TestTempUserEquality:
    @pytest.mark.asyncio
    async def test_temp_user_equality(self):
        response = await AuthAPI().get_temp_user(JSONLoader.test_data.temp_user_ID)
        assert_response_status(response.status_code, HTTPStatus.OK)
        assert_truth(DataUtils.is_JSON(response.json()), 'response is JSON')

        temp_user = await AuthDB().get_temp_user(JSONLoader.test_data.temp_user_ID)
        DataUtils.assert_json(response.json(), json.loads(temp_user), excluded_fields=["password"])
        assert_(
            DataUtils.dict_to_model(response.json()).iin, 
            DataUtils.dict_to_model(json.loads(temp_user)).iin, 
            'temp user IIN equals', 
            Operators.EQUAL
        )