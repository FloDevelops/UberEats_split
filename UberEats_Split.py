class Guest:
    def __init__(self, name):
        self.name = name
        self.order_amounts = []
        self.order_subtotal = 0
        self.order_total = 0

    def add_order_amounts(self, item_amount):
        self.order_amounts.append(item_amount)
        self.order_subtotal += item_amount



def add_guests(guests_list):
    continue_adding = True
    while continue_adding:
        guest_input = input("To add a new guest type his/her name.\nTo STOP adding guests type 's': ")
        if guest_input == "s":
            continue_adding = False
            print()
        else:
            guests_list.append(Guests(guest_input))

def calculate_sub_total(guest_list):
    sub_total = 0
    for guest in guest_list:
        sub_total += guest.order_subtotal
    return sub_total

def calculate_full_bill(sub_total, delivery_charge, tip, rebate):
    total_less_tip = (sub_total + delivery_charge - rebate)
    taxes = total_less_tip * 0.14975
    total = total_less_tip + tip + taxes
    total_rounded = round(total, 2)
    return total_rounded

def calculate_guests_bills(guest_list, sub_total, delivery_charge, tip, rebate):
    delivery_splitted = delivery_charge / len(guest_list)
    rebate_splitted = rebate / len(guest_list)
    for guest in guest_list:
        tip_splitted = tip * (guest.order_subtotal / sub_total)
        guest_total = guest.order_subtotal + delivery_splitted + tip_splitted - rebate_splitted
        guest.order_total = round(guest_total, 2)
        print("{0}'s order is $ {1}".format(guest.name, guest.order_total))



# print(calculate_full_bill(28.04, 3.99, 2.80, 0))


guests = [Guest(input("What's the first guest's name? "))]
guests.append(Guest(input("What's the second guest's name? ")))
add_guests(guests)

for guest in guests:
    add_item = True
    while add_item:
        amount_input = input("To add an item to {name} enter its amount.\nTo continue to the next guest enter 's': ".format(name=guest.name))
        if amount_input == "s":
            add_item = False
            print()
        else:
            guest.add_order_amounts(float(amount_input))


sub_total = calculate_sub_total(guests)

delivery_charge = float(input("How much was the delivery charge? "))

tip_type = input("Do you prefer to enter the tip in Dollars or Percentage? Enter 'd' or 'p': ")
if tip_type == "d":
    tip = float(input("How much was the tip in Dollars? "))
elif tip_type == "p":
    tip_pct = float(input("How much was the tip in Percentage (use 00 or 00.00 format)? ")) / 100
    tip = round(sub_total * tip_pct, 2)

rebate = -float(input("If you had a rebate, how much was it (else enter 0)? "))

################################################################################ TAXES MISSING

full_bill = calculate_full_bill(sub_total, delivery_charge, tip, rebate)

print()
calculate_guests_bills(guests, sub_total, delivery_charge, tip, rebate)

print("\nThe full bill should be $ {0}.".format(full_bill))









# PROGRAM

# print("Bienvenue sur la plateforme de partage pour UberEats !")

# guests = [Guest(input("Quel est le nom de la premièe personne ? ")), Guest(input("Quel est le nom de la deuxième personne ? "))] # Créer un liste de 2 guests (minimum requis)
# add_guests = True # Ajouter de nouvelles personnes à la liste

# while add_guests == True:
#     nouveauParticipant = input("Pour ajouter une personne supplémentaire entrez son nom.\nSi toutes les personnes sont enregistrées entrez 's'. ")
#     if nouveauParticipant == "s":
#         add_guests = False
#     else:
#         guests.append(Guest(nouveauParticipant)


# ########################TO CONTINUE FROM HERE        







  

# montants = [] # Créer une liste qui contiendra le montant de chaque commande
# for personne in guests: # Ajouter le montant de la commande de chaque personne dans la liste des montants
#     montants.append(float(input("Quel est le montant de la commande de " + personne + " ? ")))

# print("Vous avez entré : " + str(guests) + str(montants))# Afficher les deux listes pour vérification


# # Définir les variables des frais supplémentaires
# devise = "CAD"
# taxes = 0.14975
# fraisLivraison = float(input("Quel est le montant des frais de livraison ? "))
# pourboire = float(input("Quel pourcentage de pourboire avez-vous donné (en nombre entier, exemple 15) ? ")) / 100
# réduction = float(input("Quel est le montant de votre réduction utilisée (entrez 0 si vous n'avez pas utilisé de réduction) ? "))

# # Calculer la part de chaque personne et afficher tous les résultats
# for i in range(len(guests)):
#     print(guests[i] + " : " + str(calcul(montants[i], len(guests), fraisLivraison, pourboire, réduction)) + " " + devise)

# # Calculer et afficher le total de la commande avec tous les frais pour contrôler l'exactitude des résultats.
# total = round(((sum(montants) + fraisLivraison) * (1 + taxes) - réduction) * (1 + pourboire), 2)
# print("Le montant total de la commande devrait être de " + str(total) + " " + devise + ".")

# # Fin du programme
# input("Bye bye !")
