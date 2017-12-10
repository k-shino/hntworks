from cassandra.cluster import Cluster

host = ["cassandra"]
keyspace = "elgoog"

cluster = Cluster(host)
session = cluster.connect()

session.execute("DROP KEYSPACE elgoog;")
session.execute("CREATE KEYSPACE elgoog WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 1};")
session.execute("CREATE TABLE elgoog.pagetable (id int PRIMARY KEY,url text,last_scanned_date int,score int,depth int,parent int);")
#session.execute("INSERT INTO elgoog.pagetable (id,url,last_scanned_date,score,depth,parent) VALUES (0,'http://www2.wagamachi-guide.com/chofu/',2017129,0,1,0);")
