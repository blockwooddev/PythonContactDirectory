contacts = {} #each value is also a dictionary
subscriptions = {} #doesn't really matter what the value is

def add_contact(phone_number, name, age):
    phone_number = str(phone_number)
    if phone_number not in contacts:
        contacts[phone_number] = {
            "name": name,
            "age": age
        }
    else:
        print("Contact already exists for phone number: {}".format(phone_number))

def update_contact(phone_number, key, value):
    phone_number = str(phone_number)
    key = str(key).lower()

    if phone_number not in contacts:
        print("Contact does not exist for phone number: {}".format(phone_number))
    else:
        if key in contacts[phone_number]:
            contacts[phone_number][key] = value

            if phone_number in subscriptions:
                print("You are subscribed to {} and it changed. Name: {} Age: {}".format(
                    phone_number, contacts[phone_number]["name"], contacts[phone_number]["age"]))
        else:
            print("Key {} does not exist for contact with phone number {}".format(key, phone_number))


def find_contact(phone_number):
    phone_number = str(phone_number)

    if phone_number in contacts:
        contact = contacts[phone_number]
        print("Contact Name: {} Age: {}".format(contact["name"], contact["age"]))

def subscribe(phone_number):
    subscriptions[str(phone_number)] = True


