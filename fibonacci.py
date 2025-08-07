a , b = 0 , 1
while a < 10:
    #Le paramètre nommé end peut servir pour enlever le retour à la ligne ou pour terminer la ligne par une autre chaîne :
    print(a, end=" , ")
    a , b = b , a + b
    # tout entier différent de zéro est vrai et zéro est faux
    #une liste, ou en fait toute séquence ; une séquence avec une valeur non nulle est vraie, une séquence vide est fausse.