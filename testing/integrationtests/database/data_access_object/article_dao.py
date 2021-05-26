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
        self.conn = dbc

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
