#Bismillah
import os
import psycopg2
import urlparse

dburl = os.environ.get("DATABASE_URL", "postgresql://postgres@localhost/musictest")

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
