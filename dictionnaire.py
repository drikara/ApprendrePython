dictionnaire = {
    "nom":"ouattara",
    "prenoms":'karamoko drissa',
    'age': 33
}
# lire un élement dans un dictionnaire
print(dictionnaire["nom"])
#modifier un élement dans un dictionnaire
dictionnaire["nom"] = "kone"
print(dictionnaire["nom"])
#supprimer un element dans un dictionnaire
dictionnaire.pop("age")
print(dictionnaire)
# techniques de boucles
for k,v in dictionnaire.items():
    print(f" {k} : {v}")
    
# autre méthode
for c,v in enumerate(["jean","korotoumou","jean"]):
    print(f"{c} : {v}")
    
question = ["anniversaire","nom","ville"]
reponse = ["07/02/1956","kone","Bouaké"]
for k,c in zip( question, reponse):
    print(f"quel est ta {k} ? c'est {c}" .format(k,c))
    
#pour faire une boucle en seens inverse on utilise reversed

for i in reversed(range(10)):
    print(i)