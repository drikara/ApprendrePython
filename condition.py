
# instruction if
"""age = int(input(f"veuillez entrer votre age "))
if age < 0 :
    print(f"impossible , une personne ne peut pas avoir un age inférieur à 0")
elif age < 18:
    print(f"vous etes mineur")

    
else:
    print(f"vous etes majeur")

# instruction for
words = ["banane","ali","clemandine"]
for word in words:
    print( word, end=',')
print(f"la taille de la liste est :", len(words))
"""
#la fonction range

for i in range(0 , 10 , 1):
    print(i , end=' ; ')


noms = ["jean" , "mariam" , "ali" , "ladji"]
for nom in range(len(noms)):
    print(f"{nom} - {noms[nom]}")

