class DataAccessError(Exception):
    pass


class Article:
    """Entity class: a data object which can be stored in the database."""

    def __init__(self, oid, description, price):
        self.oid = oid
        self.description = description
        self.price = price

    def __str__(self):
        return f"Article: [id = {self.oid}, description={self.description}, price={self.price}]"

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
        except Warning as ex:
            raise DataAccessError("Can't insert Article: " + article) from ex

    def update(self, article):
        sql = "UPDATE article SET description=?, price=? WHERE id=?"
        parameters = (article.description, article.price, article.id)
        try:
            cur = self.conn.cursor()
            cur.execute(sql, parameters)
        except Warning as ex:
            raise DataAccessError("Can't update Article: " + article) from ex

    def delete(self, oid):
        sql = "DELETE FROM article WHERE id=?"
        parameters = (oid,)
        try:
            cur = self.conn.cursor()
            cur.execute(sql, parameters)
        except Warning as ex:
            raise DataAccessError("Can't remove Article with id: " + id) from ex

    def find_by_id(self, oid):
        sql = "SELECT * FROM article WHERE id=?"
        parameters = (oid,)
        try:
            cur = self.conn.cursor()
            cur.execute(sql, parameters)
            row = cur.fetchone()
            return Article(row[0], row[1], row[2])
        except Warning as ex:
            raise DataAccessError("Can't find Article with given id: " + id) from ex

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
        except Warning as ex:
            raise DataAccessError("Can't find Article with given id: " + id) from ex
