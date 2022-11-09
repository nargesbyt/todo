from _datetime import datetime
from database_class import Database


class Task(Database):

    def __init__(self, database_name):
        Database.__init__(self, database_name)
        # self.title = title
        # self.status = "pending"
        # dt = datetime.now()
        # ts = datetime.timestamp(dt)
        # self.create_date = ts
        # self.finish_date = None

    def add(self, title):
        Database.insert(self, "tasks", {"title": title})

    def delete(self, id):
        Database.delete(self, "tasks", {"id": id})

    def update(self, id, title, status):
        Database.update(self, "tasks", {"title": title, "status": status}, {"id": f"= {id}"})

    # snake_case
    # camelCase
    # PascalCase
    # kebab-case
    def find_one_by_id(self, id):
        res = Database.find(self, "tasks", ["id", "title", "status"], {"id =": id})

        return res.fetchone()
