#Database setup

import os
import psycopg2
import urlparse

class Database:
  def __init__(self):
    self.dburl = os.environ.get("DATABASE_URL", "postgresql://postgres:@localhost/musictest")
    self.url = urlparse.urlparse(self.dburl)

  def setupTables(self):
    os.system("psql %s < ./init_db.sql" % (self.url.path[1:]))

  def getConnection(self):
    conn = psycopg2.connect(
        database = self.url.path[1:],
        user = self.url.username,
        password = self.url.password,
        host = self.url.hostname,
        port = self.url.port
    )
    return conn
