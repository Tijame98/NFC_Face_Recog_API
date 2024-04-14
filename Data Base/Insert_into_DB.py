import psycopg2 as pg

with open('Insert_DB.sql', 'r') as f:
	schema = f.read()

conn = pg.connect(dbname = 'nfc', user = 'raspi', password = 'admin', host = 'localhost')
if(conn):
	print("Connectd to database")	
else:
	print("Connexion Failed")		
cur = conn.cursor()
cur.execute(schema)
conn.commit()
print("Insertion successful")

cur.close()
conn.close()

print('Data base is set up')
