from assertions import assert_, assert_truth
from assertions.operators import Operators
from main.base_test import BaseTest
from main.utils.random.randomizer import Randomizer
from main.utils.data.JSON_loader import JSONLoader

class TestDB(BaseTest):
    @classmethod
    def test_DB(cls):
        response = cls.project_DB.get_first_project_name()
        assert_(response, JSONLoader.get_test_data().projectName, 'first project name equals expected', Operators.EQUAL)
        response = prev_response = cls.project_DB.get_first_author_data()
        assert_(len(response), 4, 'author data contains four fields', Operators.EQUAL)
        prev_response = cls.project_DB.get_all_projects()
        cls.project_DB.add_project(Randomizer.get_random_string(False, False, False, False, 5))
        response = cls.project_DB.get_all_projects()
        assert_truth(len(response) > len(prev_response), 'successfully added new project to the table')