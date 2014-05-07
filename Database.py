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
    self.__connect()

    sql = """CREATE TABLE IF NOT EXISTS responses
    (
      id serial NOT NULL,
      name character varying(255),
      age character varying(255),
      "order" character varying(255),
      comp character varying(255),
      comp_conf character varying(255),
      recog character varying(255),
      piece character varying(255),
      piece_conf character varying(255),
      CONSTRAINT responses_pkey PRIMARY KEY (id)
    )"""

    cursor = self.conn.cursor()
    cursor.execute(sql)
    self.conn.commit()
    cursor.close()

    self.__close()

  def dropTables(self):
    self.__connect()

    sql = "DROP TABLE IF EXISTS responses"
    cursor = self.conn.cursor()
    cursor.execute(sql)
    self.conn.commit()
    cursor.close()

    self.__close()

  def __connect(self):
    self.conn = psycopg2.connect(
        database = self.url.path[1:],
        user = self.url.username,
        password = self.url.password,
        host = self.url.hostname,
        port = self.url.port
    )

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
