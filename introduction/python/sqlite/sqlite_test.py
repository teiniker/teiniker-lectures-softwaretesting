import unittest
import sqlite3

class SQLiteTest(unittest.TestCase):

    DATABALE_NAME = 'testdb.db'

    # Shared test fixture (database schema and test data)
    @classmethod
    def setUpClass(cls):
        connection = sqlite3.connect(SQLiteTest.DATABALE_NAME)
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE user (id INTEGER, username TEXT, password TEXT, PRIMARY KEY(id))")
        cursor.execute("INSERT INTO user (id,username, password) VALUES (1, 'homer', '2aaab795b3836904f82efc6ca2285d927aed75206214e1da383418eb90c9052f')")
        cursor.execute("INSERT INTO user (id,username, password) VALUES (2, 'marge', 'b4b811fa40505329ae871e52f03527c3720c9af7fb8607819658535c5484c41e')")
        cursor.execute("INSERT INTO user (id,username, password) VALUES (3, 'bart', '9551dadbf76a27457946e70d1aebebe2132f8d3bce6378d216c11853524dd3a6')")
        cursor.execute("INSERT INTO user (id,username, password) VALUES (4, 'lisa', 'd84fe7e07bedb227cffff10009151d96fc944f6a1bd37cff60e8e4626a1eb1c3')")
        cursor.execute("INSERT INTO user (id,username, password) VALUES (5, 'maggie', 'aae5be5f6474904b686f639e0fcfd2be440121cd889fa381a94b71750758345e')")
        connection.commit()
        connection.close()

    @classmethod
    def tearDownClass(cls):
        connection = sqlite3.connect(SQLiteTest.DATABALE_NAME)
        cursor = connection.cursor()
        cursor.execute("DROP TABLE user")
        connection.commit()
        connection.close()

    def setUp(self):
        self.conn = sqlite3.connect(SQLiteTest.DATABALE_NAME)
        self.cur = self.conn.cursor()
        # begin()  start a database transaction
        # The Python sqlite3 module by default issues a BEGIN statement implicitly
        # before a Data Modification Language (DML) statement
        # (i.e. INSERT/UPDATE/DELETE/REPLACE).

    def tearDown(self):
        self.conn.rollback()
        self.conn.close()

    def test_select_all(self):
        # Exercise
        self.cur.execute('SELECT * from user')
        table = self.cur.fetchall()
        # Verify
        self.assertEqual(5, len(table))
        for row in table:
            print(row)

if __name__ == '__main__':
    unittest.main()
