#ouvrir le fichier txt, et parcourir ses lignes
#pour extraire le ID dela carte

with open('recieved_ID.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if 'ID:' in lines:
            id_value = line.split('ID:')[1].strip()
            break

print(id_value)
