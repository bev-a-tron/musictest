import os
import application
import unittest
from flask.ext.fillin import FormWrapper
from flask.testing import FlaskClient

from Database import Database

class FunctionalTest(unittest.TestCase):

  def setUp(self):
    self.db = Database()
    self.db.setup()

  def tearDown(self):
    self.db.dropTables()

  def test_homepageDisplays(self):
    client = FlaskClient(application.app, response_wrapper=FormWrapper)
    page = client.get('/')
    assert 'music' in page.data

  def test_firstItemDisplays(self):
    client = FlaskClient(application.app, response_wrapper=FormWrapper)
    page = client.get('/', follow_redirects=True)
    page.form.fields['name'] = 'Asif'
    page.form.fields['age'] = '23'
    page2 = page.form.submit(client, follow_redirects=True)
    assert 'Sound clip #1' in page2.data
