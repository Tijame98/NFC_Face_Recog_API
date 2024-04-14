import psycopg2 as pg

#se connecter a la base de donner locale sur la raspi 3
conn = pg.connect(dbname = 'nfc', user= 'raspi', password = 'admin', host = 'localhost')

#creer un curor pour lui affecter les requtes a executer 
cur = conn.cursor()

#inserer un eleve dans la base de données pour faire un test, pour valider les connexions avec la base de données 
cur.execute("INSERT INTO eleve values (500415610577, 'David', 'Davidson')")

cur.execute("INSERT INTO photo values (2, 500415610577)")

#valider la requete du cursor puis fermer le cursor et la connexion
conn.commit()
cur.close()
conn.close()

