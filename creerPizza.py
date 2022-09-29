'''
Créer des pizzas
Quelle meilleure façon de faire de la programmation qu'en créant des pizzas ?

Dans cet exercice, vous devez utiliser les méthodes de classe pour créer une pizza napolitaine et une pizza au
fromage avec la syntaxe suivante :

napo = Pizza.napolitaine()
fromage = Pizza.fromage()
La pizza napolitaine devra avoir comme nom "Napolitaine", comme ingrédients la liste ["Tomates", "Anchois"] et
comme prix 12.99€.

La pizza au fromage devra avoir comme nom "4 Fromages",
comme ingrédients ["Mozzarella", "Comté", "Cheddar", "Gorgonzola"] et comme prix 14.99€.
'''

class Pizza:
    def __init__(self, nom, ingredients, prix=9.99):
        self.nom = nom
        self.ingredients = ingredients
        self.prix = prix

    def __repr__(self):
        return f"La pizza {self.nom} qui contient {self.ingredients} est au prix de {self.prix} €"

    @classmethod
    def napolitaine(cls):
        return cls(nom="Napolitaine", ingredients=["Tomates", "Anchois"], prix=12.99)

    @classmethod
    def fromage(cls):
        return cls(nom="4 Fromages", ingredients=["Mozzarella", "Comté", "Cheddar", "Gorgonzola"], prix=14.99)


napo = Pizza.napolitaine()
fromage = Pizza.fromage()
print(napo)
print(fromage)



