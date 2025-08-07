#les listes sont structure de données , ils ne sont pas du meme type, ils sont à l'intérieur d'un crochet
#il faut noter que les tranche permet de faire une copie de liste
squares = [3,5,6,7,3]
print(squares)
# pour recuperer le premier élement d'une liste
premier = squares[0]
print(f"le premier element du liste {squares} est :",premier)
# le dernier élement de la liste 
dernier = squares[-1]
print(f"le dernier élement de la liste {squares} est :", dernier)
# pour modifier le premier élément
squares[0] = 678
print(f"nous avons changé la valeur du premier element de la liste :", squares)
# je veux afficher les élémnent à partir de la 3 eme position
print(squares[3:])
#pour ajouter un élémént à la fin de la liste on utilise la m"thode append
squares.append(6900)
print(f"la nouvelle liste est : ", squares)
#je crée une nouvelle liste 
listes = squares[:]
print(f"la nouvelle liste est :", listes)
#la taille de la liste
print(f"voici la taille de notre liste: ", len(listes))