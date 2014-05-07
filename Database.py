#Database setup

import os
import psycopg2
import urlparse
from Response import Response

class Database:
  def __init__(self):
    self.dburl = os.environ.get("DATABASE_URL", "postgresql://postgres:@localhost/musictest")
    self.url = urlparse.urlparse(self.dburl)

  def setup(self):
    os.system("psql %s < ./init_db.sql" % (self.url.path[1:]))

  def dropTables(self):
    os.system("psql %s < ./drop_tables.sql" % (self.url.path[1:]))

  def __connect(self):
    self.conn = psycopg2.connect(
        database = self.url.path[1:],
        user = self.url.username,
        password = self.url.password,
        host = self.url.hostname,
        port = self.url.port
    )
    print self.url.path[1:]

  def __close(self):
    self.conn.close()

  def countResponses(self):
    self.__connect()

    sql = "Select Count(*) From responses;"
    cursor = self.conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    self.conn.commit()
    cursor.close()

    self.__close()

    return result[0]



  def saveResponse(self, response):
    self.__connect()

    sql = """INSERT INTO responses
          ("order", recog, comp, comp_conf, piece, piece_conf, name, age)
          VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
            response.order,
            response.recog,
            response.comp,
            response.comp_conf,
            response.piece,
            response.piece_conf,
            response.name,
            response.age
          )

    cursor = self.conn.cursor()
    cursor.execute(sql)
    self.conn.commit()

    self.__close()
