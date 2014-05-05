#Bismillah
import os
import psycopg2
import urlparse

dburl = os.environ.get("DATABASE_URL", "postgresql://postgres:@localhost/musictest")

url = urlparse.urlparse(dburl)

print url

print "username is " + url.username

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

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

cur.execute(sql)

sql = "select * from responses"
cur.execute(sql)

rows = cur.fetchall()

for row in rows:
  print row
