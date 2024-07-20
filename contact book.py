import json

# Function to load contacts from a JSON file
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}
    
    return contacts

# Function to save contacts to a JSON file
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

# Function to add a new contact
def add_contact(name, phone):
    contacts = load_contacts()
    contacts[name] = phone
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.")

# Function to display all contacts
def display_contacts():
    contacts = load_contacts()
    if contacts:
        print("Contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")

# Function to search for a contact
def search_contact(name):
    contacts = load_contacts()
    if name in contacts:
        print(f"Phone number for '{name}' is: {contacts[name]}")
    else:
        print(f"Contact '{name}' not found.")

# Function to delete a contact
def delete_contact(name):
    contacts = load_contacts()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

# Main function to run the contact book application
def main():
    while True:
        print("\nWelcome to the Contact Book!")
        print("1. Add a new contact")
        print("2. Display all contacts")
        print("3. Search for a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            display_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == '4':
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == '5':
            print("Thank you for using the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()