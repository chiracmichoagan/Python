# créaction  de la classe Voiture
class Voiture:  
    # Constructeur (méthode spéciale) pour initialiser l'objet  
    def __init__(self, marque, modele, annee):  
        self.marque = marque    # Attribut  
        self.modele = modele     # Attribut  
        self.annee = annee       # Attribut  

    # Méthode pour afficher les informations de la voiture  
    def info(self):  
        return f"{self.marque} {self.modele}, {self.annee}"  

# Créer un objet de la classe Voiture  
ma_voiture = Voiture("Toyota", "Corolla", 2020)  
print(ma_voiture.info())  # Affiche "Toyota Corolla, 2020"

# heriter de la classe Voiture

class VoitureDeSport(Voiture):  
    def __init__(self, marque, modele, annee, vitesse_max):  
        super().__init__(marque, modele, annee)  # Appelle le constructeur de la classe parente  
        self.vitesse_max = vitesse_max            # Attribut supplémentaire  

    def info(self):  # Redéfinir la méthode info  
        return f"{super().info()}, Vitesse max: {self.vitesse_max} km/h"  

# Création d'un objet de la classe VoitureDeSport  
ma_voiture_sport = VoitureDeSport("Ferrari", "488", 2021, 340)  
print(ma_voiture_sport.info())  # Affiche les infos de la voiture de sport

# encapsulation des attributs 
# L'encapsulation signifie restreindre l'accès direct à certains des attributs d'un objet
class CompteBancaire:  
    def __init__(self, solde_initial):  
        self.__solde = solde_initial  # Attribut privé  

    def deposer(self, montant):  
        self.__solde += montant  

    def retirer(self, montant):  
        if montant <= self.__solde:  
            self.__solde -= montant  
        else:  
            print("Fonds insuffisants!")  

    def afficher_solde(self):  
        return self.__solde  

mon_compte = CompteBancaire(1000)  
mon_compte.deposer(500)  
print(mon_compte.afficher_solde())  # Affiche 1500

# Polymporphisme Le polymorphisme permet d'utiliser la même méthode sur différents objets. Par exemple, si tu as des classes différentes avec une méthode qui porte le même nom, tu peux appeler cette méthode sans te soucier de la classe de l'objet.
class Oiseau:  
    def chanter(self):  
        print("Chirp!")  

class Chien:  
    def chanter(self):  
        print("Woof!")  

def faire_chanter(animal):  
    animal.chanter()  

oiseau = Oiseau()  
chien = Chien()  

faire_chanter(oiseau)  # Affiche "Chirp!"  
faire_chanter(chien)   # Affiche "Woof!"


#notion de porter 

#un exemple de synthaxe

x = 100  # Variable globale  

def fonction_1():  
    x = 10  # Variable locale  
    def fonction_2():  
        nonlocal x  # Modifie x de fonction_1  
        x += 5  
        print(f"Valeur de x dans fonction_2 : {x}")  

    fonction_2()  
    print(f"Valeur de x dans fonction_1 : {x}")  

fonction_1()  
print(f"Valeur de x globale : {x}")  # Affiche 100


#  Syntaxe de Base des Expressions Régulières
# Voici quelques éléments de la syntaxe des expressions régulières :

# . : Correspond à n'importe quel caractère (sauf un saut de ligne).
# ^ : Indique le début d'une chaîne.
# $ : Indique la fin d'une chaîne.
# * : Correspond à zéro ou plusieurs répétitions du caractère précédent.
# + : Correspond à une ou plusieurs répétitions du caractère précédent.
# ? : Correspond à zéro ou une répétition du caractère précédent.
# {n} : Correspond à exactement n répétitions du caractère précédent.
# [abc] : Correspond à un caractère dans les crochets (a, b ou c).
# [^abc] : Correspond à un caractère qui n'est pas dans les crochets.
# \d : Correspond à un chiffre (équivalent à [0-9]).
# \w : Correspond à un caractère alphanumérique (lettres, chiffres ou underscore).
# \s : Correspond à un espace blanc (espace, tabulation, saut de ligne).
# 4. Exemples Pratiques
# Vérification d'un Motif avec match
# python
# import re  

# # Vérifier si la chaîne commence par "Bonjour"  
# resultat = re.match(r"Bonjour", "Bonjour tout le monde!")  
# if resultat:  
#     print("La chaîne commence par 'Bonjour'")  
# Recherche dans une Chaîne avec search
# python
# # Recherche d'un mot  
# resultat = re.search(r"monde", "Bonjour tout le monde!")  
# if resultat:  
#     print("Le mot 'monde' a été trouvé!")  
# Trouver toutes les Occurrences avec findall
# python
# # Trouver tous les chiffres  
# chaine = "Il y a 3 pommes, 5 oranges et 10 bananes."  
# resultats = re.findall(r"\d+", chaine)  
# print("Les chiffres trouvés :", resultats)  # Affiche ['3', '5', '10']  
# Remplacement de Motifs avec sub
# python
# # Remplacer les chiffres par '#'  
# chaine = "Il y a 3 pommes et 5 oranges."  
# nouvelle_chaine = re.sub(r"\d+", "#", chaine)  
# print(nouvelle_chaine)  # Affiche "Il y a # pommes et # oranges."  
# 5. Cas d'Utilisation Courants
# Valider des adresses e-mail :

# python
# email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"  
# email = "exemple@domain.com"  
# if re.match(email_pattern, email):  
#     print("Adresse e-mail valide!")  
# Extraction de numéros de téléphone :

# python
# text = "Contactez-nous au 01234 567890 ou au 09876 543210."  
# numeros = re.findall(r"\d{5} \d{6}", text)  
# print("Numéros de téléphone trouvés :", numeros) 