import types

# global constants
consts = types.SimpleNamespace()
# menu options:
consts.CMD_SHOW = "show"
consts.CMD_GRAB = "grab"
consts.CMD_EDIT = "edit"
consts.CMD_DROP = "drop"
consts.CMD_EXIT = "exit"

items = ["wooden staff", "wizard hat", "cloth shoes"]

def main(): 
    print("The Wizard Inventory Program")
    command = ""
    while command.lower != consts.CMD_EXIT:
        command = input(display_menu())
        match command:
            case consts.CMD_SHOW:
                show_items()
            case consts.CMD_GRAB:
                grab_item()
            case consts.CMD_EDIT:
                edit_item()
            case consts.CMD_DROP:
                drop_item()
            case consts.CMD_EXIT:
                break
            case _:
                print("Unknown Command. Try again.")
    print("Bye")

def display_menu():
    menu_text = '\nCOMMAND MENU:\n'
    menu_text += f'{consts.CMD_SHOW}: Show all items\n'
    menu_text += f'{consts.CMD_GRAB}: Grab an item\n'
    menu_text += f'{consts.CMD_EDIT}: Edit an item\n'
    menu_text += f'{consts.CMD_DROP}: Drop an item\n'
    menu_text += f'{consts.CMD_EXIT}: Exit program\n'
    menu_text += '\n'
    menu_text += 'Command: '
    return menu_text

def show_items():
    print("-- Items --")
    for nbr, item in enumerate(items, start=1):
        print(f'{nbr}. {item}')

def grab_item():
    print("-- Grab Item --")
    if len(items) >= 4:
        print("You cannot carry anymore items. Please drop one first.")
    else:
        item_name = input("Item Name: ")
        items.append(item_name)
        print(f'{item_name} was added to your bag!')

def edit_item():
    print("-- Edit Item --")
    success = False
    while success != True:
        item_num = int(input("Item number: "))
        if item_num > len(items) or item_num <= 0:
            print("Invalid item number. Try again.")
        else:
            new_name = input("Updated item name: ")
            items[item_num - 1] = new_name
            print(f'Item number {item_num} was updated.')
            success = True

def drop_item():
    print("-- Drop Item --")
    success = False
    while success != True:
        item_num = int(input("Item number: "))
        if item_num > len(items) or item_num <= 0:
            print("Invalid item number. Try again.")
        else:
            item_del = items.pop(item_num - 1)
            print(f'{item_del} was deleted.')
            success = True

if __name__ == "__main__":
    main()
