import unittest
import sqlite3


class DataAccessError(Exception):
    pass


class Article:
    """Entity class: a data object which can be stored in the database."""

    def __init__(self, id, description, price):
        self.id = id
        self.description = description
        self.price = price

    def __str__(self):
        return ("Article: [id = %d, description=%s, price=%d]" % (self.id, self.description, self.price))

    def __repr__(self):
        return str(self)


class ArticleDao:
    """Data Access Object: A class used to store Article objects in the database."""

    def __init__(self, dbc):
        self.conn = dbc;

    def insert(self, article):
        sql = "INSERT INTO article (id, description, price) VALUES (?,?,?)"
        parameters = (article.id, article.description, article.price)
        try:
            cur = self.conn.cursor()
            cur.execute(sql, parameters)
        except Warning as e:
            raise DataAccessError("Can't insert Article: " + article) from e

    def update(self, article):
        sql = "UPDATE article SET description=?, price=? WHERE id=?"
        parameters = (article.description, article.price, article.id)
        try:
            cur = self.conn.cursor()
            cur.execute(sql, parameters)
        except Warning as e:
            raise DataAccessError("Can't update Article: " + article) from e

    def delete(self, id):
        sql = "DELETE FROM article WHERE id=?"
        parameters = (id,)
        try:
            cur = self.conn.cursor()
            cur.execute(sql, parameters)
        except Warning as e:
            raise DataAccessError("Can't remove Article with id: " + id) from e

    def find_by_id(self, id):
        sql = "SELECT * FROM article WHERE id=?"
        parameters = (id,)
        try:
            cur = self.conn.cursor()
            cur.execute(sql, parameters)
            row = cur.fetchone()
            return Article(row[0], row[1], row[2])
        except Warning as e:
            raise DataAccessError("Can't find Article with given id: " + id) from e

    def find_all(self):
        sql = "SELECT * FROM article"
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            results = []
            for row in rows:
                results.append(Article(row[0], row[1], row[2]))
            return results
        except Warning as e:
            raise DataAccessError("Can't find Article with given id: " + id) from e


class SQLiteTest(unittest.TestCase):
    DATABASE_NAME = 'testdb.db'

    # Shared test fixture (database schema and test data)
    @classmethod
    def setUpClass(cls):
        conn = sqlite3.connect(SQLiteTest.DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE article (id INTEGER PRIMARY KEY, description TEXT, price INTEGER)")
        cursor.execute("INSERT INTO article (id,description, price) VALUES (1, 'Book: Fluent Python', 3599)")
        cursor.execute("INSERT INTO article (id,description, price) VALUES (2, 'Book: Python Crash Course', 2599)")
        conn.commit()
        conn.close()

    @classmethod
    def tearDownClass(cls):
        conn = sqlite3.connect(SQLiteTest.DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE article")
        conn.commit()
        conn.close()

    def setUp(self):
        self.conn = sqlite3.connect(SQLiteTest.DATABASE_NAME)
        self.cur = self.conn.cursor()
        self.dao = ArticleDao(self.conn)
        # begin()  start a database transaction

    def tearDown(self):
        # The underlying sqlite3 library operates in autocommit mode by default,
        # but the Python sqlite3 module by default does not.
        # The Python sqlite3 module by default issues a BEGIN statement implicitly
        # before a Data Modification Language (DML) statement
        # (i.e. INSERT/UPDATE/DELETE/REPLACE).
        self.conn.rollback()
        self.conn.close()

    def testInsert(self):
        # Exercise
        article = Article(3, 'Book: Effective Python', 4550)
        self.dao.insert(article)
        # Verify
        self.cur.execute("SELECT * FROM article WHERE id=3")
        row = self.cur.fetchone()
        self.assertEqual(3, row[0])
        self.assertEqual('Book: Effective Python', row[1])
        self.assertEqual(4550, row[2])

    def testUpdate(self):
        # Exercise
        article = Article(2, 'Book: Python Crash Course', 1599)
        self.dao.update(article)
        # Verify
        self.cur.execute("SELECT * FROM article WHERE id=2")
        row = self.cur.fetchone()
        self.assertEqual(2, row[0])
        self.assertEqual('Book: Python Crash Course', row[1])
        self.assertEqual(1599, row[2])

    def testDelete(self):
        # Exercise
        article = self.dao.delete(2)
        # Verify
        self.cur.execute("SELECT * from article")
        table = self.cur.fetchall()
        self.assertEqual(1, len(table))

    def testFindById(self):
        # Exercise
        article = self.dao.find_by_id(1)
        # Verify
        self.assertEqual(1, article.id)
        self.assertEqual('Book: Fluent Python', article.description)
        self.assertEqual(3599, article.price)

    def testFindAll(self):
        # Exercise
        articles = self.dao.find_all()
        # Verify
        print(articles)
        self.assertEqual(2, len(articles))


if __name__ == '__main__':
    unittest.main()
