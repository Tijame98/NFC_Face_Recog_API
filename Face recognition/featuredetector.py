import cv2

# Charger les images depuis les répertoires respectifs
img1 = cv2.imread('TrainDatasetanas/anas.jpeg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('TestDatasetanas/image 2.jpeg', cv2.IMREAD_GRAYSCALE)

# Vérifier si les images ont été chargées avec succès
if img1 is None or img2 is None:
    print("Erreur: Impossible de charger les images.")
    exit()

# Créer le détecteur ORB avec 1000 points d'intérêt maximum
orb = cv2.ORB_create(nfeatures=1000)

# Détecter et calculer les descripteurs des points d'intérêt pour chaque image
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Dessiner les points d'intérêt sur les images
imgkp1 = cv2.drawKeypoints(img1, kp1, None)
imgkp2 = cv2.drawKeypoints(img2, kp2, None)

# Matcher les descripteurs entre les deux images
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

# Filtrer les bonnes correspondances
good = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good.append([m])

# Dessiner les correspondances sur une nouvelle image
img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)

# Afficher les images
cv2.imshow('kp1', imgkp1)
cv2.waitKey(0)
cv2.imshow('kp2', imgkp2)
cv2.waitKey(0)

cv2.imshow('img1', img1)
cv2.waitKey(0)
cv2.imshow('img2', img2)
cv2.waitKey(0)
cv2.imshow('img3', img3)
cv2.waitKey(0)
