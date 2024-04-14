import cv2

# Charger la photo d'entraînement (anas.jpeg)
reference_image = cv2.imread('TrainDatasetanas/anass.jpeg', cv2.IMREAD_GRAYSCALE)

# Créer un détecteur ORB avec 1000 points d'intérêt maximum
orb = cv2.ORB_create(nfeatures=1000)

# Extraire les descripteurs de la photo d'entraînement
kp1, des1 = orb.detectAndCompute(reference_image, None)

# Initialiser le détecteur de visage Haar Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialiser la capture vidéo à partir de la caméra
cap = cv2.VideoCapture(0)

while True:
    # Capturer le flux vidéo de la caméra
    ret, frame = cap.read()

    # Vérifier si la capture a réussi
    if not ret:
        break

    # Convertir l'image capturée en niveaux de gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Détecter les visages dans l'image capturée
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Parcourir tous les visages détectés
    for (x, y, w, h) in faces:
        # Extraire le visage de l'image capturée
        face_roi = gray[y:y+h, x:x+w]

        # Trouver les descripteurs du visage
        kp2, des2 = orb.detectAndCompute(face_roi, None)

        # Si descripteurs trouvés, faire la comparaison avec la photo de référence
        if des2 is not None:
            # Matcher les descripteurs entre la photo de référence et le visage capturé
            bf = cv2.BFMatcher()
            matches = bf.knnMatch(des1, des2, k=2)

            # Filtrer les bonnes correspondances
            good = []
            for m, n in matches:
                if m.distance < 0.75 * n.distance:
                    good.append(m)

            # Si le nombre de bonnes correspondances est supérieur à un certain seuil
            if len(good) > 20:
                # Afficher le nom "Anas" sur l'image capturée
                cv2.putText(frame, "Anas", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                print("anas kayn")
            elif len(good) < 2 :
                # Dessiner un contour rouge autour du visage
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                # Afficher le message "Inconnu"
                cv2.putText(frame, "Inconnu", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Afficher l'image capturée avec les visages détectés
    cv2.imshow('Face Detection', frame)

    # Attendre 1 milliseconde et vérifier si l'utilisateur appuie sur la touche 'q' pour quitter
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la capture vidéo et fermer toutes les fenêtres
cap.release()
cv2.destroyAllWindows()
