#Bismillah
import os
import urlparse

dburl = os.environ.get("DATABASE_URL", "postgresql://postgresql@localhost/test")

dbstring = urlparse.urlparse(dburl)

print dbstring

print "username is " + dbstring.username
