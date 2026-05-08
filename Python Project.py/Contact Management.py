# CONTACT MANAGEMENT SYSTEM
contacts={}

while True:
    print("\nContact Management System")
    print("1. Create Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contacts")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    if choice == '1':
        name=input("Enter contact name: ")
        if name in contacts:
            print(f"Contact '{name}' already exists.")
        else:
            phone= int(input("Enter contact phone number: "))
            email=input("Enter contact email: ")
            age=int(input("Enter contact age: "))
            if age<0:
                print("Age cannot be negative. Contact not created.")
            else:
                contacts[name]={'age':int(age),'phone':phone,'email':email}
            print(f"Contact '{name}' created successfully.")
    elif choice == '2':
    
        if contacts:
            print("\nSaved contacts:")
            for cname, contact in contacts.items():
                print(f"Name: {cname}, Age: {contact.get('age')}, Phone: {contact.get('phone')}, Email: {contact.get('email')}")
        else:
            print("No contacts saved.")

    elif choice == '3':
        name=input("Enter contact name to update: ")
        if name in contacts:
            phone=int(input("Enter new phone number: "))
            email=input("Enter new email: ")
            age=int(input("Enter new age: "))
            contacts[name]={'age':int(age),'phone':phone,'email':email}
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    elif choice == '4':
        name=input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

    elif choice == '5':
        name=input("Enter contact name to search: ")
        if name in contacts:
            contact=contacts[name]
            print(f"Name: {name}, Age:{age}, Phone:{phone}, Email:{email}")
        else:
            print(f"Contact '{name}' not found.")

    elif choice == '6':
        print(f"Total contacts: {len(contacts)}")

    elif choice == '7':
        print("Exiting Contact Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
    
    
        
    