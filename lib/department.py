from __init__ import CURSOR, CONN

class Department:

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"

    def save(self):
        """ Save the department instance to the database """
        if self.id is None:
            sql = """
                INSERT INTO departments (name, location) VALUES (?, ?)
            """
            CURSOR.execute(sql, (self.name, self.location))
            CONN.commit()
            self.id = CURSOR.lastrowid
        else:
            sql = """
                UPDATE departments SET name=?, location=? WHERE id=?
            """
            CURSOR.execute(sql, (self.name, self.location, self.id))
            CONN.commit()

    @classmethod
    def create(cls, name, location):
        """ Create a new Department instance and save it to the database """
        department = cls(name, location)
        department.save()
        return department

    def update(self):
        """ Update the corresponding row in the database with the instance's new attribute values """
        self.save()

    def delete(self):
        """ Delete the instance's corresponding row in the database """
        if self.id is not None:
            sql = """
                DELETE FROM departments WHERE id=?
            """
            CURSOR.execute(sql, (self.id,))
            CONN.commit()
            self.id = None

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Department instances """
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Department instances """
        sql = """
            DROP TABLE IF EXISTS departments;
        """
        CURSOR.execute(sql)
        CONN.commit()
