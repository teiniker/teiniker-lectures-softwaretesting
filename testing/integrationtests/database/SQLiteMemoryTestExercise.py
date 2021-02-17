import unittest
import sqlite3

# Exercise: SQLite in-memory database
# We can use the special name :memory: to create a database in RAM.
# The database ceases to exist as soon as the database connection is closed!!
#
# 1) Setup and teardown
#    Implement the setUp() and tearDown() methods of the given test class.
#    Note that the in-memory database only exists as long as the database
#    connection.
#    CREATE TABLE user (id INTEGER, username TEXT, password TEXT, PRIMARY KEY(id))
#    INSERT INTO user (id,username, password) VALUES (1, 'homer', '2aaab795b3836904f82efc6ca2285d927aed75206214e1da383418eb90c9052f')
#    INSERT INTO user (id,username, password) VALUES (2, 'marge', 'b4b811fa40505329ae871e52f03527c3720c9af7fb8607819658535c5484c41e')
#    INSERT INTO user (id,username, password) VALUES (3, 'bart', '9551dadbf76a27457946e70d1aebebe2132f8d3bce6378d216c11853524dd3a6')
#    INSERT INTO user (id,username, password) VALUES (4, 'lisa', 'd84fe7e07bedb227cffff10009151d96fc944f6a1bd37cff60e8e4626a1eb1c3')
#    INSERT INTO user (id,username, password) VALUES (5, 'maggie', 'aae5be5f6474904b686f639e0fcfd2be440121cd889fa381a94b71750758345e')

#  2) SQL Queries
#    Implement a test case for every of the following SQL queries:

#    > SELECT * from user
#       Verify the number of rows returned from the query

#    > SELECT * from user ORDER BY username
#       Verify if the usernames returned from the query are in the right order.

#    > parameters = ('m%',)
#      execute("SELECT * from user WHERE username LIKE ?", parameters)
#      Verify the number of usernames found (2: marge and maggie)

#    > parameters = ('bart',)
#      execute("SELECT * from user where username=?", parameters)
#      Verify the found record (id, username, password)

#    > parameters = ('lisa', 'd84fe7e07bedb227cffff10009151d96fc944f6a1bd37cff60e8e4626a1eb1c3')
#      execute("SELECT * from user where username=? AND password=?", parameters)
#      Verify if such a user exists (number of found records == 1)

class SQLiteMemoryTest(unittest.TestCase):

    DATABALE_NAME = ':memory:'

    # TODO

if __name__ == '__main__':
    unittest.main()

