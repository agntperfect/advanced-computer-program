CONTACTS_FILE = "contacts.txt"
WIDTH = 50

def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter contact phone: ").strip()
    
    if not name or not phone:
        print("Name and phone cannot be empty.")
        return
    
    try:
        with open(CONTACTS_FILE, "a") as file:
            file.write(f"{name},{phone}\n")
        print(f"Contact added successfully!")
    except Exception as e:
        print(f"Error adding contact: {e}")

def view_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("No contacts found.")
                return
            
            print("\n" + "Contact List")
            print("-" * WIDTH)
            for i, contact in enumerate(contacts, 1):
                name, phone = contact.strip().split(",", 1)
                print(f"{i}. {name}: {phone}")
    except FileNotFoundError:
        print("Contacts file not found. Try adding a contact first.")
    except Exception as e:
        print(f"Error reading contacts: {e}")

def search_contact():
    search_name = input("Enter name to search: ").strip().lower()
    
    try:
        with open(CONTACTS_FILE, "r") as file:
            contacts = file.readlines()
            found = False
            for contact in contacts:
                name, phone = contact.strip().split(",", 1)
                if search_name in name.lower():
                    print(f"Found: {name} - {phone}")
                    found = True
            if not found:
                print("No matching contact found.")
    except FileNotFoundError:
        print("Contacts file not found. Try adding a contact first.")
    except Exception as e:
        print(f"Error searching contacts: {e}")

def delete_contact():
    delete_name = input("Enter name to delete: ").strip().lower()
    
    try:
        with open(CONTACTS_FILE, "r") as file:
            contacts = file.readlines()
        
        new_contacts = [c for c in contacts if delete_name not in c.split(",", 1)[0].lower()]
        
        if len(new_contacts) == len(contacts):
            print("No contact found to delete.")
            return
        
        with open(CONTACTS_FILE, "w") as file:
            file.writelines(new_contacts)
        
        print(f"🗑️ Contact '{delete_name}' deleted.")
    except FileNotFoundError:
        print("Contacts file not found. Try adding a contact first.")
    except Exception as e:
        print(f"Error deleting contact: {e}")

def update_contact():
    update_name = input("Enter name to update: ").strip().lower()
    
    try:
        with open(CONTACTS_FILE, "r") as file:
            contacts = file.readlines()
        
        updated = False
        for i, contact in enumerate(contacts):
            name, phone = contact.strip().split(",", 1)
            if name.lower() == update_name:
                new_phone = input(f"Enter new phone for {name}: ").strip()
                if not new_phone:
                    print("Phone number cannot be empty.")
                    return
                contacts[i] = f"{name},{new_phone}\n"
                updated = True
                break
        
        if updated:
            with open(CONTACTS_FILE, "w") as file:
                file.writelines(contacts)
            print(f"Contact '{update_name}' updated.")
        else:
            print("No contact found to update.")
    except FileNotFoundError:
        print("Contacts file not found. Try adding a contact first.")
    except Exception as e:
        print(f"Error updating contact: {e}")

def menu():
    while True:
        print("\n" + "=" * WIDTH)
        print("Contact Book".center(WIDTH))
        print("=" * WIDTH)
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()