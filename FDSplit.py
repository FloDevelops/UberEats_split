def greet():
	print("""Hello!
Welcome to the Food Delivery Split tool!""")

# Recursively builds and returns a list of guests' names
def get_guests_names(count = 1):
	question = "What's the name of the guest {0}".format(count)
	if count <= 2:
		question += ": "
		guest_name = input(question)
	else:
		question += "?\nEnter 's' to Stop adding guests: "
		guest_name = input(question)

	if guest_name.lower() == "s":
		return []
	# elif type(guest_name) != str:
	# 	return get_guests_names(count)
	else:
		count += 1
		return [guest_name] + get_guests_names(count)

def make_guests_dict():
	guests_list = get_guests_names()
	guests_dict = {}
	for guest in guests_list:
		guests_dict[guest] = []
	return guests_dict


def get_guest_items_amounts(guest, item_list = []):
	if not item_list:
		question = "\nHow much was {0}'s first item? ".format(guest)

	else:
		item_list_string = [str(item) for item in item_list]
		print("Currently, {0}'s items list is:\n-".format(guest), "\n- ".join(item_list_string))
		question = "How much was {0}'s item number {1}?\nEnter 's' to Stop adding items: ".format(guest, len(item_list)+1)

	item = input(question)
	if item == "s":
		return item_list
	else:
		item_amount = float(item)
		item_list.append(item_amount)
		return get_guest_items_amounts(guest, item_list)


def get_guest_order_amount(guests_dict):
	for guest in guests_dict:
		order = get_guest_items_amounts(guest, [])
		total = 0
		for item in order:
			total += item
		guests_dict[guest] = [order, total]
	return guests_dict

print(get_guest_order_amount({"Flo": [], "Lolo": []}))


def get_delivery_charge_amount():
	pass

def get_tip_amount():
	pass

def get_rebate_amount():
	pass



def calculate_taxes():
	pass




def run_split():
	greet()
	guests = make_guests_dict()
	get_guest_order_amount(guests)



# run_split()