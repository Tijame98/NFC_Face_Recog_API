import psycopg2 as pg
import extract_ID as ext

#se connecter a la base de donner locale sur la raspi 3
conn = pg.connect(dbname = 'nfc', user= 'raspi', password = 'admin', host = 'localhost')

cur = conn.cursor()

#chercher si le ID scanner est bien dans l base de données 
cur.execute("SELECT * FROM eleve")

#stoker la sortie du requte dans une liste pour faire un retour si le test est passé ou pas
Val = cur.fetchone()

with open('feedback.txt', 'w') as f:
    if Val[0] == ext.id_value:
        f.write('ID is OK' + str(Val[1]) + str(Val[2]))
    else:
        f.write('No matching ID')

f.close()

cur.close()
conn.close()