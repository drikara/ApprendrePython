from collections import deque

# liste des fruits
fruits = ["banane","carotte", "pomme ", 'orange', "ananas","carotte"]
# le count affiche le nombre d'elements qui a la valeur x dans la liste
#print(fruits.count("banane"))
#index renvoie la poqition du premier element dans la liste 
#print(fruits.index('carotte'))
#reverse inverse l'ordre des elements dans la liste
#fruits.reverse()
#print(fruits)

#append ajoute l'elemnt à la fin de la liste

#fruits.append("clemantine")
#print(fruits)

#sort ordonne les elements de la liste

fruits.sort()
print(fruits)

#copy permet de copié une liste

li = fruits.copy()
print(li)

#insert permet d'inserer un element à la position souhaité
fruits.insert(0,"jean")
print(fruits)
# insert , sort et remove n'affichent pas de valeur de retour elles renvoient plutot None
queue = deque(["jean","philippe","ali"])
queue.append("mariam")
queue.append("said")
print(queue.pop())

mul = []
"""for i in range(10):
    mul.append(i * 5)
    
print(mul)
"""
mul = [x ** 2 for x in range(5)]
print(mul)
