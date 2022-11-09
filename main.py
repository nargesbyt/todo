import json
import sqlite3
from datetime import datetime

from animal import Animal, Tiger
from todo_class import Task
from database_class import Database

STATUS_PENDING = "pending"
STATUS_IN_PROGRESS = "in_progress"
STATUS_FINISHED = "finished"

STATUS = {STATUS_PENDING: 0, STATUS_IN_PROGRESS: 1, STATUS_FINISHED: 2}


def main():
    """'main' documentation."""

    #
    # cur.execute("""
    # CREATE TABLE IF NOT EXISTS tasks(
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     title TEXT NOT NULL,
    #     status CAHR(10) CHECK(status IN ('pending', 'in_progress', 'finished')) NOT NULL DEFAULT 'pending',
    #     created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    #     finished_at timestamp
    # );
    # """)
    # cur.execute('ALTER TABLE tasks ADD COLUMN id PRIMARY KEY')
    # conn.commit()

    # cur.execute("""
    # INSERT INTO tasks(title) VALUES
    #     ('Test Title 1'),
    #     ('Test Title 2')
    # """)
    # conn.commit()

    # res = cur.execute('SELECT name from sqlite_master where type="table"')
    # db1 = Database('todo.db')
    # db2 = Database('todo.db')
    t2 = Task("todo.db")
    t = Task("todo.db")
    print(t.find_one_by_id(2))
    t.update(2, "The new title 2", "finished")
    print(t.find_one_by_id(2))
    # d = Database('todo.db')
    # d.update('tasks', {"title":"new task"} , {"title": " LIKE '%ft%'" , "status":"='pending'"})
     #d = Database('todo.db')
    # d.delete("tasks", {"id": 6})
    # d = Database('todo.db')
    # d.find("tasks", ['id', 'title', 'status'], {"title": " like '%e%'", "id": " >2"})


def invert(file, area):
    with open(file) as f:
        list = json.load(f)

    for dic in list:
        if dic["area"] == area:
            print(dic["country"])


status = ["pending", "in_progress", "finished"]


def add(task_title):
    with open("todo.json") as todo_file:
        todo_list = json.load(todo_file)
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    task = {"title": task_title, "status": STATUS[STATUS_PENDING], "create_date": ts, "finish_date": None}
    todo_list.append(task)
    with open("todo.json", 'w') as todo_file:
        json.dump(todo_list, todo_file, indent=2)
    print(todo_list)
    # for dic in todo_list:
    # print(datetime.fromtimestamp(dic["create_date"], tz= None) , end= '  ')


def filter(status):
    flag = 0
    with open("todo.json") as todo_file:
        todo_list = json.load(todo_file)
    for dic in todo_list:
        if dic["status"] == status:
            print(dic)
            flag = 1
    if flag == 0:
        print(f"There is no {status} task")


def update(title, status):
    with open("todo.json") as todo_file:
        todo_list = json.load(todo_file)
    for dic in todo_list:
        if dic["title"] == title:
            dic["status"] = status
            if status == "finished":
                dt = datetime.now()
                ts = datetime.timestamp(dt)
                dic["finish_date"] = ts
            print(dic)
    with open("todo.json", 'w') as todo_file:
        json.dump(todo_list, todo_file, indent=2)


def remove_task():
    with open("todo.json") as todo_file:
        todo_list = json.load(todo_file)
    for dic in todo_list:
        if dic["status"] == "finished":
            todo_list.remove(dic)
    print(todo_list)
    with open("todo.json", 'w') as todo_file:
        json.dump(todo_list, todo_file, indent=2)


# Dunder
if __name__ == "__main__":
    main()
