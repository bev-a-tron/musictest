import unittest
import os

from Database import Database
from Response import Response

class DatabaseConnectionTest(unittest.TestCase):
  def setUp(self):
    self.db = Database()
    self.db.setup()

  def tearDown(self):
    self.db.dropTables()

  def test_countResponses(self):
    count = self.db.countResponses()
    self.assertEquals(count, 0)

  def test_insertsResponseIntoTable(self):
    oldCount = self.db.countResponses()

    resp = Response()
    resp.recog = "True"
    resp.comp = "Composer"
    resp.comp_conf = "5"
    resp.piece = "Piece"
    resp.piece_conf = "3"
    resp.name = "Name"
    resp.age = "23"

    self.db.saveResponse(resp)

    newCount = self.db.countResponses()
    newResponses = newCount - oldCount

    self.assertEquals(newResponses, 1)
