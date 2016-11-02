contacts = {} #each value is also a dictionary
subscriptions = {} #doesn't really matter what the value is

def add_contact(phone_number, name, age):
    phone_number = str(phone_number)
    try:
        contacts[phone_number]
    except KeyError:
        contacts[phone_number] = {
            "name": name,
            "age": age
        }
    else:
        print("Contact already exists for phone number: {}".format(phone_number))

def update_contact(phone_number, key, value):
    phone_number = str(phone_number)
    try:
        contacts[phone_number]
    except KeyError:
        print("Contact does not exist for phone number: {}".format(phone_number))
    else:
        try:
            contacts[phone_number][str(key).lower()] = value
            try:
                subscriptions[phone_number]
                print("You are subscribed to {} and it changed. Name: {} Age: {}".format(
                      phone_number, contacts[phone_number]["name"], contacts[phone_number]["age"]))
            except KeyError:
                pass
        except KeyError:
            print("Key {} does not exist for contact with phone number {}".format(key, phone_number))




def find_contact(phone_number):
    try:
        contact = contacts[str(phone_number)]
        print("Contact Name: {} Age: {}".format(contact["name"], contact["age"]))
    except KeyError:
        print("Could not find contact with phone number: {}".format(phone_number))

def subscribe(phone_number):
    subscriptions[str(phone_number)] = True


