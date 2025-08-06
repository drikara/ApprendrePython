a = 5
b = 7
addition = a + b
print(f"{a} + {b} = ",addition)
multiplication = a * b
print(f"{a} * {b} = ", multiplication)
soustration = a - b
print(f'{a} - {b} =', soustration)
#donne le quotient
division = b / a
print(f'{b} / {a} = ', division)
#donne la partie entière  du quotient 
div = b // a
print(f"{b} / {a} = ", div)
# donne le reste d'une division
modulo = b % 2 
print(f"{a} / 2 =" , modulo)
#utilisation des chaines de caratères
nom = "ouattara"
prenoms = "karamoko drissa"
print(f"mon nom est: {nom}\n mon prenoms est: {prenoms}")
print("""
      demain je vais à adjamé
          et toi
    je vais avec loukou et isaac      
      
      
      
      """)
#concatener deux chaines de caractères
py = "py"
thon = "thon"
res = py + thon
print(res)
#mot
word = "python"
print(f"la première lettre du mot python est :",word[0])
print(f"la dernière lettre du mot python", word[-1])
#trancher une chaine de caractère ou bien slice
print(f"les deux premières  lettre du mot est : ", word[0:2])
print(f"toutes les lettres du mot est ", word[0:])
print(f"les trois dernières lettres du mot sont : ", word[0:3])
print(f"les quatres premières lettres du mot python sont: ", word[:4])
print(f"les deux premières lettrs du mot sont : ",word[:2])
#le mot est python
#premier indice indique la position et la deuxième indique la taille
# il faut noter que on ne peut pas modifier des chaines de caractèrs en python donc ils sont immuables

print(f"je veux afficher à partir de la deuxième lettre et quatre lettre :" , word[2:4])
#pour connaitre la taille d'une chaine de caractère on utilise len
print(f"la taille du chaine python est :",len(word))