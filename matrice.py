def matrice(longeur, largeur):
    nb_boules_largeur = (largeur-15)//30
    nb_boules_longeur = (longeur-100)//30
    if nb_boules_largeur > 27 :
        nb_boules_largeur = 27
    

    matrix = [[(None, (15 + 15*(j%2) + i*30, 15 + int((3**(1/2) * 15 * j)))) for i in range(nb_boules_largeur)]  for j in range(nb_boules_longeur) ]
    return matrix


print(matrice(315, 400))