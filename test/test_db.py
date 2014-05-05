import unittest
import os
import psycopg2
import urlparse

from Database import Database

class DatabaseConnectionTest(unittest.TestCase):
  def test_tableIsCreated(self):
    db = Database()
    conn = db.getConnection()

    cur = conn.cursor()

    sql = "Select * From responses"
    cur.execute(sql)
