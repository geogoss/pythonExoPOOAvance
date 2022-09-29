'''
Implémenter l'addition entre instances
Dans cet exercice, on veut permettre d'additionner plusieurs chaînes de caractères ensemble pour récupérer un
chemin de dossier.

La variable composite, qui additionne l'instance c avec des chaînes de caractères doit donc retourner
le chemin :

#>>> composite = c + "dossier" + "test" + "script"
/Users/john/dossier/test/script
Le symbole d'addition doit donc concaténer les différentes chaînes de caractères ensemble en ajoutant un
slash entre chaque chaîne de caractères afin de créer un chemin au format unix valide.
'''

class Chemin:
    def __init__(self, chemin):
        self.chemin = chemin

    def __str__(self):
        return self.chemin

    def __add__(self, content):
        return Chemin(self.chemin + "/" + content)


c = Chemin("/Users/john")
composite = c + "dossier" + "test" + "script"
print(composite)
caca = c + "essai pour le fun"
print(caca)


