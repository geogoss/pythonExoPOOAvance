'''
Gérer une classe d'élèves
Dans cet exercice, vous devez créer une classe Classe (oui, c'est un peu meta...) qui permette de gérer les
élèves créés avec la classe Eleve.

La classe Classe doit posséder une méthode statique ajouter_eleve qui permette d'ajouter un élève avec un
prénom et un nom.
Les instances d'élèves créées avec cette méthode statique doivent être ajoutées à une liste élèves
appartenant à Classe.
Vous devez également modifier la représentation des instances créées à partir d'Eleve pour qu'elles affichent
le prénom et le nom des élèves.
Dans le cas de ce script, l'attribut eleves devra donc être une liste qui contient une instance d'un élève qui
s'appelle "John Smith" et cet attribut devra afficher la liste suivante :

#>>> Classe.eleves
["John Smith"]
'''

class Eleve:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

    def __repr__(self):
        return f"{self.prenom} {self.nom}"

class Classe:

    liste_eleves = []

    @staticmethod
    def ajouter_eleve(nom, prenom):
        eleve = Eleve(prenom=prenom, nom=nom)
        Classe.liste_eleves.append(eleve)


Classe.ajouter_eleve("John", "Smith")
Classe.ajouter_eleve("geof", 'goss')
print(Classe.liste_eleves)


