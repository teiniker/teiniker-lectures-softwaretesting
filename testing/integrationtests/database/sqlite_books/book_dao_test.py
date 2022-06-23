import unittest
import sqlite3

from book_dao import Book, BookDao

class SQLiteTest(unittest.TestCase):
    DATABASE_NAME = 'testdb.db'

    # Shared test fixture (database schema and test data)
    @classmethod
    def setUpClass(cls):
        conn = sqlite3.connect(SQLiteTest.DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE book (isbn TEXT PRIMARY KEY, title TEXT, authors TEXT, publisher TEXT, year INTEGER)")
        cursor.execute("INSERT INTO book (isbn, title, authors, publisher, year) VALUES ('1449355730', 'Learning Python: Powerful Object-Oriented Programming', 'Mark Lutz', 'OReilly', 2013)")
        cursor.execute("INSERT INTO book (isbn, title, authors, publisher, year) VALUES ('1593279280', 'Python Crash Course', 'Eric Matthes', 'No Starch Press', 2019)")
        conn.commit()
        conn.close()

    @classmethod
    def tearDownClass(cls):
        conn = sqlite3.connect(SQLiteTest.DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE book")
        conn.commit()
        conn.close()

    def setUp(self):
        self.conn = sqlite3.connect(SQLiteTest.DATABASE_NAME)
        self.cur = self.conn.cursor()
        self.dao = BookDao(self.conn)
        # begin()  start a database transaction

    def tearDown(self):
        self.conn.rollback()
        self.conn.close()

    def test_insert(self):
        # Exercise
        book = Book('1718501048', 'Effective C: An Introduction to Professional C Programming', 'Robert C. Seacord', 'No Starch Press', 2020)
        self.dao.insert(book)
        # Verify
        self.cur.execute("SELECT * FROM book WHERE isbn='1718501048'")
        row = self.cur.fetchone()
        self.assertEqual('1718501048', row[0])
        self.assertEqual('Effective C: An Introduction to Professional C Programming', row[1])
        self.assertEqual('Robert C. Seacord', row[2])
        self.assertEqual('No Starch Press', row[3])
        self.assertEqual(2020, row[4])

    def test_find_by_isbn(self):
        # Exercise
        book = self.dao.find_by_isbn('1593279280')
        # Verify
        self.assertEqual('1593279280', book.isbn)
        self.assertEqual('Python Crash Course', book.title)
        self.assertEqual('Eric Matthes', book.authors)
        self.assertEqual('No Starch Press', book.publisher)
        self.assertEqual(2019, book.year)

if __name__ == '__main__':
    unittest.main()
