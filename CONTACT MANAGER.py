import re
contacts = {}

def capitalize_words(text):
    return text.title()

def validate_alpha(text):
    return bool(re.match(r'^[A-Za-z\s]+$', text))

def validate_email(email):

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone_number(number):
    # Check if number contains only digits and is 10-15 digits long
    return number.isdigit() and 10 <= len(number) <= 15

def add_contact():
    print("Adding a contact.")

    first_name = input("Enter first name: ").strip()
    if not validate_alpha(first_name):
        print("Invalid first name. It should contain only alphabetic characters and spaces.")
        return
    first_name = capitalize_words(first_name)

    last_name = input("Enter last name: ").strip()
    if not validate_alpha(last_name):
        print("Invalid last name. It should contain only alphabetic characters and spaces.")
        return
    last_name = capitalize_words(last_name)

    gender = input("Enter gender: ").strip()
    if not validate_alpha(gender):
        print("Invalid gender. It should contain only alphabetic characters and spaces.")
        return

    address = input("Enter address: ").strip()
    address = capitalize_words(address)

    contact_number = input("Enter contact number: ").strip()
    if not validate_phone_number(contact_number):
        print("Invalid contact number. It should be a 10-15 digit number.")
        return

    email_id = input("Enter email ID: ").strip()
    if not validate_email(email_id):
        print("Invalid email ID. Please enter a valid email address.")
        return

    contact = {
        'first_name': first_name,
        'last_name': last_name,
        'gender': gender,
        'address': address,
        'contact_number': contact_number,
        'email_id': email_id
    }

    contacts[first_name + ' ' + last_name] = contact
    print("Contact added successfully!")

def delete_contact():
    print("Deleting a contact.")
    name = input("Enter the full name of the contact to delete (first name last name): ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


def update_contact():
    print("Updating a contact.")
    name = input("Enter the full name of the contact to update (first name last name): ").strip()
    if name in contacts:
        contact = contacts[name]

        # Update each field if a new value is provided, otherwise keep the old one
        new_first_name = input(f"Enter new first name (leave blank to keep {contact['first_name']}): ").strip()
        if new_first_name and not validate_alpha(new_first_name):
            print("Invalid first name. It should contain only alphabetic characters and spaces.")
            return
        new_first_name = capitalize_words(new_first_name) or contact['first_name']

        new_last_name = input(f"Enter new last name (leave blank to keep {contact['last_name']}): ").strip()
        if new_last_name and not validate_alpha(new_last_name):
            print("Invalid last name. It should contain only alphabetic characters and spaces.")
            return
        new_last_name = capitalize_words(new_last_name) or contact['last_name']

        new_gender = input(f"Enter new gender (leave blank to keep {contact['gender']}): ").strip()
        if new_gender and not validate_alpha(new_gender):
            print("Invalid gender. It should contain only alphabetic characters and spaces.")
            return
        new_gender = new_gender or contact['gender']

        new_address = input(f"Enter new address (leave blank to keep {contact['address']}): ").strip()
        new_address = capitalize_words(new_address) or contact['address']

        new_contact_number = input(
            f"Enter new contact number (leave blank to keep {contact['contact_number']}): ").strip()
        if new_contact_number and not validate_phone_number(new_contact_number):
            print("Invalid contact number. It should be a 10-15 digit number.")
            return
        new_contact_number = new_contact_number or contact['contact_number']

        new_email_id = input(f"Enter new email ID (leave blank to keep {contact['email_id']}): ").strip()
        if new_email_id and not validate_email(new_email_id):
            print("Invalid email ID. Please enter a valid email address.")
            return
        new_email_id = new_email_id or contact['email_id']

        # Update the contact details
        contact['first_name'] = new_first_name
        contact['last_name'] = new_last_name
        contact['gender'] = new_gender
        contact['address'] = new_address
        contact['contact_number'] = new_contact_number
        contact['email_id'] = new_email_id

        # Update the key in the dictionary if the name has changed
        new_full_name = new_first_name + ' ' + new_last_name
        if new_full_name != name:
            contacts[new_full_name] = contacts.pop(name)

        print("Contact updated successfully!")
    else:
        print("Contact not found.")


# Function to search for a contact
def search_contact():
    print("Searching for a contact.")
    name = input("Enter the full name of the contact to search (first name last name): ").strip()
    if name in contacts:
        contact = contacts[name]
        print("Contact found:")
        for key, value in contact.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
    else:
        print("Contact not found.")


# Function to view all contacts
def view_contacts():
    if contacts:
        print("Contacts list:")
        for name, contact in contacts.items():
            print(f"\nName: {name}")
            for key, value in contact.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
    else:
        print("No contacts found.")


# Main menu
def menu():
    while True:
        print("\n==== Welcome to the Contact Management System ====")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Update Contact")
        print("4. Search Contact")
        print("5. View Contacts")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            delete_contact()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            view_contacts()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 6.")
menu()