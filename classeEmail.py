'''
Créer une classe e-mail
Dans cet exercice, vous devez compléter la classe e-mail.

- Créer une méthode send_to
Premièrement, vous devez créer une méthode send_to avec un paramètre email.

- Créer un attribut number_of_mails_sent
Vous devez créer un attribut de classe nommé number_of_mails_sent sur la classe Email.
Cet attribut devra être incrémenté de 1 à chaque fois qu'un e-mail est envoyé (donc à chaque fois que
la méthode send_to est appelée).

L'e-mail ne doit être envoyé que si l'attribut is_sent est False.
Si cet attribut est False, vous devez le modifier pour le passer à True pour signifier que l'e-mail a bien
été envoyé et empêcher ainsi l'utilisateur de l'envoyer une seconde fois.

Retourner des chaînes de caractères

    Si l'e-mail est envoyé, vous devez retourner dans la méthode send_to la chaîne de caractères "E-mail envoyé".

    Si l'e-mail a déjà été envoyé, vous devez retourner dans la méthode send_to la chaîne de caractères "L'e-mail a
    déjà été envoyé".

La variable response_01 devra donc contenir la chaîne de caractères "E-mail envoyé" et la variable response_02
devra contenir la chaîne de caractères "L'e-mail a déjà été envoyé".
'''

class Email:
    def __init__(self, content):
        self.content = content
        self.is_sent = False

    number_of_mails_sent = 0

    def send_to(self, email):
        if not self.is_sent:
            Email.number_of_mails_sent += 1
            self.is_sent = True
            return "E-mail envoyé"
        else:
            return "L'e-mail a déjà été envoyé"




email = Email(content="La nouvelle formation est disponible !")
response_01 = email.send_to(email="JohnSmith@gmail.com")
response_02 = email.send_to(email="JohnSmith@gmail.com")
print(response_01)
print(response_02)

