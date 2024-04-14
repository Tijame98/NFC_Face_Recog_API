import psycopg2 as pg

with open('schema.sql', 'r') as f:
	schema = f.read()
 
conn = pg.connect(dbname = 'nfc', user = 'raspi', password = 'admin', host = 'localhost')
if(conn):
	print("Connectd to database")	
else:
	print("Connexion Failed")
cur = conn.cursor()
cur.execute(schema)
conn.commit()
print('Tables are created')
cur.close()
conn.close()
