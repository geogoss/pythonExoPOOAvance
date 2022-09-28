'''
Empêcher la modification d'un attribut
Le but de cet exercice est d'empêcher la modification de l'attribut numero de l'instance john.

Je ne vous en dis pas plus, à vous de trouver un moyen d'empêcher le numéro d'être modifié.

Si on essaie de modifier l'attribut, le script doit retourner une erreur de type AttributeError.
'''

class Compte:
    def __init__(self, nom, numero, balance):
        self.nom = nom
        self._numero = numero
        self.balance = balance

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        raise AttributeError("Vous ne pouvez pas modifier le numéro du compte.")


john = Compte(nom="John Smith", numero="123456", balance=20000)

print(john.numero)

john.numero = 45


