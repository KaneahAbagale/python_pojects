# Project: Create a phonebook application
# A user should be able to add a contact. That is name of a person and their number
# A user should be able to delete a contact
# A user should be able to edit a contact
# A user should be able to view all contacts
# A user should be able to search for a contact.

menu = "=" * 30 + \
"\nWelcome to our Phonebook App\n\n" + \
"1. Create a new contact\n"
"2. Edit a contact\n" + \
"3. View all contacts\n" + \
"4. Search for a contact\n" + \
"0. Quite" + \
"=" * 30

while True:
    print(menu)

    data = {}

    command = input(">>>")

    if command == "1":
        name = input("Enter name of contact: ")
        phone = input("Enter phone number: ")
        contact = {"name": name, "phone": phone}
        data.append(contact)
        print("Contact added successfully")
        print(data)

    elif command == "2":
        name = input("Enter the name of the contact you wish to edit")
        for i, contact in enumerate(data):
            print(f"i = {i}, contact = {contact}")       
        
    elif command == "0":
        print("Program ended. Have a nice day!")
        break