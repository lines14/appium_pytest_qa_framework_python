import os
import dotenv
from main.utils.DB.base_DB import BaseDB
dotenv.load_dotenv(override=True)

class ProjectDB(BaseDB):
    def __init__(self):
        super().__init__(
            '' or os.environ.get('DB_HOST'),
            '' or os.environ.get('DB_USERNAME'),
            '' or os.environ.get('DB_PASSWORD'),
            '' or os.environ.get('DB_DATABASE'),
            '' or os.environ.get('DB_PORT')
        )

    def get_first_project_name(self):
        results = super().sql_select('project', 'name', 'ORDER BY `id` ASC LIMIT 1')
        return list(results.pop()).pop()
    
    def get_first_author_data(self):
        return (super().sql_select('author', conditions='ORDER BY `id` ASC LIMIT 1')).pop()
    
    def get_all_projects(self):
        return super().sql_select('project', 'name', 'ORDER BY `id`')
    
    def add_project(self, name):
        super().sql_insert('project', 'name', f'"{name}"')