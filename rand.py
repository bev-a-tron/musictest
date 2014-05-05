#Bismillah
import os
import psycopg2
import urlparse
from Database import Database

db = Database()
conn = db.getConnection()
db.createTables()

cur = conn.cursor()

# sql = "CREATE TABLE IF NOT EXISTS responses ("
# sql += "id serial PRIMARY KEY, "
# sql += "name character varying(255), "
# sql += "age character varying(255)"
# sql += ")"


sql = "CREATE TABLE responses"
sql += "("
sql += "  id serial NOT NULL,"
sql += "  \"order\" character varying(255),"
sql += "  CONSTRAINT responses_pkey PRIMARY KEY (id)"
sql += ")"
sql += "WITH ("
sql += "  OIDS=FALSE"
sql += ");"
sql += "ALTER TABLE responses"
sql += "  OWNER TO postgres;"

# cur.execute(sql)

sql = "select * from responses"
cur.execute(sql)

rows = cur.fetchall()

for row in rows:
  print row
