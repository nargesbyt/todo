import sqlite3


class Singleton(type):
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super(Singleton, self).__call__(*args, **kwargs)
        return self._instance


class Database(metaclass=Singleton):
    def __init__(self, db_name):
        print("CALLED .....")
        self.db_name = db_name
        self.con = sqlite3.connect(self.db_name)


    def insert(self, table_name: str, fields):
        keys = []
        values = []

        for key, value in fields.items():
            keys.append(key)
            values.append(value)

        markers = ",".join("?" * len(fields))
        columns = ",".join(keys)

        sql = "INSERT INTO {0} ({1}) VALUES ({2});"

        cur = self.con.cursor()
        cur.execute(sql.format(table_name, columns, markers), values)
        self.con.commit()

    def update(self, table_name: str, fields, condition):
        # sql = "UPDATE table_name SET col1 = ? , col2 = ?   WHERE  condition;"

        set_values = []
        for k, v in fields.items():
            set_values.append(k + " = ?")

        str_condition = []
        for k, v in condition.items():
            str_condition.append(k + v)

        sql = "UPDATE {0} SET {1} WHERE {2};"

        cur = self.con.cursor()
        cur.execute(sql.format(table_name, " , ".join(set_values), '\n AND '.join(str_condition)),
                    list(fields.values()))
        self.con.commit()

    def delete(self, table_name: str, field):  # field is a dict
        sql = "DELETE FROM {0} WHERE {1}= ?"

        field_items = field.items()
        col = field_items[0]
        val = field_items[1]

        cur = self.con.cursor()
        cur.execute(sql.format(table_name, col), (val,))
        self.con.commit()

    def find(self, table_name, fields, condition):  # fields is a list of columns , condition is a dict
        columns = ", ".join(fields)

        str_condition = []
        for k, v in condition.items():
            str_condition.append(k + " ?")

        sql = "SELECT {0} FROM {1} WHERE {2}"

        cur = self.con.cursor()
        # print(sql.format(columns, table_name, '\n AND '.join(str_condition)))
        result = cur.execute(sql.format(columns, table_name, '\n AND '.join(str_condition)), list(condition.values()))

        return result
