class Guest:
    def __init__(self, name):
        self.name = name
        self.order_amount = 0

    def add_order_amount(self. amount):
        self.order_amount += amount

        

# Convertir le montant HT d'une personne en TTC avec autres frais partagés inclus
def calcul(montant, nbguests, fraisLivraison, pourboire, réduction):

    fraisLivraisonPP = fraisLivraison / nbguests
    réductionPP = réduction / nbguests

    return round(((montant + fraisLivraisonPP) * (1 + taxes) - réductionPP) * (1 + pourboire), 2)






# PROGRAM

print("Bienvenue sur la plateforme de partage pour UberEats !")

guests = [Guest(input("Quel est le nom de la premièe personne ? ")), Guest(input("Quel est le nom de la deuxième personne ? "))] # Créer un liste de 2 guests (minimum requis)
add_guests = True # Ajouter de nouvelles personnes à la liste

while add_guests == True:
    nouveauParticipant = input("Pour ajouter une personne supplémentaire entrez son nom.\nSi toutes les personnes sont enregistrées entrez 's'. ")
    if nouveauParticipant == "s":
        add_guests = False
    else:
        guests.append(Guest(nouveauParticipant)


########################TO CONTINUE FROM HERE        







  

montants = [] # Créer une liste qui contiendra le montant de chaque commande
for personne in guests: # Ajouter le montant de la commande de chaque personne dans la liste des montants
    montants.append(float(input("Quel est le montant de la commande de " + personne + " ? ")))

print("Vous avez entré : " + str(guests) + str(montants))# Afficher les deux listes pour vérification


# Définir les variables des frais supplémentaires
devise = "CAD"
taxes = 0.14975
fraisLivraison = float(input("Quel est le montant des frais de livraison ? "))
pourboire = float(input("Quel pourcentage de pourboire avez-vous donné (en nombre entier, exemple 15) ? ")) / 100
réduction = float(input("Quel est le montant de votre réduction utilisée (entrez 0 si vous n'avez pas utilisé de réduction) ? "))

# Calculer la part de chaque personne et afficher tous les résultats
for i in range(len(guests)):
    print(guests[i] + " : " + str(calcul(montants[i], len(guests), fraisLivraison, pourboire, réduction)) + " " + devise)

# Calculer et afficher le total de la commande avec tous les frais pour contrôler l'exactitude des résultats.
total = round(((sum(montants) + fraisLivraison) * (1 + taxes) - réduction) * (1 + pourboire), 2)
print("Le montant total de la commande devrait être de " + str(total) + " " + devise + ".")

# Fin du programme
input("Bye bye !")
