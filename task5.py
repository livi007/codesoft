import csv

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")
    
    with open('contacts.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email, address])
    
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts():
    with open('contacts.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print("Name:", row[0])
            print("Phone:", row[1])
            print("Email:", row[2])
            print("Address:", row[3])
            print("-----------------------")

# Function to search for a contact by name or phone number
def search_contact():
    search_query = input("Enter name or phone number to search: ")
    with open('contacts.csv', 'r') as file:
        reader = csv.reader(file)
        found = False
        for row in reader:
            if search_query in row[0] or search_query in row[1]:
                print("Name:", row[0])
                print("Phone:", row[1])
                print("Email:", row[2])
                print("Address:", row[3])
                print("-----------------------")
                found = True
        if not found:
            print("Contact not found.")

# Function to update a contact
def update_contact():
    search_query = input("Enter name or phone number of the contact to update: ")
    updated_info = []
    with open('contacts.csv', 'r') as file:
        reader = csv.reader(file)
        found = False
        for row in reader:
            if search_query in row[0] or search_query in row[1]:
                print("Current details:")
                print("Name:", row[0])
                print("Phone:", row[1])
                print("Email:", row[2])
                print("Address:", row[3])
                print("-----------------------")
                name = input("Enter updated name (press enter to keep current): ")
                phone = input("Enter updated phone number (press enter to keep current): ")
                email = input("Enter updated email (press enter to keep current): ")
                address = input("Enter updated address (press enter to keep current): ")
                updated_info = [name if name else row[0], phone if phone else row[1], email if email else row[2], address if address else row[3]]
                found = True
    if found:
        with open('contacts.csv', 'r') as file:
            reader = csv.reader(file)
            lines = list(reader)
        with open('contacts.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for line in lines:
                if search_query in line[0] or search_query in line[1]:
                    writer.writerow(updated_info)
                else:
                    writer.writerow(line)
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact():
    search_query = input("Enter name or phone number of the contact to delete: ")
    with open('contacts.csv', 'r') as file:
        reader = csv.reader(file)
        lines = list(reader)
        found = False
        for line in lines:
            if search_query in line[0] or search_query in line[1]:
                lines.remove(line)
                found = True
    if found:
        with open('contacts.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(lines)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

# Main function
def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Thank you for using the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
