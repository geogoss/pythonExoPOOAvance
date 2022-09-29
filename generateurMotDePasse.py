'''
Créer un générateur de mots de passe
Dans cet exercice, rien de très compliqué, mais là encore vous partez de 0.

Vous devez créer une classe PasswordGenerator qui permet de générer grâce à une méthode generate
un mot de passe aléatoire composé de lettres minuscules ou majuscules et de chiffres de 0 à 9 d'une longueur
indiquée par un argument envoyé à la méthode generate :

#>>> mot_de_passe = PasswordGenerator.generate(15)
"MPCk5L1q2jEulId"
'''
import random
import string



class PasswordGenerator:

    @staticmethod
    def generate(longueur):
        mdp = random.sample(string.digits + string.ascii_letters, longueur)
        print("".join(mdp))


mot_de_passe = PasswordGenerator.generate(15)

