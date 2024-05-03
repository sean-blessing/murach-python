import types, csv

# global constants
consts = types.SimpleNamespace()
# menu options:
consts.CMD_LIST = "list"
consts.CMD_VIEW = "view"
consts.CMD_ADD = "add"
consts.CMD_DEL = "del"
consts.CMD_EXIT = "exit"

contacts = []

def main(): 
    print("Contact Manager")
    load_contacts()
    command = ""
    while command.lower != consts.CMD_EXIT:
        command = input(display_menu())
        match command:
            case consts.CMD_LIST:
                list_contacts()
            case consts.CMD_VIEW:
                view_contact()
            case consts.CMD_ADD:
                add_contact()
            case consts.CMD_DEL:
                del_contact()
            case consts.CMD_EXIT:
                break
            case _:
                print("Unknown Command. Try again.")
    print("Bye")

def load_contacts():
    with open("contacts.csv", newline="") as contact_file:
        reader = csv.reader(contact_file)
        for row in reader:
            contacts.append([row[0], row[1], row[2]])

def save_contacts():
    with open("contacts.csv", "w", newline="") as contact_file:
        writer = csv.writer(contact_file)
        writer.writerows(contacts)

def display_menu():
    menu_text = '\nCOMMAND MENU:\n'
    menu_text += f'{consts.CMD_LIST}: Display all contacts\n'
    menu_text += f'{consts.CMD_VIEW}: View a contact\n'
    menu_text += f'{consts.CMD_ADD} : Add a contact\n'
    menu_text += f'{consts.CMD_DEL} : Delete a contact\n'
    menu_text += f'{consts.CMD_EXIT}: Exit program\n'
    menu_text += '\n'
    menu_text += 'Command: '
    return menu_text

def list_contacts():
    print("-- Contacts --")
    for nbr, contact in enumerate(contacts, start=1):
        print(f'{nbr}. {contact[0]}')

def view_contact():
    print("-- View Contact --")
    success = False
    while success != True:
        nbr = int(input("Contact Number: "))
        if nbr < 1 or nbr > len(contacts):
            print(f"Invalid contact #({nbr}). Try again.")
        else:
            contact = contacts[nbr - 1]
            print(f"Name:  {contact[0]}")
            print(f"Email: {contact[1]}")
            print(f"Phone: {contact[2]}")
            success = True

# Start here
def add_contact():
    print("-- Add Contact --")
    name = input("Name:    ")
    email = input("Email: ")
    phone = input("Phone: ")
    contacts.append([name, email, phone])
    save_contacts()
    print(f"{name} was added.")

def del_contact():
    print("-- Delete Contact --")
    success = False
    while success != True:
        nbr = int(input("Contact number: "))
        if nbr > len(contacts) or nbr <= 0:
            print("Invalid item number. Try again.")
        else:
            cont_del = contacts.pop(nbr - 1)
            print(f'{cont_del[0]} was deleted.')
            success = True
    save_contacts()

if __name__ == "__main__":
    main()